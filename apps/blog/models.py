from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from mptt.models import MPTTModel, TreeForeignKey

User = get_user_model()


class Category(MPTTModel):
    name = models.CharField(
        _('Name'),
        max_length=50,
        unique=True
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name=_('Parent'),
        related_name='children',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Post(models.Model):
    title = models.CharField(
        _('Title'),
        max_length=200
    )
    content = models.TextField(
        _('Content'),
        blank=True,
        null=True
    )
    logo = models.URLField(
        _('Logo')
    )
    pub_date = models.DateTimeField(
        _('Publication date')
    )
    update_date = models.DateTimeField(
        _('Update date'),
        auto_now=True
    )
    delete_date = models.DateTimeField(
        _('Delete date'),
        blank=True,
        null=True
    )
    author = models.CharField(
        _('Author'),
        max_length=255,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        'Tag',
        verbose_name=_('Tags'),
        blank=True
    )

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class BannedWord(models.Model):
    word = models.CharField(
        _('Word'),
        max_length=50,
        unique=True
    )
    reason = models.CharField(
        _('Reason'),
        max_length=200,
        blank=True
    )

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = _('Banned word')
        verbose_name_plural = _('Banned words')
