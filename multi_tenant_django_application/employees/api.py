from rest_framework import viewsets, mixins

from multi_tenant_django_application.base import response
from multi_tenant_django_application.tenants.utils import tenant_from_request
from multi_tenant_django_application.employees.models import EmployeeModel
from multi_tenant_django_application.employees.serializers import EmployeeSerializer
from multi_tenant_django_application.employees.permissions import CompanyAdminOrSelf


class EmployeeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin, mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (CompanyAdminOrSelf, )

    def list(self, request, *args, **kwargs):
        if tenant_from_request(self.request):
            return super().list(request, *args, **kwargs)
        return response.NotFound()

    def create(self, request, *args, **kwargs):
        company = tenant_from_request(request)
        if company:
            existing_employee = self.get_queryset().filter(id=request.data['id']).first()
            if existing_employee:
                return response.BadRequest({"error_message": "Already an employee in one of the companies"})
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(data=request.data, context={'company': company})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return response.Created(serializer.data)
        return response.NotFound()

    def retrieve(self, request, *args, **kwargs):
        if tenant_from_request(self.request):
            return super().retrieve(request, *args, **kwargs)
        return response.NotFound()

    def destroy(self, request, *args, **kwargs):
        if tenant_from_request(self.request):
            return super().destroy(request, *args, **kwargs)
        return response.NotFound()

    def get_queryset(self):
        company = tenant_from_request(self.request)
        return super().get_queryset().filter(company=company)
