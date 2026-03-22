from django.shortcuts import render
from user_auth.models import User
from user_auth.serializers import UserSerializer
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q
from rest_framework import status


# Create your views here.

class SignUp(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
             "message": "you are registered successfully",
             "data": {
             "username": serializer.data["username"],
             "email": serializer.data["email"]
                }
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class SignIn(APIView):
    def post(self,request):
        username= request.data.get("username")
        password=request.data.get('password')
        email=request.data.get('email')
        
        try:
            user = User.objects.get(Q(username=username) | Q(email=email))
        except User.DoesNotExist:
            return Response({"error": "User not found"})
            
        if not user.check_password(password):
            return Response("wrong password")
        refresh = RefreshToken.for_user(user)
        
        return Response({
    "user": {
        "id": user.id,
        "username": user.username,
    },
    "access": str(refresh.access_token),  
    "refresh": str(refresh),               
})