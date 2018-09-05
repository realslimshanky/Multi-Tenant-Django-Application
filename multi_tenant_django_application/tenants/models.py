from django.db import models
from django.utils.translation import ugettext_lazy as _

from multi_tenant_django_application.users.models import User
from multi_tenant_django_application.base.models import TimeStampedUUIDModel


class CompanyModel(TimeStampedUUIDModel):
    name = models.CharField(_('Company Name'), max_length=100)
    admin = models.ForeignKey(User, verbose_name=_('Company Admin'), on_delete=models.SET_NULL, null=True)
    tenant_aware_suffix = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')
        ordering = ('name', )


class CompanyAwareModel(TimeStampedUUIDModel):
    company = models.ForeignKey(CompanyModel, on_delete=models.CASCADE)

    class Meta:
        abstract = True
