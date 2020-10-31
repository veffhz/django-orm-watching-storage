from django.shortcuts import render

from datacenter.models import Visit
from datacenter.models import Passcard
from datacenter.models import format_duration


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode).get()
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = [
        {
            "entered_at": visit.entered_at,
            "duration": format_duration(visit.get_duration()),
            "is_strange": visit.is_visit_long(),
        }
        for visit in visits
    ]
    context = {
        "passcard": passcard,
        "this_passcard_visits": this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
