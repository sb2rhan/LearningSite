from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class News(models.Model):
    title = models.CharField(verbose_name='Title', max_length=120)
    themes = models.ManyToManyField('Theme')
    publish_date = models.DateTimeField(verbose_name='Date of publish', auto_now=timezone.now())
    content = models.TextField(blank=False, null=False)
    image = models.ImageField(null=True, blank=True)
    is_active = models.BooleanField(verbose_name='Is active', null=False, default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
        ordering = ['-id']

    def __str__(self):
        return f'News: {self.title}, by {self.author}, {self.publish_date}'

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"id": self.pk})


class Theme(models.Model):
    name = models.CharField(verbose_name="Theme", max_length=100)

    def __str__(self):
        return f'Theme: {self.name}'
