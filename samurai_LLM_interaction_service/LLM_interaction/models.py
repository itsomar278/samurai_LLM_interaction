import uuid
from django.db import models
from django.utils.timezone import now
import pytz


def get_uae_time():
    UAE_TIMEZONE = pytz.timezone('Asia/Dubai')
    return now().astimezone(UAE_TIMEZONE)


class Status(models.IntegerChoices):
    RECEIVED = 0, 'Received'
    ERROR_OCCURRED = 1, 'Error Occurred'
    IN_PROGRESS = 2, 'In Progress'
    READY = 3, 'Ready'


class IndexNameStatus(models.Model):
    index_name = models.UUIDField(primary_key=True, editable=False)

    status = models.IntegerField(
        choices=Status.choices,
        default=Status.RECEIVED,
    )

    def __str__(self):
        return f"Index: {self.index_name}, Status: {self.get_status_display()}"


class UserUsageHistory(models.Model):
    request_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    input_tokens_number = models.IntegerField()
    output_tokens_number = models.IntegerField()

    index_name = models.ForeignKey(IndexNameStatus, on_delete=models.CASCADE)

    creation_date = models.DateTimeField(default=get_uae_time)

    def __str__(self):
        return f"Request {self.request_id} by User {self.user_id} on Index {self.index_name.index_name} at " \
               f"{self.creation_date}"
