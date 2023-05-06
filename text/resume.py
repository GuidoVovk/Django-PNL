from PyPDF2 import PdfReader
import nltk
import heapq
from pdfminer.high_level import extract_text
from nltk import word_tokenize,sent_tokenize
import re
import PyPDF2
import spacy


nlp = spacy.load("es_core_news_lg")
nlp.max_length = 2000000 # 2 millones de caracteres


def generate_resumen(file_path, num_sentences):
    
    # Extraer texto del PDF
    article_text = PdfReader(file_path)
    number_of_pages = len(article_text.pages)
    
    all_text = ""

    for i in range(number_of_pages):
        page = article_text.pages[i]
        text = page.extract_text()
        all_text += text  # Agregar el texto de cada página a la variable `all_text`

    
    # Removing Square Brackets and Extra Spaces
    all_text = re.sub(r'\[[0-9]*\]', ' ', all_text)  
    all_text = re.sub(r'\s+', ' ', all_text)  
 
    formatted_article_text = re.sub('[^a-zA-Z]', ' ', all_text )  
    formatted_article_text = re.sub(r'\s+', ' ', formatted_article_text)  
    #nltk.download()
    #EN ESTA PARTE HACE LA TOKENIZACION 
    sentence_list = nltk.sent_tokenize(all_text)  
 
    #EN ESTA PARTE ENCUENTRA LA FRECUENCIA DE CADA PALABRA
    stopwords = nltk.corpus.stopwords.words('spanish')
 
    word_frequencies = {}  
    for word in nltk.word_tokenize(formatted_article_text):  
        if word not in stopwords:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1
 

    if word_frequencies:
        maximum_frequency = max(word_frequencies.values())
    else:
        maximum_frequency = 0

 
    for word in word_frequencies.keys():  
        word_frequencies[word] = (word_frequencies[word]/maximum_frequency)
 
    #CALCULA LAS FRASES QUE MÁS SE REPITEN
    sentence_scores = {}  
    for sent in sentence_list:  
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 40:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]
 
    #REALIZA EL RESUMEN CON LAS MEJORES FRASES
      
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
 
    summary = ' '.join(summary_sentences)  
    
    return summary  
 