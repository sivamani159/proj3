from django.urls import path
from app1 import views

urlpatterns=[
    path('userinfo',views.userinfo,name='userinfo'),
    path('student2',views.student2,name='student2'),
]