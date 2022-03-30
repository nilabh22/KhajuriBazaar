from django.urls import path
from django.urls import re_path as url
from api import views

urlpatterns = [
    path('api/', views.borrower),
    path('stateloan/', views.stateloan),
    path('sendEmail/', views.mail_send)
]
