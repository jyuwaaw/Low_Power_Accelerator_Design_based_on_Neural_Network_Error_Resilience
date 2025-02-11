def calculate_bit_jumps(binary_nums: List[str]) -> List[Tuple[int, int, int]]:
    # Calculate the bit jump count between each pair of binary numbers
    jumps = set()
    for i in range(len(binary_nums)):
        for j in range(i+1, len(binary_nums)):
            jump_count = sum([1 for x, y in zip(binary_nums[i], binary_nums[j]) if x != y])
            jumps.add((i, j, jump_count))
            jumps.add((j, i, jump_count))
    return list(jumps)

def get_optimal_order(binary_nums: List[str]) -> List[int]:
    # Calculate bit jump counts between binary numbers
    jumps = calculate_bit_jumps(binary_nums)
    
    # Initialize order with first binary number
    order = [0]
    remaining_nums = set(range(1, len(binary_nums)))
    
    # Iterate over remaining binary numbers and add to order
    while remaining_nums:
        bit_jumps = [(j, k, jump) for j, k, jump in jumps if j == order[-1] and k in remaining_nums]

        next_num = min(bit_jumps, key=lambda x: x[2])[1]
        order.append(next_num)
        remaining_nums.remove(next_num)

    return order