from django.urls import path
from .views import Home, AutoTest, Welcome

urlpatterns = [
    path("", Welcome.as_view(), name="welcome"),
    path("Home/", Home.as_view(), name="home"),
    path("Home/<str:category>/", Home.as_view(), name="category"),
    path("Home/<str:category>/<str:level>/", Home.as_view(), name="level"),
    path(
        "<str:category>/<str:level>/<str:question>",
        AutoTest.as_view(),
        name="autotest",
    ),
    # 未來將新增功能
    path("temp", Welcome.as_view(), name="temp"),
]
