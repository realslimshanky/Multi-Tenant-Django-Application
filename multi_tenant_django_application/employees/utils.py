from multi_tenant_django_application.employees.models import TeamModel


def team_from_request(request):
    full_url = request._request.get_raw_uri()
    team_aware_suffix = full_url.split('/')
    if team_aware_suffix[3] == 'api' and team_aware_suffix[5] == 'teams' and len(team_aware_suffix) > 7:
        return TeamModel.objects.filter(id=team_aware_suffix[6]).first()
    else:
        return TeamModel.objects.none()
