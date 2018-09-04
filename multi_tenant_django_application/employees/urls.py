from rest_framework.routers import DefaultRouter

from multi_tenant_django_application.employees.views import EmployeeViewSet


defaultrouter = DefaultRouter(trailing_slash=False)
defaultrouter.register('', EmployeeViewSet, base_name='company')

urlpatterns = defaultrouter.urls
