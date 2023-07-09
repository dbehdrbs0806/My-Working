from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("안녕하세요 django에 오신것을 환영합니다.")
#HttpResponse함수는 화면에 텍스트, html을 출력하는 함수
