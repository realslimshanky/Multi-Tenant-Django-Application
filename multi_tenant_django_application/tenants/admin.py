from django.contrib import admin

from multi_tenant_django_application.employees.models import EmployeeModel


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    pass
