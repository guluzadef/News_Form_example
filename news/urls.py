from django.urls import path
from .views import CreateNews,Test,NewsDetail

urlpatterns = [
    path("create/", CreateNews.as_view(), name="create"),
    path("", Test.as_view(), name="test"),
    path('detail/<int:pk>/',NewsDetail.as_view(),name="detail")

]
