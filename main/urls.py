
from  django.urls import path
from . import views

urlpatterns = [
            path('api/',views.number_classification, name="number_classification")
    ]

    