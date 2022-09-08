from django.contrib import admin
from app1.models import *

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','course','contact']

@admin.register(Userinfo)
class UserinfoAdmin(admin.ModelAdmin):
    list_display=['name','email','gender','contact']

@admin.register(Student1)
class Student1Admin(admin.ModelAdmin):
    list_display=['id','sname','course','fee','sesstime']

@admin.register(Student2)
class Student2Admin(admin.ModelAdmin):
    list_display=['id','name','email','fee']