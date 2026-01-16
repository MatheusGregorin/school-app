from rest_framework import serializers
from .models import Estudent, Course, Registration
from escola.validator import name_invalid

# Simple serializers to avoid circular references
class StudentSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudent
        fields = ['id', 'name', 'email']

class CourseSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']

class RegistrationSimpleSerializer(serializers.ModelSerializer):

    student = StudentSimpleSerializer(read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'student', 'created_at']

# Full serializers with nested relationships
class StudentSerializer(serializers.ModelSerializer):

    registrations = RegistrationSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Estudent
        fields = ['id', 'name', 'email', 'document', 'birth', 'phone', 'registrations']

    def validate(self, dados):
        if not name_invalid(dados['name']):
            raise serializers.ValidationError("Name invalid.")
        return dados

class CourseSerializer(serializers.ModelSerializer):

    registrations = RegistrationSimpleSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'description', 'duration', 'price', 'nivel', 'registrations']

class RegistrationSerializer(serializers.ModelSerializer):

    student = StudentSimpleSerializer(read_only=True)
    course = CourseSimpleSerializer(read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'student', 'course', 'created_at']