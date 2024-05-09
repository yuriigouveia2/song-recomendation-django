from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import action, api_view
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from user.api import serializers
from user import models

class UserInfoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserInfoSerializer
    queryset = models.UserInfo.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)
    

class UserRegistrationViewSet(generics.CreateAPIView):
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginViewSet(APIView):
    
    @api_view(['POST'])
    def auth(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)

    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.CustomUser.objects.all()