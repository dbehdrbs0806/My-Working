from django.http import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.utils import timezone
from .forms import *

def fprint(request):
    return HttpResponse("안녕하세요 django에 오신것을 환영합니다.")
#HttpResponse함수는 화면에 텍스트, html을 출력하는 함수

def index(request):
    question_list = Question.objects.order_by('-create_date')
    context = {'question_list':question_list}
    return render(request, 'question_list.html', context)

def detail(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {'question': question} #<= 이 코드는 없어도 된다
    return render(request, 'question_detail.html', {'question': question})
# urls.py의 저장된 question_id가 매개변수로 들어가게된다

def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('welcome:detail', question_id=question.id)
    else:
        return HttpResponseNotAllowed('Only POST is possible.')
    context = {'question': question, 'form': form}
    return render(request, 'question_detail.html', context)

def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            try:
                question.image = request.FILES['image']
            except KeyError:
                question.image = None
            question.save()
            return redirect('welcome:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'question_form.html', context)