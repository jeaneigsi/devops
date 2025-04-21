from . import views
from django.urls import path


# This is the URL configuration for the 'moduler' app.
urlpatterns = [
 path('', views.my_model_list, name='my_model_list'),
]
