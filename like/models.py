from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User


class LikeCount(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    liked_num = models.IntegerField(default=0)


class LikeRecord(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=True)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id" )

    user = models.ForeignKey(User, on_delete=True)
    liked_time = models.DateTimeField(auto_now_add=True)
