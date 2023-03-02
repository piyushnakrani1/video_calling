import uuid
from django.db import models

# Create your models here.

class UserDetail(models.Model):
    id = models.UUIDField(primary_key=True , default=uuid.uuid4 , editable= False, max_length=255)
    username = models.CharField(max_length=255, blank=True, null= True)
    is_active = models.BooleanField(default=False)
    reported = models.IntegerField(default = 0, blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username