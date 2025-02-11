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
- **Reduced Operating Voltage**: Once most operations avoid the high-delay scenario, we can safely lower the supply voltage or clock period. Due to the DNN’s inherent fault tolerance, occasional timing violations won’t drastically degrade accuracy.

## 3. Methodology

### 3.1 Single-PE Modeling and Gate-Level Simulation

1. **Multiplier Selection**  
   - Used Synopsys `DW02` 8-bit multiplier as the processing element (PE).
   - Synthesized and placed/routed in a 90nm process.
   - Extracted delay data through exhaustive input tests (all 8-bit pairs).

2. **Observations**  
   - Most input pairs do *not* trigger the worst-case delay path.
   - High-bit flips near carry chains produce longer delays.
   - Delay distribution is skewed toward lower values, suggesting potential for voltage scaling or clock period reduction.

### 3.2 Data Reordering Algorithm

![Reordering Algorithm](https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter3/pseudo_3.2.png "Reordering Algorithm")

<figure style="text-align:center;">
  <img src="https://github.com/jyuwaaw/Neural_Network_Error_Resilience_Low_Power_Accelerator_Design/blob/main/pics/Chapter3/pseudo_3.2.png" alt="Reordering Algorithm" width="300">
  <figcaption>Reordering Algorithm Pseudocode.</figcaption>
</figure>


1. **Goal**: Minimize adjacent bit flips in an input (or weight) sequence without altering the final accumulation result.
2. **Implementation**  
   - Compute pairwise bit-flip costs via XOR.
   - Use a greedy or heuristic method to reorder the sequence so that *neighboring data* have fewer and/or lower-position bit flips.
3. **Experiments**  
   - Selected **AlexNet’s third convolution layer** weights as test data.
   - Fixed certain input activations (e.g., 127, 255) to simulate MAC operations in a single PE or small PE array.
   - Results show **significant** reduction in high-delay occurrences after data reordering.

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
- **Voltage/Frequency Scaling Potential**  
  - With fewer worst-case delays, one can scale down the voltage (or tighten the clock) to reduce power. DNN fault tolerance ensures minimal impact on final accuracy.
- **Implementation Feasibility**  
  - No extra hardware is strictly required if integrated in an architecture like SCNN (where indexes/coordinates are already tracked).
  - For other designs, minimal overhead is needed for coordinate mapping.

## 5. Conclusion & Future Work

- **Major Contributions**  
  1. Demonstrates **data-sequence reordering** as a low-power technique, exploiting bit-flip patterns and timing slack.  
  2. Uses real gate-level data to validate how reordering reduces average delay in an 8-bit MAC design.  
  3. Proposes a mapping strategy in existing accelerator architectures (e.g., SCNN) without additional hardware cost.

- **Limitations**  
  - Only examined **input-stationary** dataflow in detail; other dataflows (weight-stationary, output-stationary) remain untested.  
  - Explored single or small PE arrays; large-scale deployment may involve more complex scheduling, memory considerations, or multi-layer reordering.

- **Future Directions**  
  1. Investigate reordering in combination with advanced pruning or quantization techniques.  
  2. Evaluate performance on more varied network layers (deeper or more complex topologies).  
  3. Prototype on FPGA/ASIC to quantify real-world power and accuracy trade-offs.

## References

1. Chen, Y. et al. "Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks."  
2. Parashar, A. et al. "SCNN: An Accelerator for Compressed-sparse Convolutional Neural Networks."  
3. Ernst, D. et al. "Razor: Circuit-level Correction of Timing Errors for Low-Power Operation."  
4. Zhang, J. et al. "Thundervolt: Leveraging Cross-Layer Approximations for High-Efficiency Deep Learning Accelerators."  
5. ... [More references in the main text]

