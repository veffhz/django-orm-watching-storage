from django.shortcuts import render

from datacenter.models import Visit
from datacenter.models import format_duration


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at__isnull=True)

    non_closed_visits = [
        {
            "who_entered": visit.passcard.owner_name,
            "entered_at": visit.entered_at,
            "duration": format_duration(visit.get_duration()),
            "is_strange": visit.is_visit_long(),
        }
        for visit in visits
    ]
    context = {
        "non_closed_visits": non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
