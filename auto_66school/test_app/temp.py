import unittest
import importlib.util
import os


def run_unit_tests(unit_test_path):
    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(unit_test_path))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)
    # Return result as string
    if result.wasSuccessful():
        return ("測試通過", "沒有錯誤")
    elif result.failures:
        return "錯誤的運行結果", result.failures[0][1]
    elif result.errors:
        return "錯誤的語法", result.errors[0][1]


unit_test_path = (
    "/Users/fuqianzhi/Desktop/自動化66school/auto_66school/test_app/tests.py"
)
run_unit_tests(unit_test_path)
