from django.urls import path
from . import views 

urlpatterns = [
    path('', views.register, name="register"),
    path('employer/', views.registerEmployer, name="register-employer")
]