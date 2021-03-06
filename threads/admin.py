from django.contrib import admin
from .models import Thread, Group, Message, Report, GroupMember

admin.site.register(
    Thread,
    list_display=["id", "title", "author", "created"],
)

admin.site.register(
    Group,
    list_display=["id", "name", "created", "frontpage"],
)

admin.site.register(
    GroupMember,
    list_display=["id", "user", "group", "status"],
)

admin.site.register(
    Message,
    list_display=["id", "created"],
)

admin.site.register(
    Report,
    list_display=["id", "thread", "message", "type", "comment"],
)
