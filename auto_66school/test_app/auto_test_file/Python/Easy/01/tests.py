import importlib
import Unitest.ans


from unittest.mock import patch
import unittest
from io import StringIO


class TestSum(unittest.TestCase):
    def setUp(self):
        # Reload the module to get the latest version of sum_of_values
        importlib.reload(Unitest.ans)

        # Now you can use the latest version of sum_of_values
        from Unitest.ans import sum_of_values

        self.sum_of_values = sum_of_values

    @patch("builtins.input", side_effect=["3", "1", "2", "3"])
    def test_sum_of_values(self, mock_input):
        expected_output = "1+2+3=6\n"
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            self.sum_of_values()
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch("builtins.input", side_effect=["5", "10", "20", "30", "40", "50"])
    def test_sum_of_values_with_5_inputs(self, mock_input):
        expected_output = "10+20+30+40+50=150\n"
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            self.sum_of_values()
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch("builtins.input", side_effect=["1", "0"])
    def test_sum_of_zero(self, mock_input):
        expected_output = "0=0\n"
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            self.sum_of_values()
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch("builtins.input", side_effect=["2", "1000", "-500"])
    def test_sum_of_positive_and_negative_numbers(self, mock_input):
        expected_output = "1000+-500=500\n"
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            self.sum_of_values()
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    unittest.main()
