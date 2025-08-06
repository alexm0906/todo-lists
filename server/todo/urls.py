from django.urls import path

from todo import views

app_name = "todo"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("profile/<str:username>", views.profile_view, name="profile"),
]
