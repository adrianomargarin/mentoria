from django.db import models
from django.utils.translation import gettext_lazy as _
from mentoria.core.models import AbstractBaseModel


class Category(AbstractBaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=50)
    slug = models.SlugField(verbose_name=_('slug'), max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'
