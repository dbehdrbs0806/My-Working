from django.urls import path
from . import views

app_name = 'welcome'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    # 정수형식의 question_id인 1, 2가 welcome/1/이렇게 쓰이는 것
]
"""여기서 path('')에서 볼 수 있듯이 앞의 앱의 url을 쓰지 않아도 먼저 매핑된
것으로 처리된다"""