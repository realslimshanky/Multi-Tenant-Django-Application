from rest_framework import serializers

from multi_tenant_django_application.employees.models import EmployeeModel


class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = EmployeeModel
        fields = ['id', 'created_at', 'modified_at', 'name', 'company']
