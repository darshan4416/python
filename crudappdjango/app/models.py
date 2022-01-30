from django.db import models
import uuid

class Department(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)
    dept_name = models.CharField(max_length=40,null=False)

    def __str__(self):
        return self.dept_name

class Employee(models.Model):
    name = models.CharField(max_length=40,blank=False)
    manager_name = models.CharField(max_length=40,blank=False)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE,null=True, blank=True)

    def __str__(self):
        return self.name





