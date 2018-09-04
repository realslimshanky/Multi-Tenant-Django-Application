from django.db import models
from django.utils.translation import ugettext_lazy as _

from multi_tenant_django_application.tenants.models import CompanyAwareModel


class EmployeeModel(CompanyAwareModel):
    name = models.CharField(_('Employee Name'), max_length=50)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ('name', )
