from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Indra, Magar, Thapa, Category, Copyright
from django.core.mail import send_mail
from django.contrib import messages

from rest_framework import viewsets
from .serializers import MagarSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

import requests;

class MagarViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Magar.objects.all()
    serializer_class = MagarSerializer



# Create your views here.
def index(request):
    data={
        'indraData':Indra.objects.all(),
        'thapaData':Thapa.objects.all()
    }
    return render(request, 'index.html', data)

def contact(request):
    if request.method =='POST':
        
        email=request.POST['email']
       
        subject= request.POST['subject']
        message= request.POST['message']
        send_mail("Subject: "+ 'email', 'subject', 'message', ['magarindra927@gmail.com'], fail_silently=False)
        messages.success(request, 'Your message has been sent successfully')
        back=request.META.get('HTTP_REFERER')
        return redirect (back)
    else:
        return render(request, 'contact.html')

def magar_details(request, slug):
    magarData=Magar.objects.get(slug=slug)
    indra=magarData.indra.id
    related_magar=Magar.objects.filter(indra=indra).exclude(id=magarData.id)
    data={
       'magarData':Magar.objects.get(slug=slug),
       'related_magar':related_magar,
    }
    return render(request, 'magar_details.html', data)

def indra_magar(request, slug):
    data={
        'indData':Indra.objects.get(slug=slug)
    }
    return render(request, 'indra_magar.html', data)

def magar(request):
    if request.method=='POST':
        search=request.POST['search']
        find_data=Magar.objects.filter(title__icontains=search) | Magar.objects.filter(indra__name__icontains=search)
        paginator = Paginator(find_data, 3)  
        page= request.GET.get('page')
        find_data= paginator.get_page(page)
        data={
            'magarData':find_data,
            'title':'Search Result'
        }
        return render(request, 'magar.html', data)
    else:
        magar_data=Magar.objects.all()
        paginator = Paginator(magar_data, 3)  
        page= request.GET.get('page')
        magar_data= paginator.get_page(page)
        data={
            'magarData':magar_data,
            'title':'All News'
        }
        return render(request, 'magar.html', data)
    
def category(request, slug):
    data={
        'catData':Category.objects.get(slug=slug)
    }    
    return render(request, 'category.html', data)

def copyright(request, slug):
    data={
        'copData':Copyright.objects.get(slug=slug)
    }    
    return render(request, 'copyright.html', data)

def magar_api(request):
    url="https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d9ee7c42051e40ffa298114b256596fa"
    response=requests.get(url)
    data=response.json()
    data=data['articles']
    send_data={
        'magarData':data
    }
    return render(request, 'magar_api.html', send_data)