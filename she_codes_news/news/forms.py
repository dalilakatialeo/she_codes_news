from django import forms #to use all the super cool django form stuff
from django.forms import ModelForm
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta: 
        #nested class we want django to infer from
        model = NewsStory
        #list of fields to be included in the form
        fields = ['title', 'author', 'pub_date', 'content'] 
        widgets = {
            'pub_date': forms.DateInput(format=('%m/%d/%Y'),
            attrs={"class":"form-control", 
            "placeholder":"Select a date",
            "type":"date"})
}