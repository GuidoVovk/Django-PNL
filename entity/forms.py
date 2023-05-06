from django import forms

class UploadPDFForm(forms.Form):
     file_path = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'btn btn-outline-primary'}), label='PDF')
    
