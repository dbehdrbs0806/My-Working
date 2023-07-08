from django.http import HttpResponse
from django.shortcuts import render
from .forms import *

def index(request):
    return HttpResponse("안녕하세요 django에 오신것을 환영합니다.")

def write(request):
    if request.method =='POST':
        form = Form(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = Form()
         #forms.py파일에 있는 Form파일 함수
    return render(request, 'write.html', {'form':form}) 
#이 views파일에 write함수는 url파일에서 사용함
#render함수는 두 개의 매개변수 받음 

def list(request):
    articleList = Article.objects.all()
    return render(request, 'list.html', {'articleList':articleList})

