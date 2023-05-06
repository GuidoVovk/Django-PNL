from django import forms

class UploadPDFForm(forms.Form):
     file_path = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'form-control btn btn-outline-dark'}), label='PDF', required=False)
     url = forms.CharField(widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'Ingrese URL'}), label='URL', required=False)
    
