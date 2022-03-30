from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import datetime as dt
import time
from Task import settings
from django.core.mail import send_mail
from .models import Borrower, Stateloan
from .serializers import BorrowerSerializer, StateloanSerializer

@csrf_exempt
def borrower(request,id=1):
    if request.method=="GET":
        items = Borrower.objects.all()
        item_serializer = BorrowerSerializer(items, many =True)
        return JsonResponse(item_serializer.data, safe =False)

def stateloan(request, id =1):
    if request.method == "GET":
        data = Stateloan.objects.all()
        data_serializer = StateloanSerializer(data, many =True)
        return JsonResponse(data_serializer.data, safe = False)


def mail_send(request,id=1):
    if request.method == 'GET':

        send_time = dt.datetime(2022,3,30,16,48,0)
        print(send_time.timestamp())
        print(time.time())
        x= time.sleep(send_time.timestamp() - time.time())
        print(x)

        send_mail(subject='New Email',
        message =f'NEW EMAIL FROM "KhajuriBazaar".\n\nHello Nilabh,\nGood Morning from KhajuriBazaar',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list = ['jacky.jones786@gmail.com'],
        fail_silently=False)

        return HttpResponse('ok')