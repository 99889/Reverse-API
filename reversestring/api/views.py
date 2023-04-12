from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import views
from rest_framework.response import Response
from .serializers import StringSerializer


class ReverseStringView(views.APIView):
    def post(self, request, format=None):
        serializer = StringSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_string = serializer.validated_data['input_string']
        output_string = input_string[::-1]
        return Response({'output_string': output_string})
