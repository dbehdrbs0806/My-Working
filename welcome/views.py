from django.http import *
from django.shortcuts import render
from .models import *

def fprint(request):
    return HttpResponse("안녕하세요 django에 오신것을 환영합니다.")
#HttpResponse함수는 화면에 텍스트, html을 출력하는 함수

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question}
    return render(request, 'question_detail.html', {'question': question})

# 저장된 question_id가 매개변수로 들어가게된다