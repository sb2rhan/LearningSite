from django import forms
from django.forms import fields
from .models import News


class NewsForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget.attrs['placeholder'] = 'Title'
        self.fields['themes'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['author'].widget.attrs['class'] = 'form-control'

    class Meta:
        model = News
        fields = ['title', 'themes', 'content', 'image', 'author']
