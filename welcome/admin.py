from django.contrib import admin
from .models import *

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)

"""admin페이지에서 확인할 수 있는 부분
파라미터부분은 admin.ModelAdmin이 가독성이 좋으며
search_fields속성에 subject를 추가한다

admin.site.register(Question, 클래스 이름) 이렇게 해주면 검색하는
기능이 가능한 admin이된다
"""
