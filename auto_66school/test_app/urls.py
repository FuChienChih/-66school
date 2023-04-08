from django.urls import path
from .views import Index, Home

urlpatterns = [
    path("", Index.as_view(), name="index-view"),
    path("Home/", Home.as_view(), name="home"),
    path("Home/<str:category>/", Home.as_view(), name="category"),
    path("Home/<str:category>/<str:level>/", Home.as_view(), name="level"),
]
