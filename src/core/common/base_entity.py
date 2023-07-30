import re
import uuid

from django.db import models
from django.db.models.base import ModelBase


class CustomModelBase(ModelBase):
    def __new__(cls, name, bases, attrs, **kwargs):
        if 'Meta' not in attrs:
            class Meta:
                pass
            attrs['Meta'] = Meta

        meta = attrs['Meta']

        if not hasattr(meta, 'db_table') and not getattr(meta, 'abstract', False):
            db_table = "_".join(re.findall("[A-Z][^A-Z]*", name)).lower()
            meta.db_table = db_table

        return super().__new__(cls, name, bases, attrs, **kwargs)


class BaseEntity(models.Model, metaclass=CustomModelBase):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
