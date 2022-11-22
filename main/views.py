from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'pages/index.html',locals())

def about(request):
    return render(request,'pages/about.html',locals())

def services(request):
    return render(request,'pages/services.html',locals())

def blog(request):
    return render(request,'pages/blog.html',locals())

def shop(request):
    return render(request,'pages/shop.html',locals())

def galery(request):
    return render(request,'pages/galery.html',locals())

def contact(request):
    return render(request,'pages/contact.html',locals())
