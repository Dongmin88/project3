from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.http import HttpResponse
from django.shortcuts import render

# Main page view
def main_page(request):
    return render(request, 'main_page.html')

# Login page view
def login_page(request):
    return render(request, 'login_page.html')

# Feature 1 page view
def feature_page1(request):
    return render(request, 'feature_page1.html')

# Feature 2 page view
def feature_page2(request):
    return render(request, 'feature_page2.html')


@api_view(['GET', 'POST', 'DELETE'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data  # 요청으로 들어온 데이터
        return Response({"message": f"Received data: {data}"}, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        return Response({"message": "Resource deleted."}, status=status.HTTP_204_NO_CONTENT)