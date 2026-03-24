# test_labs.py
from lab_1c import max_subarray_sum
from lab_1d import two_sum

# --- Tests for lab_1c (Maximum Subarray) ---

def test_max_subarray_standard():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6

def test_max_subarray_all_negatives():
    # Should return the single largest negative number
    assert max_subarray_sum([-5, -2, -9, -12]) == -2

def test_max_subarray_all_positives():
    # Should sum the entire array
    assert max_subarray_sum([1, 2, 3, 4]) == 10

def test_max_subarray_single_element():
    assert max_subarray_sum([5]) == 5
    assert max_subarray_sum([-3]) == -3

def test_max_subarray_empty_list():
    # Edge case handling
    assert max_subarray_sum([]) == 0


# --- Tests for lab_1d (Two Sum) ---

def test_two_sum_standard():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_with_negatives():
    assert two_sum([-3, 4, 3, 90], 0) == [0, 2]
    
def test_two_sum_same_values():
    # Target requires using two identical numbers at different indices
    assert two_sum([3, 3], 6) == [0, 1]

def test_two_sum_target_at_end():
    assert two_sum([1, 2, 3, 4, 5], 9) == [3, 4]

def test_two_sum_no_solution():
    # Edge case where no solution exists
    assert two_sum([1, 2, 3], 10) == []