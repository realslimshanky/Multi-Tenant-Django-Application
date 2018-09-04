from rest_framework import viewsets

from multi_tenant_django_application.tenants.utils import tenant_from_request
from multi_tenant_django_application.employees.models import EmployeeModel
from multi_tenant_django_application.employees.serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        tenant = tenant_from_request(self.request)
        return super().get_queryset().filter(company=tenant)
