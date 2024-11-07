from django.forms import ModelForm
from django import forms
from book_app.models import BookInfo

class BookInfoForm(ModelForm):

    class Meta:
        model = BookInfo
        fields = ['title','author','description','price','publication_date']