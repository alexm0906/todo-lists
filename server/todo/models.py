from django.db import models


class ToDoList(models.Model):
    name = models.CharField(max_length=256)
    items: models.Manager["ToDoItem"]

    def incomplete_count(self):
        return self.items.filter(completed=False).count()

    def __str__(self) -> str:
        return self.name


class ToDoItem(models.Model):
    list = models.ForeignKey(ToDoList, on_delete=models.CASCADE, related_name="items")
    item = models.CharField(max_length=256)
    completed = models.BooleanField()

    def __str__(self) -> str:
        return self.item


class Profile(models.Model):
    username = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    description = models.TextField()
