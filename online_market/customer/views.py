from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import CustomerSerializer
from .models import Customer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LoginSerializer

class CustomerViewset(ModelViewSet):
	serializer_class=CustomerSerializer
	queryset=Customer.objects.all()

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response({"message": "Login successful", "username": user.username}, status=status.HTTP_200_OK)