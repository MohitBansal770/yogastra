from django.http import *
from django.shortcuts import *
from django.urls import reverse

from ..forms import Subscribe
from ..PaymentGateway.gateway import completePayment

def get_details(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Subscribe(request.POST)
        # check whether it's valid:
        if form.is_valid():
            if(completePayment()):
                data=form.cleaned_data

                return success(request,form.cleaned_data['first_name'],'Jan','2023')
            else:
                return failed(request,first_name=form.cleaned_data['first_name'],link=reverse('home'))
    # if a GET (or any other method) we'll create a blank form
    else:
        form = Subscribe()
    return render(request, 'subscribe.html', {'form': form})

def failed(request,first_name,link):
    return render(request,'failed.html',{'first_name':first_name,'link':link})

def success(request,first_name,month,year):
    return render(request,'success.html',{'first_name':'Samarth','month':month,'year':year})
