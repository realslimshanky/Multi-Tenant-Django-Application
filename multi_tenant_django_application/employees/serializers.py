from rest_framework import serializers

from multi_tenant_django_application.employees.models import EmployeeModel, TeamModel


class EmployeeSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name', read_only=True)
    first_name = serializers.CharField(source='id.first_name', read_only=True)
    last_name = serializers.CharField(source='id.last_name', read_only=True)
    email = serializers.CharField(source='id.email', read_only=True)

    def create(self, validated_data):
        validated_data['company'] = self.context['company']
        return EmployeeModel.objects.create(**validated_data)

    class Meta:
        model = EmployeeModel
        fields = ['id', 'created_at', 'modified_at', 'first_name', 'last_name', 'email', 'company']
        read_only_fields = ['created_at', 'modified_at']


class TeamSerializer(serializers.ModelSerializer):
    company = serializers.CharField(source='company.name', read_only=True)

    def create(self, validated_data):
        validated_data['company'] = self.context['company']
        return TeamModel.objects.create(**validated_data)

    class Meta:
        model = TeamModel
        fields = ['id', 'created_at', 'modified_at', 'name', 'description', 'employees', 'company']
        read_only_fields = ['created_at', 'modified_at', 'employees']


class TeamEmployeesSerializer(TeamSerializer):
    employees = EmployeeSerializer(many=True, required=False)

    class Meta(TeamSerializer.Meta):
        fields = ['id', 'name', 'employees']
        read_only_fields = ['created_at', 'modified_at' 'name', 'description']
