from multi_tenant_django_application.tenants.models import CompanyModel


def tenant_from_request(request):
    full_url = request._request.get_raw_uri()
    tenant_aware_suffix = full_url.split('/')
    if tenant_aware_suffix[3] == 'company' and len(tenant_aware_suffix) > 4:
        return CompanyModel.objects.filter(tenant_aware_suffix=tenant_aware_suffix[4]).first()
    else:
        return CompanyModel.objects.none()
