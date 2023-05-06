from django.shortcuts import render
from .forms import UploadPDFForm
from .resumidor import generate_wordcloud


def resumen(request):
    if request.method == 'POST':
        form = UploadPDFForm(request.POST, request.FILES)
        if form.is_valid():
            file_path = request.FILES.get('file_path') # intenta obtener el archivo del objeto FILES
            url = request.POST.get('url')
            
            if file_path is not None: # comprueba si el archivo se envió
                response, page = generate_wordcloud(file_path, None)
                result = response.to_image()
                result_path = "static/wordCloud/imagen.png" # reemplazar con la ruta deseada
                result.save(result_path)
                
            elif url is not None: # comprueba si la URL se envió
                response, page = generate_wordcloud(None, url)
                result = response.to_image()
                result_path = "static/wordCloud/imagen.png" # reemplazar con la ruta deseada
                result.save(result_path)
                
            context = {
                'page': page,
                'file_path': file_path,
                'url': url
            }
                
            return render(request, 'nube/nube.html', context)
        
    else:
        form = UploadPDFForm()
        
    return render(request, 'resumen/resumen.html', {'form': form})


