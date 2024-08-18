from django.urls import path
from . import views

urlpatterns=[
    path("<str:operation>",views.Operation),
]
    
