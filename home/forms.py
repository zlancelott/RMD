from django import forms

from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Submission, File, User, Subject



class SubForm(forms.Form):
    ### CRIAR FORMULÁRIO ###
    subject = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Subject.objects.all())
    topic = forms.CharField(widget=forms.HiddenInput(), max_length=100)
    class_date = forms.DateField(widget=forms.HiddenInput())
    description = forms.CharField(widget=forms.HiddenInput())
    files = forms.ImageField(widget=forms.FileInput(attrs={'id':'files','multiple':True}))

    files.widget.attrs.update({'class': 'btn btn-dark button-files'})



# class SubForm(forms.Form):
#     ### CRIAR FORMULÁRIO ###
#     subject = forms.ModelChoiceField(queryset=Subject.objects.all())
#     topic = forms.CharField(max_length=100)
#     class_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
#     files = forms.ImageField(widget=forms.FileInput(attrs={'id':'files','multiple':True}))

#     files.widget.attrs.update({'class': 'btn btn-dark button-files'})

class UpdateSubForm(forms.Form):
    ### CRIAR FORMULÁRIO ###
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    topic = forms.CharField(max_length=100)
    class_date = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))



# class UpdateSubForm(forms.Form):
#     ### CRIAR FORMULÁRIO ###
#     subject = forms.ModelChoiceField(widget=forms.HiddenInput(), queryset=Subject.objects.all())
#     topic = forms.CharField(widget=forms.HiddenInput(), max_length=100)
#     class_date = forms.DateField(widget=forms.HiddenInput())
#     description = forms.CharField(widget=forms.HiddenInput())