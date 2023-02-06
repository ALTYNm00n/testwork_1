from rest_framework.viewsets import ModelViewSet
from rest_framework import filters 

from django_filters.rest_framework import DjangoFilterBackend

from mainapp.serializers import CourseSerializer
from mainapp.models import Course

from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework import permissions
from rest_framework.decorators import action


class  CourseView(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class=CourseSerializer
    filter_backends=(DjangoFilterBackend,)
    filter_fields=(
        'start_course',)
    @action(methods=['post',], detail=True,\
        serializer_class=CourseSerializer,permission_classes=\
            (permissions.IsAuthenticatedOrReadOnly))
    def add_course (self , request, *args, **kwargs):
        courses= self.get_object()
        user= request.user
        serializer=CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data=serializer.validated_data
        course=Course.objects.create(
            courses=courses,
            name= data.get('name'),
            start_date= data.get('start_date'),
            description= data.get('description'),
            user= user,
        )
        return Response(CourseSerializer(course).data)

    
            

    




