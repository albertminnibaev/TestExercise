from django.contrib.auth.models import (
    BaseUserManager
)


class UserManager(BaseUserManager):
    """
    функция создания пользователя — в нее мы передаем обязательные поля
    """

    def create_user(self, email, first_name, last_name, phone, is_active=False, is_superuser=False,
                    is_staff=False, is_admin=False, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone=phone
        )
        user.is_active = is_active
        user.is_superuser = is_superuser
        user.is_staff = is_staff
        user.is_admin = is_admin
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, first_name, last_name, phone, password=None):
        """
        функция для создания суперпользователя — с ее помощью мы создаем админинстратора
        это можно сделать с помощью команды createsuperuser
        """

        user = self.create_user(
            email,
            first_name=first_name,
            last_name=last_name,
            phone=phone,
            is_active=True,
            is_superuser=True,
            is_staff=True,
            is_admin=True,
            password=password,
        )

        user.save(using=self._db)
        return user
