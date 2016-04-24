from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=60)
    abbreviation = models.CharField(max_length=4)

class Course(models.Model):
    identifier = models.CharField(max_length=8)
    department = models.ForeignKey(Department)
    name = models.CharField(max_length=96)
    credit = models.CharField(max_length=48)
    description = models.TextField()
    
    def __str__(self):
        return self.identifier

    def __cmp__(self, other):
        this_ident = str(self.identifier)
        othr_ident = str(other.identifier)
        return this_ident < othr_ident

    def get_ident(self):
        return self.identifier

    def get_credit(self):
        try:
            return int(self.credit[8])
        except ValueError:
            return 0
