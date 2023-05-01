from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()


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
    pub_date = models.DateTimeField(
        _('Publication date'),
        auto_now_add=True
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
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=_('Author'),
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
