import unittest
from .adaptative_batch_gradient_descent import adapt_learning_rate

class TestCalculator(unittest.TestCase):
    """Unit tests for the Calculator class."""

    def setUp(self):
        """Initialization before each test."""

    def test_adapt_learning_rate_0(self):
        """Should return same learning rate when previous error is infinity."""
        learning_rate = 1
        previous_error = float('inf')
        new_error = 90

        self.assertEqual(adapt_learning_rate(learning_rate, previous_error, new_error), learning_rate)

    def test_adapt_learning_rate_1(self):
        """Should return learning rate multiplied by 2 when the error decreased by 10%."""
        learning_rate = 1
        previous_error = 100
        new_error = 90

        self.assertEqual(adapt_learning_rate(learning_rate, previous_error, new_error), 2)

    def test_adapt_learning_rate_2(self):
        """Should return learning rate divided by 2 when the error decreased by 20%."""
        learning_rate = 1
        previous_error = 100
        new_error = 80

        self.assertEqual(adapt_learning_rate(learning_rate, previous_error, new_error), 0.5)

    def test_adapt_learning_rate_3(self):
        """Should return learning rate multiplied by 2 when the error decreased by less than 10%."""
        learning_rate = 1
        previous_error = 100
        new_error = 91

        self.assertEqual(adapt_learning_rate(learning_rate, previous_error, new_error), 2)

    def test_adapt_learning_rate_4(self):
        """Should return learning rate divided by 2 when the error decreased by more than 20%."""
        learning_rate = 1
        previous_error = 100
        new_error = 79

        self.assertEqual(adapt_learning_rate(learning_rate, previous_error, new_error), 0.5)

    def test_adapt_learning_rate_5(self):
        """Should return learning rate divided by 2 when the new error is higher thant the previoous one"""
        learning_rate = 1
        previous_error = 100
        new_error = 2000

        self.assertEqual(adapt_learning_rate(learning_rate, previous_error, new_error), 0.5)



if __name__ == '__main__':
    unittest.main()