from django.urls import path
from . import views

# This calls the correct view for the movies app when called from the main urls.py
urlpatterns = [
	path('', views.home_page, name='home_page'),
	path('create/', views.create, name='create'),
]

