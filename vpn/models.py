from django.conf import settings
from django.db import models
from django.core.validators import URLValidator


class Site(models.Model):
    site_name = models.CharField(max_length=255)
    original_url = models.URLField(max_length=255, validators=[URLValidator()])
    sent_data = models.PositiveIntegerField(default=0, null=False)
    received_data = models.PositiveIntegerField(default=0, null=False)
    number_of_transitions = models.PositiveIntegerField(default=0, null=False)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.site_name

    class Meta:
        unique_together = ('original_url', 'user_id')

