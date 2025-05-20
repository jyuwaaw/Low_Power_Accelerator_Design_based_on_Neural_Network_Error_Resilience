# Low power Accelerator Design based on Neural Network Error Resilience Characteristics

*Last Revision: Jun/7/2023*

This document summarizes the key ideas and contributions of the research on **data reordering to reduce power consumption in Deep Neural Network (DNN) accelerators**.

## 1. Introduction

**Deep Neural Networks (DNNs)** power many modern AI applications such as image recognition, speech recognition, autonomous driving, etc. As these models grow in complexity and scale, their computational and **energy demands** increase significantly.

In **low-power scenarios** (IoT devices, wearables, sensors, etc.), limited hardware resources and battery life constraints require more efficient DNN deployments. Traditional approaches to lower power include:
- Minimizing memory accesses (data reuse, compression, prefetching).
- Exploiting sparsity (pruning, SCNN, etc.).
- Using dynamic voltage scaling (DVS) and near-threshold computing (e.g., Razor, Thundervolt).
  
However, achieving large power reductions *while* keeping high inference accuracy remains a challenge. This research introduces a **data reordering** technique that leverages:
1. **DNN fault tolerance** (minor calculation errors have limited impact on final accuracy).
2. **Timing slack** in circuits (not every input triggers the worst-case path).

## 2. Key Motivation & Idea

- **Timing Slack**: Static timing analysis must guarantee correctness for the worst-case path (i.e., maximum delay). But many real input patterns do not trigger that path.
- **Bit Flips & Delay**: In an 8-bit multiplier, large or high-bit flips often cause longer computation delays. If the input data sequence is re-ordered to minimize drastic bit-position changes, the *actual* delays become lower or shorter more often.
- **Dynamic Voltage/Frequency Scaling(DVFS)**: Once most operations avoid the high-delay scenario, we can safely lower the supply voltage or clock period. Due to the DNN’s inherent fault tolerance, occasional timing violations won’t drastically degrade accuracy.

## 3. Methodology

### 3.1 Single-PE Modeling and Gate-Level Simulation

1. **Multiplier Selection**  
   - Used Synopsys `DW02` 8-bit multiplier as the processing element (PE).
   - Synthesized and placed/routed in a 90nm process.
   - Extracted delay data through exhaustive input tests (all 8-bit pairs).

2. **Observations**  
   - Most input pairs do *not* trigger the worst-case delay path.
   - High-bit flips near carry chains produce longer delays.





<div style="display: flex; gap: 20px; justify-content: center;">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter2/bit_flip_pos.png" alt="Pic 1" style="width: 30%;">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter2/Snipaste_2023-06-03_18-54-26.jpg" alt="Pic 2" style="width: 30%;">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter2/bitjumpsquant.jpg" alt="Pic 3" style="width: 30%;">
</div>

   - Delay distribution is skewed toward lower values, suggesting potential for voltage scaling or clock period reduction.

3. **Fundamental Low Power Technique**
   - Power gating for unused PEs
      - For a large PE array, 64×64 for example, the systolic array will benefit from switching off partial of it's array to achieve an even lower power consumption.
   - Reduced memory access
      - Input Stationary (IS) dataflow was implemented, in this case, the occurances of fetching input feature map from memory significantly reduced. Previously, the **N** feature map will compute with **M** weight matrices, total **N × M** times of memory fetch. By implementing IS dataflow, we reduced the total number of memory fetching from **N × M** to **M** only.
   - UPF for the PE(Later in VCS NLP)
      ``` C++
      ## CREATE POWER DOMAINS
      ######################
      create_power_domain TOP
      create_power_domain MULT  -elements Multiplier

      ## TOPLEVEL CONNECTIONS
      #######################
      # VDD
      create_supply_port VDD 
      create_supply_net  VDD   -domain TOP
      connect_supply_net VDD   -ports VDD

      # VSS
      create_supply_port VSS 
      create_supply_net  VSS   -domain TOP
      create_supply_net  VSS   -domain MULT -reuse

      connect_supply_net VSS   -ports VSS

      ## PRIMARY POWER NETS
      #####################
      set_domain_supply_net TOP   -primary_power_net VDD   -primary_ground_net VSS
      set_domain_supply_net MULT  -primary_power_net VDDMS -primary_ground_net VSS


      ## MULT SETUP
      #############
      # SWITCH
      create_power_switch mult_sw \
        -domain MULT \
        -input_supply_port {in VDDM} \
        -output_supply_port {out VDDMS} \
        -control_port {mult_on mult_on} \
        -on_state {mac_u in {!mult_on}}

      # ISO
      set_isolation mult_iso_out \
        -domain MULT \
        -isolation_power_net VDD -isolation_ground_net VSS \
        -clamp_value 1 \
        -applies_to outputs 

      set_isolation_control mult_iso_out \
        -domain MULT \
        -isolation_signal mult_iso_out \
        -isolation_sense high \
        -location parent

      # ADD PORT STATE INFO
      #####################
      add_port_state VDD   -state {HV  1.2}

      add_port_state VDDM  -state {HV  1.2}

      add_port_state mult_sw/out -state {HV  1.2}\
                                -state {OFF off}
                                
      ## CREATE PST#############
      create_pst chiptop_pst -supplies{}
      ```
