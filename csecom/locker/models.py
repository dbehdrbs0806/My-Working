from django.contrib.auth.models import User
from django.db import models

# class Student(models.Model):
#     '''유저 정의 모델
#     student_number: 학번, 외래키
#     name: 이름
#     password: 비밀번호
#     '''
#     student_number = models.ForeignKey(User, on_delete=models.CASCADE)
#     name = models.CharField(max_length=10)
#     password = models.CharField(max_length=20)

# class Locker(models.Model):
#     '''사물함 정의 모델
#     student_number: 학번, 외래키
#     locker_number: 사물함 번호
#     start_date: 사용 시작 날짜
#     '''
#     student_number = models.ForeignKey(User, on_delete=models.CASCADE)
#     locker_number = models.IntegerField()
#     start_date = models.DateTimeField()
