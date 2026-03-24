def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Function that takes in a list of integers and a target integer, and returns the indices of the two numbers that add up to the target.

    Args:
        nums (list[int]): List of integers.
        target (int): Target integer.
    
    Returns:
        list[int]: Indices of the two numbers that add up to the target.
    """
    num_to_index = {}
    for index, num in enumerate(nums):
        # Bug Fix: Subtract the current number from the target
        complement = target - num 
        
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
        
    return []  # In case there is no solution