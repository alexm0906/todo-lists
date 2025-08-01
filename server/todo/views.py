from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render

from todo.models import ToDoList


def index(request: HttpRequest) -> HttpResponse:
    items = ToDoList.objects.all()

    return render(request, "todo/index.html.jinja", {"items": items})


def detail(request: HttpRequest, list_id: int) -> HttpResponse:
    todo_list = get_object_or_404(ToDoList, pk=list_id)

    return render(request, "todo/list.html.jinja", {"todo_list": todo_list})
