from django.db import models

# Create your models here.

class Department(models.Model):
    dept_no=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100)
    loc=models.CharField(max_length=100)
    
    def __str__(self):
        return self.dname
    
class Worker(models.Model):
    
    emp_no=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100,unique=True)
    job=models.CharField(max_length=100)
    mgr=models.IntegerField()
    hiredate=models.DateField()
    sal=models.IntegerField()
    comm=models.IntegerField(null=True)
    dept_no=models.ForeignKey(Department,on_delete=models.CASCADE)
    
    
    def  __str__(self):
        return self.job

    

