from django.db import models
from django.utils.translation import ugettext_lazy as _

from multi_tenant_django_application.users.models import User
from multi_tenant_django_application.tenants.models import CompanyAwareModel


class EmployeeModel(CompanyAwareModel):
    id = models.OneToOneField(User, verbose_name=_('Employee'), on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('Employee')
        verbose_name_plural = _('Employees')
        ordering = ('id', )


class TeamModel(CompanyAwareModel):
    name = models.CharField(_('Team Name'), max_length=20)
    description = models.TextField(_('Team description'))
    employees = models.ManyToManyField(EmployeeModel, verbose_name=_('Employees'))

    class Meta:
        verbose_name = _('Team')
        verbose_name_plural = _('Teams')
        ordering = ('name', )
