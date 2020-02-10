from django.contrib import admin

from core.models import Department, Employee


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_name', 'birthdate', 'department')


admin.site.register(Department, DepartmentAdmin)
admin.site.register(Employee, EmployeeAdmin)
