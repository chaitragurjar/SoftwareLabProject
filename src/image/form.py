from django import forms
from .models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model=Image
        fields=('Song_Name','Upload_File')
        widgets = {
            'Song_Name': forms.TextInput(attrs={'class':'form-control'}),
            'Upload_File': forms.ClearableFileInput(attrs={'class':'form-control'}),
        }