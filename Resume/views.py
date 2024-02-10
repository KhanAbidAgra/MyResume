from django.shortcuts import render, HttpResponse
from Resume.models import Contact
from datetime import datetime

# Create your views here.
def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        company = request.POST.get('company')
        city = request.POST.get('city')
        country = request.POST.get('country')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, mobileNumber=mobile, companyName=company,cityName=city, countryName=country,msgContent=message, msgDate=datetime.today())
        contact.save()
        
    return render(request,'contact.html') 