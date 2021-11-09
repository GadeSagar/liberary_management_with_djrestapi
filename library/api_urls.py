from django.urls import path
from . import api

urlpatterns = [
    path("list/",api.ListBookAPIView.as_view(),name="book_list"),
    path("create/", api.CreateBookAPIView.as_view(),name="book_create"),
    path("update/<int:pk>/",api.UpdateBookAPIView.as_view(),name="update_book"),
    path("delete/<int:pk>/",api.DeleteBookAPIView.as_view(),name="delete_book")
]