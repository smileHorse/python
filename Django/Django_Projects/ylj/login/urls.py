from django.urls import path, include
import login.views

urlpatterns = [
    path('', login.views.login),
]