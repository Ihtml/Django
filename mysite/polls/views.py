from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("HEllo, wrold, I love python!(from polls views)")
