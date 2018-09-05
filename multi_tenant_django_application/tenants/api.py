from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAdminUser

from multi_tenant_django_application.tenants.models import CompanyModel
from multi_tenant_django_application.tenants.serializers import CompanySerializer


class CompanyViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     viewsets.GenericViewSet):
    queryset = CompanyModel.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (IsAdminUser, )
