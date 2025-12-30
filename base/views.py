from django.shortcuts import render,HttpResponse,redirect
from base.models import category,Article
from base.froms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    context={
        # 'categories':category.objects.all(),
        'articles':Article.objects.filter(status='published',is_trending=True).order_by('-updated_at'),
        'not_trending':Article.objects.filter(status='published',is_trending=False)
    }

    return render(request,'home.html',context)

def category_articles(request,cat):
    cate=category.objects.get(category_name=cat)
    context={
        'articles':Article.objects.filter(category=cate.id),
        'category':cate
    }
    return render(request,'category.html',context)

@login_required(login_url='login')
def single_article(request,slug):
    context={
        'article':Article.objects.get(slug=slug)
    }
    
    return render(request,'single_article.html',context)

def register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'register.html',{'form':form})
    forms=RegisterForm()
    return render(request,'register.html',{'form':forms})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request,'login.html',{'form':form})
        
    login=AuthenticationForm()
    return render(request,'login.html',{'login':login})

def logout(request):
    auth.logout(request)
    return redirect('home')