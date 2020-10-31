from django.db import models
from django.utils.timezone import now


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def get_duration(self):
        if self.leaved_at:
            return (self.leaved_at - self.entered_at).total_seconds()
        return (now() - self.entered_at).total_seconds()

    def is_visit_long(self, minutes=60):
        duration = self.get_duration()
        return duration // 60 > minutes

    def __str__(self):
        return "{user} entered at {entered} {leaved}".format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved="leaved at " + str(self.leaved_at) if self.leaved_at else "not leaved"
        )


def format_duration(duration):
    hours = duration // (60*60)
    seconds = duration % (60*60)
    minutes = seconds // 60
    return '%02i:%02i' % (hours, minutes)
