from django import forms
from csecom.models import User, Locker

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['student_number', 'name', 'password']
        labels = {
            'student_number': '학번',
            'name': '이름',
            'password': '비밀번호',
        }

class LockerForm(forms.ModelForm):
    class Meta:
        model = Locker
        fields = ['student_number', 'locker_number', 'start_date']
        labels = {
            'student_number': '학번',
            'locker_number': '사물함 번호',
            'start_date': '사용 시작 날짜',
        }
