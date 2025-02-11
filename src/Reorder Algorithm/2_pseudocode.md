FUNCTION calculate_bit_jumps(binary_nums: LIST OF STRINGS) -> LIST OF TUPLES (int, int, int)
    jumps = CREATE A SET
    FOR i = 0 TO LENGTH OF binary_nums - 1
        FOR j = i + 1 TO LENGTH OF binary_nums - 1
            jump_count = SUM OF 1 FOR EACH ELEMENT x, y IN ZIP OF binary_nums[i] AND binary_nums[j] IF x != y
            jumps.ADD((i, j, jump_count))
            jumps.ADD((j, i, jump_count))
    RETURN LIST(jumps)

FUNCTION get_optimal_order(binary_nums: LIST OF STRINGS) -> LIST OF INTEGERS
    jumps = calculate_bit_jumps(binary_nums)
    order = [0]
    remaining_nums = SET OF INTEGERS FROM 1 TO LENGTH OF binary_nums - 1
    WHILE remaining_nums IS NOT EMPTY
        bit_jumps = [(j, k, jump) FOR j, k, jump IN jumps IF j = order[-1] AND k IN remaining_nums]
        next_num = MIN(bit_jumps, KEY=LAMBDA x: x[2])[1]
        order.APPEND(next_num)
        remaining_nums.REMOVE(next_num)
    RETURN order
