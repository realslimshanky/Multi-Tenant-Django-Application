# Third Party Stuff
from rest_framework.routers import DefaultRouter

# Multi Tenant Django Application Stuff
from multi_tenant_django_application.base.api.routers import SingletonRouter
from multi_tenant_django_application.users.api import CurrentUserViewSet
from multi_tenant_django_application.users.auth.api import AuthViewSet
from multi_tenant_django_application.tenants.api import CompanyViewSet
from multi_tenant_django_application.employees.api import EmployeeViewSet

default_router = DefaultRouter(trailing_slash=False)
singleton_router = SingletonRouter(trailing_slash=False)
company_router = DefaultRouter(trailing_slash=False)

# Register all the django rest framework viewsets below.
default_router.register('auth', AuthViewSet, base_name='auth')
singleton_router.register('me', CurrentUserViewSet, base_name='me')
default_router.register('company', CompanyViewSet, base_name='companies')
company_router.register(r'[a-z A-Z]+', EmployeeViewSet, base_name='company')

# Combine urls from both default and singleton routers and expose as
# 'urlpatterns' which django can pick up from this module.
urlpatterns = default_router.urls + singleton_router.urls + company_router.urls
