from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify




active_field_choices = [
    (True, _('Active')),
    (False, _('Inactive'))
]




class Language(models.Model):
    code = models.CharField(_('code'),max_length = 25)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)


    def __str__(self):
        return self.code


class Category(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    parent = models.ForeignKey('self', related_name='father', on_delete=models.CASCADE, blank=True, null=True)
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=100)
    content = models.TextField(_('content'), max_length=4000)
    categories = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.FileField(_('image'),upload_to="static/img/",null=False, blank=False)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)
    views_counter = models.IntegerField(_('views count'), null=True, blank=True, default=0, editable=False)
    active = models.BooleanField(_('active'), default=True, choices=active_field_choices)
    slug = models.SlugField()





    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title




class PostLanguage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_lang', verbose_name=_('post'))
    language = models.ForeignKey(Language, on_delete=models.PROTECT, related_name='posts_lan', verbose_name=_('language'))


    def __str__(self):
        return self.title

class TranslateLanguage(models.Model):
    language_code = models.CharField( max_length=10)
    def __str__(self):
        return self.language_code

# Create your models here.
