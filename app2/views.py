
from django.http import HttpResponse

def about(request):
    return HttpResponse("Hello from App2 About Page!")
