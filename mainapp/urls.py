from django.urls import path 
from rest_framework.routers import DefaultRouter as DR
from mainapp.views import (CourseView,)

router = DR()
router.register('course',CourseView,basename='course')


urlpatterns =[]

urlpatterns += router.urls
