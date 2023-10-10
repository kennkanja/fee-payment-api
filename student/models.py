from django.db import models

# Create your models here.
class Home(models.Model):
    name = models.CharField(max_length=100)
    
    def str__str__(self):
        return  self.name
    
class Student(models.Model):
    reg_no = models.CharField(max_length = 100)
    name = models.CharField(max_length = 100)
    course = models.CharField(max_length = 50)
    year  =  models.IntegerField()
    fee = models.IntegerField()
    time = models.DateField()
       

    def __str__(self):
        return self.name

class Pay(models.Model):
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING)  
    amount = models.IntegerField()
    time  = models.DateField()

    def __str__(self):
        return str(self.student)


