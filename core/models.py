from django.db import models
from django.db.models.expressions import RawSQL


class Department(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return "{} {}".format(self.id, self.name)

    class Meta:
        db_table = 'departments'


class Employee(models.Model):
    employee_name = models.CharField(max_length=255)
    birthdate = models.DateField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.id, self.employee_name)

    class Meta:
        db_table = 'employees'

    @staticmethod
    def get_oldest_employee_from_department():
        """
        if db backend is postgres
        # return Employee.objects.all().order_by('department','birthdate').distinct('department')
        :return:
        """
        employees = Employee.objects.raw(
            "SELECT * FROM employees where birthdate in ( SELECT MIN(birthdate) from employees GROUP BY department_id)")
        for employee in employees:
            print("name={}, birthdate={}, department={}".format(employee.employee_name, employee.birthdate, employee.department.name))
        return list(employees)

