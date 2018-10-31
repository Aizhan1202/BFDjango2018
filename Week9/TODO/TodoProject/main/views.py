from django.shortcuts import render
from django.http import HttpResponse
from .models import User, Owner, Task
from datetime import datetime, timedelta
from django.views import View


class Index1(View):
    def get(self, request):
        cur_day = datetime.today()
        todo_list = [{
            'title': "Task {}".format(i),
            'created': cur_day.strftime("%d/%m/%y"),
            'due_on': (cur_day + timedelta(days=3)).strftime("%d/%m/%y"),
            'owner': "admin",
            'mark': 'Done'
        }
             for i in range(1, 5)
        ]
        context = {
             'todo_list': todo_list,
        }
        return render(request, 'todo_list.html', context)

class Index2(View):
    def index2(self, request):
        cur_day = datetime.today ()
        task = {
            'title': "Task {}".format (2),
            'created': cur_day.strftime ("%d/%m/%y"),
            'due_on': (cur_day + timedelta (days=3)).strftime ("%d/%m/%y"),
            'owner': "admin",
            'mark': 'Undone'
        }
        context = {
            'task': task
        }
        return render (request, 'completed_todo_list.html', context)
