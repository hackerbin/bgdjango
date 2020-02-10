from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.id, self.name)


class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.id, self.employee_name)

# Employee.objects.all().order_by('department','birthdate').distinct('department')

# select * from bgdjango.core_employee where birthdate in ( select MIN(birthdate) from bgdjango.core_employee group by department_id);
