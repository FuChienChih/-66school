import os
import unittest
import importlib.util


def run_unit_tests(func, unit_test_path):
    # Dynamically load the test module
    spec = importlib.util.spec_from_file_location(
        "test_module", unit_test_path
    )
    test_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(test_module)

    # Discover and run tests
    loader = unittest.TestLoader()
    suite = loader.discover(os.path.dirname(unit_test_path))
    runner = unittest.TextTestRunner()
    result = runner.run(suite)

    # Return result as string
    if result.wasSuccessful():
        return "測試通過"
    elif result.failures:
        return "錯誤的運行結果:", result.failures[0][1]
    elif result.errors:
        return "錯誤的語法:", result.errors[0][1]
