from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view 

from .models import Book
from .serializers import BookListSerializer, BookSerializer

@api_view(['GET'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookListSerializer(books, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def book_detail(request, book_pk):
    book = Book.objects.get(pk = book_pk)
    if request.method =='GET':
        serializer = BookSerializer(book)
        return Response(serializer.data)


