from rest_framework import serializers

from multi_tenant_django_application.tenants.models import CompanyModel


class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = CompanyModel
        fields = ['id', 'created_at', 'modified_at', 'name', 'admin', 'tenant_aware_suffix']
