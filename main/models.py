from django.db import models
from django.db.models.fields.json import JSONField


class Testmodel(models.Model):
    field = models.TextField(max_length=255)
    data = JSONField()

    def __str__(self):
        return self.field, self.data
