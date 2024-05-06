from django.http import HttpResponse

def hello_view(request):
    return HttpResponse("this is django based api")