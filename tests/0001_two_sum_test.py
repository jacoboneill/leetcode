import pytest
from solution import Solution

test_cases = [
    ([2, 7, 11, 15], 9, [0, 1]),
    ([3, 2, 4], 6, [1, 2]),
    ([3, 3], 6, [0, 1]),
]


@pytest.mark.parametrize("nums, target, expected_output", test_cases)
def test_two_pointer(nums, target, expected_output):
    assert Solution().twoSum(nums, target) == expected_output


if __name__ == "__main__":
    pytest.main()
