from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET', 'POST'])
def sample_api(request):
    if request.method == 'POST':
        data = request.data
        return Response({"message": "Data received", "data": data})
    return Response({"message": "Hello from API!"})
