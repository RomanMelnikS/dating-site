from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    SEX_CHOICES = [
        ('м', 'Мужской'),
        ('ж', 'Женский')
    ]

    avatar = models.ImageField(
        upload_to='avatars/',
        verbose_name='Аватарка',
        blank=True,
        null=True
    )
    sex = models.CharField(
        max_length=20,
        verbose_name='Пол',
        choices=SEX_CHOICES,
        blank=True,
        null=False
    )
    email = models.EmailField(
        max_length=254,
        verbose_name='Электронная почта',
        help_text='Адрес вашей эл.почты',
        unique=True,
        null=False
    )
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Match(models.Model):
    liking_client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='liking',
        verbose_name='Симпатизирующий'
    )
    liked_client = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='liked',
        verbose_name='Понравившийся',
        null=True
    )

    def __str__(self):
        return ('Симпатии')

    class Meta:
        verbose_name = 'Симпатии'
        verbose_name_plural = 'Симпатии'
