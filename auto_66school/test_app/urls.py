from django.urls import path
from .views import Home, AutoTest

urlpatterns = [
    # path("", Index.as_view(), name="index-view"),
    path("Home/", Home.as_view(), name="home"),
    path("Home/<str:category>/", Home.as_view(), name="category"),
    path("Home/<str:category>/<str:level>/", Home.as_view(), name="level"),
    path(
        "<str:category>/<str:level>/<str:question>",
        AutoTest.as_view(),
        name="autotest",
    ),
]
