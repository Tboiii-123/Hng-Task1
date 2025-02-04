
from  django.urls import path
from . import views

urlpatterns = [
            path('api/classify-number',views.number_classification, name="number_classification")
    ]

    
