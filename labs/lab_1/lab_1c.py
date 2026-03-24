def max_subarray_sum(nums: list[int]) -> int:
    """
Function that takes in a list of integers and returns the maximum 
sum of any contiguous subarray.
    Args:
        nums (list[int]): List of integers.

    Returns:
        int: The maximum sum of any contiguous subarray. Returns 0 if the list is empty.
    """
    # Edge case: Empty list
    if not nums:
        return 0

    max_current = max_global = nums[0]
    
    # Start iterating from the second element
    for num in nums[1:]:
        max_current = max(num, max_current + num)
        
        # Bug Fix: Update global max if current is GREATER
        if max_current > max_global:
            max_global = max_current
            
    return max_global