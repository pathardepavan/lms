from django import forms
from .models import Author
from .models import Publisher,Author,Book,Issue

class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput),
    password = forms.CharField(widget=forms.PasswordInput)




class IssueCreateForm(forms.ModelForm):
    class Meta:
        model=Issue
        fields=['book','user']
        widgets = {
            'book':forms.Select(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class':'form-control'})
        }


class BookCreateForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['title','price','isbn','authors','publisher','publication_date','available']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'isbn': forms.TextInput(attrs={'class': 'form-control'}),
            # 'authors': forms.ModelMultipleChoiceField(queryset=Author.objects.all(),to_field_name=None),
            'publisher': forms.Select(attrs={'class': 'form-control'}),
            # 'publication_date': forms.DateField(),
            'available':forms.TextInput(attrs={'class':'form-control'})
        }

class PublisherCreateForm(forms.ModelForm):
    class Meta:
        model=Publisher
        fields=['name','address','city','state','country','website']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'state': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'website': forms.TextInput(attrs={'class': 'form-control'})
        }

class AuthorCreateForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name','email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),

        }

