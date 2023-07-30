from enum import Enum


class UserRole(Enum):
    ADMIN = "ADMIN"
    USER = "USER"

USER_ROLE_CHOICES = [(role.value, role.name) for role in UserRole]