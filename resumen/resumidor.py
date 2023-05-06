import requests
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
from textblob import TextBlob
from wordcloud import WordCloud
from nltk.corpus import stopwords
from random import randint
from wordcloud import get_single_color_func


def generate_wordcloud(file_path=None, url=None):
    if url is not None:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        all_text = soup.get_text()
        number_of_pages = len(all_text.split('\f'))
    

        
    elif file_path:
        reader = PdfReader(file_path, None)
        number_of_pages = len(reader.pages) 

        all_text = ""

        for i in range(number_of_pages):
            page = reader.pages[i]
            text = page.extract_text()
            all_text += text  # Agregar el texto de cada página a la variable `all_text`
    
    else:
        return None, None
    

    # Crear un diccionario con el número de páginas
    context = number_of_pages

    # Cargar las palabras vacías en una lista
    stop_words = set(stopwords.words('spanish'))

    additional_stop_words = set(['una', 'más', 'cuando', 'si', 'los', 'las', 'que', 'en', 'la', 'el', 'de','se', 'su', 'es', 'del', 'al', 'por', 'lo', 'también', 'pero', 'pp'])
    stop_words = stop_words.union(additional_stop_words)

    # Limpiar el texto eliminando las palabras vacías
    words = all_text.split()
    clean_text = " ".join([word for word in words if word.lower() not in stop_words])

    # Crear un objeto TextBlob con el texto limpio
    blob = TextBlob(clean_text)
    
    
    def color_func(word, font_size, position, orientation, random_state=None, **kwargs):
        colors = ['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#f1c40f', '#e67e22', '#e74c3c', '#ecf0f1', '#95a5a6', '#34495e']
        return colors[randint(0, len(colors)-1)]

    # Crear una instancia de WordCloud con el objeto TextBlob
    wordcloud = WordCloud(width=800, height=400, color_func=color_func).generate(str(blob))
    
    return wordcloud, context
    
   
