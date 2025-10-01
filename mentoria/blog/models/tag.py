from django.utils.translation import gettext_lazy as _
from mentoria.core.models import AbstractBaseModel, models


class Tag(AbstractBaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=50, unique=True)

    def __str__(self):
        return f'{self.name}'
