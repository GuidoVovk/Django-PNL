from django.shortcuts import render
from .forms import UploadPDFForm
from .entidades import buscar_entidades

# Create your views here.
def entity(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = request.FILES['file_path']
            entidades, polaridad = buscar_entidades(file_path)
            context = {
                'entidades':entidades,
                'polaridad':polaridad
            }
        
            
            
            return render(request, 'entity/entity.html', context)

           
    else:
        form = UploadPDFForm()
    return render(request, 'resumen/resumen.html', {'form': form})