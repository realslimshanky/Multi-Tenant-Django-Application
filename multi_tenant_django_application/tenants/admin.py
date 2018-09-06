from django.contrib import admin

from multi_tenant_django_application.tenants.models import CompanyModel


@admin.register(CompanyModel)
class CompanyAdmin(admin.ModelAdmin):
    pass
