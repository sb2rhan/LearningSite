from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.shortcuts import reverse
from django.utils import timezone
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(verbose_name='Bio', null=True, blank=True)
    birth_date = models.DateField(verbose_name='Date of birth', null=True, blank=True)
    picture = models.ImageField(verbose_name='Profile picture', blank=True, null=True)
    background_picture = models.ImageField(verbose_name='Background picture', blank=True, null=True)
    courses = models.ManyToManyField('Course', blank=True, default=None)

    def __str__(self):
        return f'Profile {self.pk} {self.user} {self.birth_date}'

    def get_absolute_url(self):
        return reverse("profile_page", kwargs={"username": self.user.username})


class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=500)
    publish_date = models.DateTimeField(verbose_name='Date of publish', auto_now=timezone.now())
    is_active = models.BooleanField(verbose_name='Is active', default=True, null=False)

    class Meta:
        ordering = ['-id']


class Course(models.Model):
    name = models.CharField(null=False, blank=False, max_length=200)
    description = models.TextField(null=False, blank=False)
    instructor = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    enroll_count = models.BigIntegerField(default=0)
    is_active = models.BooleanField(verbose_name='Is active', default=True, null=False)

    def __str__(self):
        return f'Course {self.pk} {self.name}'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
