from channels.db import database_sync_to_async
from core.models import UserDetail


@database_sync_to_async
def userdata(id):
    return UserDetail.objects.get(id=id)
    