from audioop import reverse
from django.shortcuts import render
from django.http import HttpResponse
import requests
from urllib3 import request
from .models import News
# from .forms import NewsForm
from .forms import NewsModelForm
from django.contrib.auth.decorators import login_required
from django.http import Http404 , HttpResponseRedirect
from django.urls import reverse


def index (request):
    obj=News.objects.all()
    print(request.method)
    print(obj)
    
    return render(request,'news/index.html',{'name':obj})

def detail_viev(request,bwp):
    obj = News.objects.get(id=bwp)
    print(request.POST)   
    print(request.GET)
    return render(request ,'news/detail.html', {'detailnews':obj})


@login_required
def create_view(request):
    form = NewsModelForm(request.POST or None)
    if request.method =='POST' :
        if form.is_valid():
            obj=form.save(commit=False)
            obj.author=request.user
            obj.save() 
        print(form.is_valid())
    return render(request, 'news/forms.html',{'form' : form})
            # data=form.cleaned_data
            # News.objects.create(**data)
            
@login_required
def edit_view(request, pk):
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404
    if request.method == "POST":
        form= NewsModelForm(request.POST ,instance=obj )
        if form.is_valid():
            edited_obj = form.save(commit=False)
            edited_obj.save()
    else:
        form =NewsModelForm(instance=obj)
        
        
    return render(request , 'news/edit_news_form.html',{'single_object':obj, 'form':form})
@login_required
def delete_view(request,pk):
    try:
        obj = News.objects.get(id=pk)
    except News.DoesNotExist:
        raise Http404
    obj.delete()
    return HttpResponseRedirect(reverse('index'))
        















