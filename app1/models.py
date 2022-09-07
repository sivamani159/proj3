import email
from django.db import models

# Create your models here.

courses=(
    ("1","python"),
    ("2","javascript"),
    ("3","django"),
    ("4","sql"),
    ("5","mangodb")
)
class Student(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    course=models.CharField(max_length=20,choices=courses,default="1")
    contact=models.IntegerField()

GENDER=(
    ("1","male"),
    ("2","female"),
    ("3","others")
)
class Userinfo(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    gender=models.CharField(max_length=20,choices=GENDER,default='1')
    contact=models.PositiveIntegerField()

class Student1(models.Model):
    sname=models.CharField(max_length=30)
    course=models.CharField(max_length=20)
    fee=models.SmallIntegerField(default='200')
    sesstime=models.TimeField(auto_now_add=True)

class Student2(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)

    
