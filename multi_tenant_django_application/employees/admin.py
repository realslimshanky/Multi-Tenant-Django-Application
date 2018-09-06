from django.contrib import admin

from multi_tenant_django_application.employees.models import EmployeeModel, TeamModel


@admin.register(EmployeeModel)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamModel)
class TeamAdmin(admin.ModelAdmin):
    pass
