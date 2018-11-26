from django.shortcuts import render
from .models import UserMessage
# Create your views here.


def getform(request):
    # queryset类型，支持for循环
    # all_message = UserMessage.objects.filter(name='Foo', address='Beijing')
    # all_message.delete()
    # for message in all_message:
    #     print(message.name)
    #     message.delete()
    name = request.POST.get('name', '')
    message = request.POST.get('message', '')
    address = request.POST.get('address', '')
    email = request.POST.get('email', '')
    user_message = UserMessage()
    user_message.name = name
    user_message.message = message
    user_message.address = address
    user_message.email = email
    user_message.object_id = 'helloword2'

    user_message.save()
    return render(request, 'message/message_form.html')
