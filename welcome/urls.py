from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'welcome'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('ans/<int:question_id>/', views.answer_create, name='answer'),
    #이 url은 위 url에 정보를 주는 함수를 사용하기 위해 만든 것
    path('question/create/', views.question_create, name='question_create'),
    # 정수형식의 question_id인 1, 2가 welcome/1/이렇게 쓰이는 것
]
"""여기서 path('')에서 볼 수 있듯이 앞의 앱의 url을 쓰지 않아도 먼저 매핑된
것으로 처리된다"""
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)