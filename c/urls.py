# todo/api/urls.py : API urls.py
from django.conf.urls import url
from django.urls import path, include
from .views import (

    TodoDetailApiView
)

urlpatterns = [
   # path('', TodoListApiView.as_view()),
    path('<int:c_id>/', TodoDetailApiView.as_view()),
]