<figure style="text-align:center;">
  <p align="center">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/PE_off.jpg" alt="PE array Power Gating" width="400">
    </p>
</figure>

### 3.2 Data Reordering Algorithm



1. **Goal**: Minimize adjacent bit flips in an input (or weight) sequence without altering the final accumulation result.
2. **Implementation**  
   - Compute pairwise bit-flip costs via XOR.
   - Use a greedy or heuristic method to reorder the sequence so that *neighboring data* have fewer and/or lower-position bit flips.

<figure style="text-align:center;">
  <p align="center">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter3/pseudo_3.2.png" alt="Reordering Algorithm" width="400">
    </p>
</figure>

3. **Experiments**  
   - Used Synopsys `DW02` 8-bit multiplier as the processing element (PE). Synthesized and placed/routed in a 90nm process. Extracted delay data through exhaustive input tests (all 8-bit pairs).
   - Selected **AlexNet’s third convolution layer** weights as test data.
   - Fixed certain input activations (e.g., 127, 255) to simulate MAC operations in a single PE or small PE array.
   - Results show **significant** reduction in high-delay occurrences after data reordering.
  
<figure style="text-align:center;">
  <p align="center">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter3/reordered_data.png"  width="500">
    </p>
</figure>

### 3.3 Accelerator Mapping & Dataflow

1. **Input-Stationary Dataflow**  
   - Keep input activations in local storage; traverse weight sequences.
   - Reorder the weight sequence offline, then map to the array for MAC operations.
   - Use coordinate/index tracking to accumulate partial sums correctly.
2. **SCNN Integration**  
   - SCNN compresses sparse weights & activations, maintaining index lists.
   - The proposed reordering can be integrated with minimal hardware overhead, reusing SCNN’s existing coordinate system to place partial sums accurately.

## 4. Experimental Results

- **Delay Distribution Improvement**  
  - Before reordering: high-delay cases occur more frequently due to large bit flips.
  - After reordering: these cases drop significantly, pushing most delay paths below a lower threshold.
- **Dynamic Voltage/Frequency Scaling**  
  - Originally we have the PE running at 1 GHz, by obesrving the delay distribution, we can tell that most of the delay lies near 5000ps. To implement Dynamic Voltage/Frequency Scaling(**DVFS**) we set the bottomline of model accuracy to 85%. A sweep script exercises the PE at frequencies from 1 GHz downwards, measuring the induced error rate and resulting model accuracy. And ultimately we find that by dropping the clock frequency to 297.2MHz, we can still meet the bottomline with 85.72% accuracy. 
  
  - As we stretch the clock period beyond the bulk of the delay distribution, occasional paths will exceed the period and produce timing errors.Because the network’s weights and activations inherently smooth out small numbers of errors, accuracy degrades gradually rather than collapsing.

    | Clock Frequency | Model Accuracy |
    | :-------------: | :------------: |
    |      1 GHz      |     99.8 %     |
    |    297.2 MHz    |     85.72 %    |

  Key takeaway: By leveraging the neural network’s graceful degradation under sparse timing errors, DVFS can push the PE well below its worst-case frequency, slashing power consumption while respecting a user-defined accuracy floor.
- **Dataflow Implementation Feasibility**  
  - No extra hardware is strictly required if integrated in an architecture like SCNN (where indexes/coordinates are already tracked).
  - For other designs, minimal overhead is needed for coordinate mapping.

<figure style="text-align:center;">
  <p align="center">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter4/arch_1.png" width="600">
    </p>
</figure>

<figure style="text-align:center;">
  <p align="center">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter4/arch_2.png"  width="600">
    </p>
</figure>

## 5. Conclusion & Future Work

- **Major Contributions**  
  1. Demonstrates **data-sequence reordering** as a low-power technique, exploiting bit-flip patterns and timing slack. 
  2. Introduces fine-tuned dynamic voltage and frequency scaling by observing trade-offs between an acceptable model accuracy and 
  3. Uses real gate-level data to validate how reordering reduces average delay in an 8-bit MAC design.  
  4. Proposes a mapping strategy in existing accelerator architectures (e.g., SCNN) without additional hardware cost.

- **Future Directions**  
  1. Investigate reordering in combination with advanced pruning or quantization techniques.  
  2. Evaluate performance on more varied network layers (deeper or more complex topologies).  
  3. Prototype a module on `Flexibit` to quantify real-world power and accuracy trade-offs.

## References

1. Chen, Y. et al. "Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks."  
2. Parashar, A. et al. "SCNN: An Accelerator for Compressed-sparse Convolutional Neural Networks."  
3. Ernst, D. et al. "Razor: Circuit-level Correction of Timing Errors for Low-Power Operation."  
4. Zhang, J. et al. "Thundervolt: Leveraging Cross-Layer Approximations for High-Efficiency Deep Learning Accelerators."  
5. ... [More references in the main text]

