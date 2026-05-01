from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def home(request):
    return Response({
        "name": "Sakshyat Adhikari",
         "age":20, 
         "city":"Kathmandu"
         }


    )
