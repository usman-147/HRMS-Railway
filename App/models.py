from django.db import models

class Authority(models.Model):
    name         = models.CharField(max_length=100)
    email        = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100)
    location     = models.CharField(max_length=100)
    password     = models.CharField(max_length=128)

class HRUser(models.Model):
    name     = models.CharField(max_length=100)
    email    = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
    
class HR(models.Model):
    joined_data = models.CharField(max_length = 200, null = True)
    department = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return self.name

class Instructor(models.Model):
    instructor_name = models.CharField(max_length = 200, null = True, blank = True)
    experience = models.IntegerField()
    salary = models.IntegerField()
    status =  models.CharField(max_length = 200, null = True, blank = True)
    experience = models.IntegerField()

    def __str__(self):
        return self.instructor_name
    
#^^^^^^^^^^^^^^^^^^^^^^^^^^^Future Iterations^^^^^^^^^^^^^^^^^^^^^^^^^^^^

class Department(models.Model):
    department_name = models.CharField(max_length = 200, null = True, blank = True)
    d_no = models.IntegerField()

    def __str__(self):
        return self.department_name
    
class Activities(models.Model):
    activity_name = models.CharField(max_length = 200, null = True, blank = True)
    activity_duration = models.IntegerField()

    def __str__(self):
        return self.activity_name

class Capital(models.Model):
    bonus = models.IntegerField()

    def __str__(self):
        return str(self.bonus)
