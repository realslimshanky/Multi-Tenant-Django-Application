from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from multi_tenant_django_application.base import response
from multi_tenant_django_application.tenants.utils import tenant_from_request
from multi_tenant_django_application.employees.utils import team_from_request
from multi_tenant_django_application.employees.models import EmployeeModel, TeamModel
from multi_tenant_django_application.employees.serializers import (
    EmployeeSerializer, TeamSerializer, TeamEmployeesSerializer)
from multi_tenant_django_application.employees.permissions import IsCompanyAdminOrSelf, IsCompanyAdmin


class EmployeeViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin, mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = (IsCompanyAdminOrSelf, )

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


class TeamsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin, mixins.DestroyModelMixin,
                   mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = TeamModel.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsCompanyAdmin, )

    def list(self, request, *args, **kwargs):
        if tenant_from_request(self.request):
            return super().list(request, *args, **kwargs)
        return response.NotFound()

    def create(self, request, *args, **kwargs):
        company = tenant_from_request(request)
        if company:
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

    def update(self, request, *args, **kwargs):
        if tenant_from_request(self.request):
            return super().update(request, *args, **kwargs)
        return response.NotFound()

    def partial_update(self, request, *args, **kwargs):
        if tenant_from_request(self.request):
            return super().partial_update(request, *args, **kwargs)
        return response.NotFound()

    def get_queryset(self):
        company = tenant_from_request(self.request)
        return super().get_queryset().filter(company=company)


class TeamEmployeesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = TeamModel.objects.all()
    serializer_class = TeamEmployeesSerializer

    def list(self, request, *args, **kwargs):
        if tenant_from_request(self.request) and team_from_request(self.request):
            team = self.get_queryset().first()
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(team)
            return response.Ok(serializer.data)
        return response.NotFound()

    @action(methods=['PATCH'], detail=False)
    def add_employee(self, request):
        company = tenant_from_request(self.request)
        team = team_from_request(self.request)
        if not team or not company:
            return response.NotFound()

        employee = EmployeeModel.objects.filter(company=company).filter(id=request.data['employee']).first()
        if employee:
            queryset = self.get_queryset().first()
            queryset.employees.add(employee)
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(queryset)
            return response.Ok(serializer.data)

        return response.BadRequest({'error_message': 'Employee not found'})

    @action(methods=['PATCH'], detail=False)
    def remove_employee(self, request):
        company = tenant_from_request(self.request)
        team = team_from_request(self.request)
        if not team or not company:
            return response.NotFound()

        employee = EmployeeModel.objects.filter(company=company).filter(id=request.data['employee']).first()
        if employee:
            queryset = self.get_queryset().first()
            queryset.employees.remove(employee)
            serializer_class = self.get_serializer_class()
            serializer = serializer_class(queryset)
            return response.Ok(serializer.data)

        return response.BadRequest({'error_message': 'Employee not found'})

    def get_queryset(self):
        company = tenant_from_request(self.request)
        team = team_from_request(self.request)
        return super().get_queryset().filter(company=company).filter(id=team.id)
