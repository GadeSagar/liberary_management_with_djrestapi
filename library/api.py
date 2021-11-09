from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class ListBookAPIView(ListAPIView):
    """This endpoint list all of the available Books from the database"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class CreateBookAPIView(CreateAPIView):
    """This endpoint allows for creation of a bBook"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class UpdateBookAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific book by passing in the id of the todo to update"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class DeleteBookAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific book from the database"""
    queryset = Book.objects.all()
    serializer_class = BookSerializer