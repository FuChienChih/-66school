# from django.db import models
import os
import unittest


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


def create_py_file(string, path):
    filename = f"{string}"
    filepath = os.path.join(path, filename)
    with open(filepath, "w") as f:
        f.write(string)


def run_py_files(path):
    for filename in os.listdir(path):
        if filename.endswith(".py"):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                code = compile(f.read(), filepath, "exec")
                exec(code)
