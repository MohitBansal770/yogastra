from django.http import HttpResponse

def login(request):
    return HttpResponse(request.POST['email']+request.POST['secret'])


