from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
]
"""여기서 path('')에서 볼 수 있듯이 앞의 앱의 url을 쓰지 않아도 먼저 매핑된
것으로 처리된다"""