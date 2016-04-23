from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=4)

class Course(models.Model):
    identifier = models.CharField(max_length=8)
    department = models.ForeignKey(Department)
    name = models.CharField(max_length=128)
    credit = models.IntegerField()
    description = models.TextField()
    
    def __str__(self):
        return self.name