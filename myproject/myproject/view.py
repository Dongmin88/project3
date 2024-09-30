from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

@api_view(['GET', 'POST', 'DELETE'])
def hello_world(request):
    if request.method == 'GET':
        return Response({"message": "Hello, world!"}, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = request.data  # 요청으로 들어온 데이터
        return Response({"message": f"Received data: {data}"}, status=status.HTTP_201_CREATED)
    
    elif request.method == 'DELETE':
        return Response({"message": "Resource deleted."}, status=status.HTTP_204_NO_CONTENT)