from django.utils import timezone
from django.db import models


class Item(models.Model):
    unprocessed, processed = 0, 1

    STATUS = (
        (unprocessed, 'Unprocessed'),
    )

    job_number = models.CharField(max_length=100, null=True)
    data = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    status = models.CharField(choices=STATUS, max_length=100, default=unprocessed)

    def __str__(self):
        return self.job_number
