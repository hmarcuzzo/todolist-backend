from django.contrib.auth.hashers import check_password
from django.db import models
from django.forms import EmailField, CharField, DateTimeField

from src.core.common.base_entity import BaseEntity
from src.core.constants.enums.user_role import USER_ROLE_CHOICES, UserRole


class User(BaseEntity):
    email: EmailField = models.EmailField(max_length=128, unique=True)
    password: CharField = models.CharField(max_length=128)
    role: CharField = models.CharField(
        max_length=20,
        choices=USER_ROLE_CHOICES,
        default=UserRole.USER.value
    )
    last_login: DateTimeField = models.DateTimeField(blank=True, null=True)

    def check_password(self, raw_password: str) -> bool:
        return check_password(raw_password, self.password)
