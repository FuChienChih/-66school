from django.shortcuts import render
from django.views.generic import View
from .temp import run_unit_tests

unit_test_path = (
    "/Users/fuqianzhi/Desktop/自動化66school/auto_66school/test_app/tests.py"
)


class Index(View):
    def get(self, request):
        data = {"name": "Adam", "age": 18}
        return render(request, "index.html", data)

    def post(self, request):
        input_value = request.POST.get("inputField")
        data = {}
        data["test_result"], data["error"] = run_unit_tests(unit_test_path)
        return render(request, "index2.html", data)
