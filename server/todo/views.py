from django.db import connection
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect, render
from django.views import generic

from todo.models import ToDoItem, ToDoList


class IndexView(generic.ListView):
    template_name = "todo/index.html"

    def get_queryset(self) -> QuerySet[ToDoList]:
        return ToDoList.objects.all()


class DetailView(generic.DetailView):
    model = ToDoList
    template_name = "todo/list.html"

    def post(self, request: HttpRequest, pk: int):
        """
        Voeg een nieuw item toe aan een todo list.
        """

        # Haal het item op uit de opgestuurde form
        item = request.POST.get("item")

        # Haal de huidige todo list op
        todo_list = self.get_object()

        # Maak een nieuw item aan op de huidige todo list
        todo_item = ToDoItem(list=todo_list, item=item, completed=False)

        # Sla het nieuwe item op in de database
        todo_item.save()

        # Stuur de gebruiker door naar de bijgewerkte lijst
        return redirect(request.path_info, pk=pk)


def profile_view(request: HttpRequest, username: str) -> HttpResponse:
    with connection.cursor() as cursor:
        cursor.execute("SELECT name, description FROM todo_profile WHERE username = %s", [username])
        row = cursor.fetchone()

    if row:
        name = row[0]
        description = row[1]
    else:
        return HttpResponseNotFound()

    return render(request, "todo/profile.html", {"name": name, "description": description})
