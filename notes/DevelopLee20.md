# 정리

- models.py는 db 정의해준다.
- 어드민 계정 admin - ckadltmf

```python
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
```
