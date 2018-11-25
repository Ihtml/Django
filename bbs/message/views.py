from django.shortcuts import render
from .models import UserMessage
# Create your views here.


def getform(request):
    # queryset类型，支持for循环
    all_message = UserMessage.objects.all()
    for message in all_message:
        print(message)
    return render(request, 'message/message_form.html')
