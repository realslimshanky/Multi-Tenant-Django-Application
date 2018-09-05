from django.db import models
from django.utils.translation import ugettext_lazy as _

from multi_tenant_django_application.users.models import User
from multi_tenant_django_application.tenants.models import CompanyAwareModel


class EmployeeModel(CompanyAwareModel):
    employee = models.OneToOneField(User, verbose_name=_('Employee'), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.employee)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ('employee', )
