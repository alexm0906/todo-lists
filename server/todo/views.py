from django.db import connection
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.views import generic

from todo.models import ToDoList


class IndexView(generic.ListView):
    template_name = "todo/index.html"

    def get_queryset(self) -> QuerySet[ToDoList]:
        return ToDoList.objects.all()


class DetailView(generic.DetailView):
    model = ToDoList
    template_name = "todo/list.html"


def profile_view(request: HttpRequest, username: str) -> HttpResponse:
    with connection.cursor() as cursor:
        # NOTE: Explicitly vulnerable to SQL Injection for demo purposes
        cursor.execute(f"SELECT name, description FROM todo_profile WHERE username = '{username}'")
        row = cursor.fetchone()

    if row:
        name = row[0]
        description = row[1]
    else:
        return HttpResponseNotFound()

    return HttpResponse(
        f"""
        <!DOCTYPE html>
        <html>
            <head>
                <title>To-Do lists</title>

                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-LN+7fdVzj6u52u30Kp6M/trliBMCMKTyK833zpbD+pXdCLuTusPj697FH4R/5mcr" crossorigin="anonymous">
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.7/dist/js/bootstrap.bundle.min.js" integrity="sha384-ndDqU0Gzau9qJ1lfW4pNLlhNTkCfHzAVBReH9diLvGRem5+R9g2FzA8ZGN954O5Q" crossorigin="anonymous"></script>
            </head>
            <body>
                <div class="container">
                    <div class="row my-5">
                        <div class="col"><h1>Profile</h1></div>
                    </div>

                    <div class="row">
                        <div class="col">
                            <p>Name</p>
                        </div>
                        <div class="col">
                            <p>{name}</p>
                        </div>
                    </div>

                    <div class="row">
                        <div class="col">
                            <p>Description</p>
                        </div>
                        <div class="col">
                            <p>{description}</p>
                        </div>
                    </div>
                </div>
            </body>
        </html>
        """
    )
