from django.db.models.query import QuerySet
from django.views import generic

from todo.models import ToDoList


class IndexView(generic.ListView):
    template_name = "todo/index.html.jinja"

    def get_queryset(self) -> QuerySet[ToDoList]:
        return ToDoList.objects.all()


class DetailView(generic.DetailView):
    model = ToDoList
    template_name = "todo/list.html.jinja"

