from django.db import models
from django.contrib.auth.models import User
from django.utils.baseconv import base64
from .datafile import get_all_files, get_columns

class File(models.Model):
    data = get_all_files()
    result = []
    for res in data:
        result.append(get_columns(res))
    print(result)