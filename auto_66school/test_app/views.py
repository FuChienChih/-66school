from django.shortcuts import render, redirect
from django.views.generic import View
from .models import run_unit_tests, write_to_file

unit_test_path = (
    "/Users/fuqianzhi/Desktop/自動化66school/auto_66school/test_app/tests.py"
)

ans_path = "/Users/fuqianzhi/Desktop/自動化66school/auto_66school/test_app/Unitest/ans.py"

# 這裡會寫一個主頁路徑，用來決定要去哪個解題區
class Index(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        input_value = request.POST.get("inputField")
        write_to_file(input_value, ans_path)
        data = {}
        data["test_result"], data["error"] = run_unit_tests(unit_test_path)
        return render(request, "index2.html", data)


# 首頁
# class Home(View):
#     def get(self, request):
#         # 在初始請求中，渲染可選擇的按鈕
#         btn = {
#             "Python": "Python",
#             "ML": "ML機器學習",
#             "BigData": "BigData大數據",
#             "DL": "DL深度學習",
#             "NLP": "NLP自然語言處理",
#         }
#         context = {"btn": btn}
#         return render(request, "home.html", context)

#     def post(self, request):
#         return redirect("Home/Python")

#     def category(self, request):
#         btn = {
#             "Easy": "初階",
#             "Medium": "中階",
#             "Hard": "高階",
#         }
#         context = {
#             "btn": btn,
#         }
#         return render(request, "home.html", context)

#     def level(self, request, category, level):
#         btn = {f"{i:03d}": f"{i:03d}" for i in range(1, 11)}
#         context = {"btn": btn, "category": category, "level": level}
#         return render(request, "home.html", context)

#     def question(self, request, category, level, question):
#         context = {"category": category, "level": level, "question": question}

#         return render(request, "home.html", context)

# class Home(View):
#     def get(self, request):
#         print("==============get=================")
#         # 在初始請求中，渲染可選擇的按鈕
#         btn = {
#             "test": "測試用",
#         }
#         context = {"btn": btn}
#         return render(request, "home.html", context)

#     def post(self, request):
#         button = request.POST.get("button")
#         if button == "test":
#             return redirect("test_post")
#         else:
#             return redirect("home/")

#     def test(self, request):
#         print("=============test=================")
#         return render("index2.html")
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
            當觸發btn請求時執行。

        Returns
        -------
        TYPE
            會根據使用者是否選擇了
            “課堂”“難度”“序號”來決定
            Returns，若都選擇，會進入...

        """
        current_path = request.path
        button_value = request.POST.get("button")
        if button_value in ["Python", "ML", "BigData", "DL", "NLP"]:
            print(button_value)
            print(f"{current_path}{button_value}/")
            return redirect(f"{current_path}{button_value}/")

        elif button_value in ["Easy", "Medium", "Hard"]:
            print(button_value)
            print(f"{current_path}{button_value}/")
            return redirect(f"{current_path}{button_value}/")

        elif button_value in [f"{i:02d}" for i in range(1, 11)]:
            print(button_value)
            print(f"{current_path}{button_value}/")
            return redirect(f"{current_path}{button_value}/")


# 這裡會寫一個各個解題區的副程式，用來被繼承。
class father(View):
    pass
