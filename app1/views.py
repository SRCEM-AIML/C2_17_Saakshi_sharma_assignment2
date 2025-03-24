
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from App1 Home!")
