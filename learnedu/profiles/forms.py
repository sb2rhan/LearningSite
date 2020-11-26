from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserChangeForm

from .models import Post, Profile, Course


class PostForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['placeholder'] = 'Content'
        self.fields['profile'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Post
        fields = ['title', 'content', 'profile']


class ProfileForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['user'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['class'] = 'form-control'
        self.fields['bio'].widget.attrs['placeholder'] = 'Bio'
        self.fields['birth_date'].widget.attrs['class'] = 'form-control'
        self.fields['birth_date'].widget.attrs['placeholder'] = 'Date of birth'
        self.fields['picture'].widget.attrs['class'] = 'form-control'
        self.fields['background_picture'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = Profile
        fields = ['user', 'bio', 'birth_date', 'picture', 'background_picture']


class CourseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'Name of course'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        self.fields['description'].widget.attrs['placeholder'] = 'Description'
        self.fields['instructor'].widget.attrs['class'] = 'form-control'
        self.fields['duration'].widget.attrs['class'] = 'form-control'
        self.fields['duration'].widget.attrs['placeholder'] = 'Duration of the course'
        self.fields['link_material'].widget.attrs['class'] = 'form-control'
        self.fields['link_material'].widget.attrs['placeholder'] = 'Link to material'

    class Meta:
        model = Course
        fields = ['name', 'description', 'instructor', 'duration', 'link_material']


# Feature
class UserEditForm(UserChangeForm):
    pass
