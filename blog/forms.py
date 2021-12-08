from django import forms
from .models import Blog
  
class BloglForm(forms.ModelForm):
  
    class Meta:
        model = Blog
        fields = ['title','description','image']