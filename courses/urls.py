from django.urls import path,re_path
from .views import CourseC, CourseRUD

urlpatterns = [
    path('courses/', CourseC.as_view(), name='courseC'),
    path('courses/<path:pk>/', CourseRUD.as_view(), name='courseRUD'),
]