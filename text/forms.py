from django import forms

class UploadPDFForm(forms.Form):
     file_path = forms.FileField(widget=forms.ClearableFileInput(attrs={'class': 'btn btn-outline-primary'}), label='PDF')
     num_sentences = forms.IntegerField(label='Cantidad de oraciones', min_value=20, max_value=500, initial=20)
