from django.http import HttpResponse
from django.shortcuts import render
from .forms import UploadPDFForm
from .resume import generate_resumen


# Create your views here.
def text(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = request.FILES['file_path']
            num_sentences = form.cleaned_data['num_sentences']
            
            # Llamada a la función generate_resumen
            response = generate_resumen(file_path, num_sentences)
            
            # Agregar los valores del título y autor al contexto del template
            context = {
                'response': response,
                'file_path': file_path
            }
           
            
        return render(request, 'text-resume/text-resume.html', context)

    else:
        form = UploadPDFForm()
    return render(request, 'text/text.html', {'form': form})