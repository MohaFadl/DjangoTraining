from django.urls import path
from myapp import views
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path('home/', views.test)
] + debug_toolbar_urls()

