from rest_framework import serializers,exceptions

from mainapp.models import Course


class CourseSerializer(serializers.ModelSerializer):
    class Meta :
        model = Course
        fields = (
            'id', 'name', 'description',
            'start_date',
        )

class RegistrationSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()


    def validate_password (self, value):
        if len(value) < 8:
            raise exceptions.ValidationError('Password is too short ')
        elif len(value) >  24:
            raise exceptions.ValidationError("Password is too long")
        return value


class AuthorizarionSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
