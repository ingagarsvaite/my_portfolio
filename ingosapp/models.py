from django.db import models

class ToDoList(models.Model):
    pavadinimas = models.CharField(max_length=200)

    def __str__(self):
        return self.pavadinimas

class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    tekstas = models.CharField(max_length=300)
    atlikta = models.BooleanField()

    def __str__(self):
        return self.tekstas
