from django.urls import path,re_path
from .views import CourseView, CourseInstanceView

urlpatterns = [
    path('courses/', CourseView.as_view(), name='courseView'),
    path('courses/<path:pk>/', CourseInstanceView.as_view(), name='courseInstanceView'),
]