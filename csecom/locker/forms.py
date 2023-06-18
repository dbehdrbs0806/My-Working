from django import forms
from .models import Lockers

class LockerForm(forms.ModelForm):
    class Meta:
        model = Lockers
        fields = ['student_number', 'locker_number', 'start_date']
        labels = {
            'student_number': '학번',
            'locker_number': '사물함 번호',
            'start_date': '사용 시작 날짜',
        }
