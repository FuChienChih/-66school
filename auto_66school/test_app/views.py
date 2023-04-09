from django.shortcuts import render, redirect
from django.views.generic import View
from .models import run_unit_tests, write_to_file
import os


# 解題區~包含答案上傳以及答案反饋
class AutoTest(View):
    def get(self, request, *args, **kwargs):
        return render(request, "index.html")

    def post(self, request, *args, **kwargs):
        # 找到test.py(單元測試)路徑
        category, level, question = request.path.split("/")[1:4]
        path = f"auto_test_file/{category}/{level}/{question}"
        unit_test_path = os.path.abspath(os.path.join(__file__, f"../{path}"))
        # 根據使用者學號定義ans.py路徑
        ans_path = os.path.abspath(
            os.path.join(__file__, f"../{path}/Unitest/ans.py")
        )
        # 將ans寫入ans_path讓test.py(單元測試)引用
        input_value = request.POST.get("inputField")
        write_to_file(input_value, ans_path)
        # 準備輸出結果
        data = {}
        data["test_result"], data["error"] = run_unit_tests(unit_test_path)
        return render(request, "index2.html", data)


# 首頁
class Home(View):
    # 有哪些課堂
    categories = ["Python", "ML", "BigData", "DL", "NLP"]
    levels = ["Easy", "Medium", "Hard"]
    questions = [f"{i:02d}" for i in range(1, 11)]

    def get(self, request, *args, **kwargs):
        current_path = request.path
        # 如果沒有任何的課程類別在current_path中，渲染選擇類別按鈕
        if not any(category in current_path for category in self.categories):
            btn = {
                "Python": "Python",
                "ML": "ML機器學習",
                "BigData": "BigData大數據",
                "DL": "DL深度學習",
                "NLP": "NLP自然語言處理",
            }
            context = {"btn": btn}
            return render(request, "home.html", context)
        # 如果沒有任何的難度(level)在current_path中，渲染選擇難度(level)按鈕
        elif not any(level in current_path for level in self.levels):
            # 設定初級中級高級按鈕
            btn = {
                "Easy": "初階",
                "Medium": "中階",
                "Hard": "高階",
            }
            context = {"btn": btn}
            return render(request, "home.html", context)
        # 如果沒有任何的題號在current_path中，渲染選擇題號按鈕
        elif not any(question in current_path for question in self.questions):
            btn = {f"{i:02d}": f"{i:02d}" for i in range(1, 11)}
            context = {"btn": btn}
            return render(request, "home.html", context)

    def post(self, request, *args, **kwargs):
        """
        Parameters
        ----------
        request : TYPE
            使用者request。
            這裡用來獲取url與獲取使用者點選的btn值

        Returns
        -------
        TYPE
            會根據使用者選擇的
            “課堂”“難度”“題號”來決定
            導向相對應的url
        """
        current_path = request.path
        button_value = request.POST.get("button")
        if button_value in ["Python", "ML", "BigData", "DL", "NLP"]:
            return redirect(f"{current_path}{button_value}/")

        elif button_value in ["Easy", "Medium", "Hard"]:
            return redirect(f"{current_path}{button_value}/")

        elif button_value in [f"{i:02d}" for i in range(1, 11)]:
            # 進入此判斷式代表選擇結束，導向解題區
            current_path_list = current_path.split("/")
            new_path = "/".join(current_path_list[2:4]) + f"/{button_value}"
            return redirect("/" + new_path)


# 這裡會寫一個各個解題區的副程式，用來被繼承。
class father(View):
    pass
