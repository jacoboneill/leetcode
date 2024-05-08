import pytest
from solution import Solution

test_cases = [
    (121, True),
    (-121, False),
    (10, False),
]


@pytest.mark.parametrize("x, expected_output", test_cases)
def test_palindrome_number(x, expected_output):
    assert Solution().isPalindrome(x) == expected_output


if __name__ == "__main__":
    pytest.main()
