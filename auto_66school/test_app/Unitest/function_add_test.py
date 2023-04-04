import unittest
from io import StringIO
from unittest.mock import patch
from .ans import sum_of_values


# def sum_of_values():
#     values = []
#     sum_ = 0  # 這個部分assertEqual查不到
#     str_ = ""
#     n = int(input("你將輸入n個正整數"))
#     for i in range(n):
#         value = int(input(f"第{i+1}個正整數"))
#         sum_ += value
#         values.append(value)
#         str_ = str_ + str(value) + "+"
#     print(str_[:-1] + "=" + str(sum(values)))


class TestSum(unittest.TestCase):
    @patch("builtins.input", side_effect=["3", "1", "2", "3"])
    def test_sum_of_values(self, mock_input):
        expected_output = "1+2+3=6\n"
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            sum_of_values()
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch("builtins.input", side_effect=["5", "10", "20", "30", "40", "50"])
    def test_sum_of_values_with_5_inputs(self, mock_input):
        expected_output = "10+20+30+40+50=150\n"
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            sum_of_values()
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch("builtins.input", side_effect=["1", "0"])
    def test_sum_of_zero(self, mock_input):
        expected_output = "0=0\n"
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            sum_of_values()
        self.assertEqual(captured_output.getvalue(), expected_output)

    @patch("builtins.input", side_effect=["2", "1000", "-500"])
    def test_sum_of_positive_and_negative_numbers(self, mock_input):
        expected_output = "1000+-500=500\n"
        captured_output = StringIO()
        with patch("sys.stdout", captured_output):
            sum_of_values()
        self.assertEqual(captured_output.getvalue(), expected_output)


unittest.main()
