import pytest
from EvenOrOdd import *

class TestSolution:
    def test_even_number(self):
        sol = Solution()
        assert sol.evenOrOdd(2) is True

    def test_odd_number(self):
        sol = Solution()
        assert sol.evenOrOdd(3) is False

    def test_zero(self):
        sol = Solution()
        assert sol.evenOrOdd(0) is True

    def test_negative_even(self):
        sol = Solution()
        assert sol.evenOrOdd(-4) is True

    def test_negative_odd(self):
        sol = Solution()
        assert sol.evenOrOdd(-7) is False