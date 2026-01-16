from django.contrib import admin
from django.urls import path, include
from escola.views import StudentViewSet, CourseViewSet, RegistrationViewSet, teste, teste_view
from rest_framework import routers
from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView,)

router = routers.DefaultRouter()
router.register('students', StudentViewSet, basename='Students')
router.register('courses', CourseViewSet, basename='Courses')
router.register('matriculas', RegistrationViewSet, basename='Registrations')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(router.urls)),
    path('teste/', teste, name='teste'),
    path('teste-view/', teste_view, name='teste_view'),
]
