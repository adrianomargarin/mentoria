from django.utils.translation import gettext_lazy as _
from mentoria.core.models import AbstractBaseModel, models


class Post(AbstractBaseModel):
    category = models.ForeignKey('blog.Category', verbose_name=_('category'), on_delete=models.PROTECT)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    subtitle = models.CharField(verbose_name=_('sub title'), max_length=50)
    slug = models.SlugField(verbose_name=_('slug'), max_length=50, unique=True)
    text = models.TextField(verbose_name=_('text'))
    created_by = models.ForeignKey(
        'auth.User',
        verbose_name=_('created by'),
        related_name='posts_created_by',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    published_by = models.ForeignKey(
        'auth.User',
        verbose_name=_('created by'),
        related_name='posts_published_by',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    published_at = models.DateTimeField(verbose_name=_('published at'), null=True, blank=True)
    tags = models.ManyToManyField('blog.Tag', verbose_name=_('tags'), blank=True)

    def __str__(self):
        return f'{self.title}'
