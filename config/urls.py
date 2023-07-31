"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views #이 부분은 현 디렉토리에 viewpy파일을 import하게 한다 의미

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', include('welcome.urls')),  
    path('write/', views.write, name ='write'),
    path('list/', views.list, name='list'),  
]
"""include를 사용하면 welcome의 서브 url인 welcome/hi, welcome/bye같은
    welcome/시작 url 추가 시 urls.py파일 전체를 수정할 필요가 없다"""

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)