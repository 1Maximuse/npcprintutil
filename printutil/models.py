import os
import mimetypes
from datetime import datetime
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

def get_file_path(instance, filename):
    return 'source/' + instance.username.username + '/' + filename

def validate_size(value):
    if value.size > 10*1024*1024:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value

def validate_type(value):
    mime = mimetypes.guess_type(value.url)
    if mime[0].split('/')[0] != 'text':
        raise ValidationError("The file type is unsupported")
    return value

class PrintRequest(models.Model):
    username = models.ForeignKey(get_user_model(), related_name='users', on_delete=models.SET(get_sentinel_user))
    req_time = models.DateTimeField(auto_now_add=True)
    source = models.FileField("Source", upload_to=get_file_path, validators=[validate_size, validate_type])
    printed = models.BooleanField(default=False)
    def __str__(self):
        return self.req_time.strftime("%d/%m/%Y, %H:%M:%S")
    def filename(self):
        return os.path.basename(self.source.name)
    def link(self):
        return self.source.url
    def printlink(self):
        return '/print/' + self.username.username + '/' + os.path.basename(self.source.name)