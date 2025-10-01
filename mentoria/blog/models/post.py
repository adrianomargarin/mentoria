from django.utils.translation import gettext_lazy as _
from mentoria.core.models import AbstractBaseModel, models


class Post(AbstractBaseModel):
    category = models.ForeignKey('blog.Category', verbose_name=_('category'), on_delete=models.PROTECT)
    title = models.CharField(verbose_name=_('name'), max_length=50)
    slug = models.SlugField(verbose_name=_('slug'), max_length=50, unique=True)
    text = models.TextField(verbose_name=_('text'))
    tags = models.ManyToManyField('blog.Tag', verbose_name=_('tags'), blank=True)

    def __str__(self):
        return f'{self.title}'
