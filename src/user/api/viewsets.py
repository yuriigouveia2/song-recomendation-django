from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.auth.models import User
from http import HTTPMethod

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
    
    @action(detail=True, methods=[HTTPMethod.DELETE])
    def destroy(self, request, *args, **kwargs):
        print('teste    ')
        return super().destroy(request, *args, **kwargs)
    
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()