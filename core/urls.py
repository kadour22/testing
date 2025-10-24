from django.urls import path
from . import views

urlpatterns = [
    path("" , views.index_api_view.as_view())
]