from escola.models import Estudent, Course, Registration
from escola.serializer import StudentSerializer, CourseSerializer, RegistrationSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.http import JsonResponse as HttpResponseJSON
import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend

class StudentViewSet(viewsets.ModelViewSet):
    # Permissions
    permission_classes = [IsAuthenticated]
    queryset = Estudent.objects.all()
    serializer_class = StudentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    order_fields = ['name', 'email']

class CourseViewSet(viewsets.ModelViewSet):
    # Permissions
    permission_classes = [IsAuthenticated]
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class RegistrationViewSet(viewsets.ModelViewSet):
    # Permissions
    permission_classes = [IsAuthenticated]
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer

def teste(request):
    try:
        print("Teste function called")

        print("Processing request...")
        print(json.loads(request.body))

        print("Model database")
        print(list(Estudent.objects.all().values()))

        return HttpResponseJSON({
            "message": "Teste function response"
        }, status=200)
    
    except Exception as e:
        return HttpResponseJSON({
            "error": str(e)
        }, status=500)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def teste_view(request):
    try:
        print("Teste function called with view")

        print("Processing request... with view")
        print(request.data)

        print("Model database with view")
        print(list(Estudent.objects.all().values()))

        return HttpResponseJSON({
            "message": "Teste function response with view"
        }, status=200)
    
    except Exception as e:
        return HttpResponseJSON({
            "error": str(e)
        }, status=500)