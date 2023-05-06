from PyPDF2 import PdfReader
import spacy
from textblob import TextBlob

def buscar_entidades(file_path):
    reader = PdfReader(file_path)
    number_of_pages = len(reader.pages) 

    all_text = ""

    for i in range(number_of_pages):
        page = reader.pages[i]
        text = page.extract_text()
        all_text += text  # Agregar el texto de cada página a la variable `all_text`
    
# Load English tokenizer, tagger, parser and NER
    nlp = spacy.load("es_core_news_sm")
    doc = nlp(all_text)

    # Find named entities, phrases and concepts
    entidades = []
    for ent in doc.ents:
        entidades.append((ent.text, ent.label_))


    # Perform sentiment analysis
    blob = TextBlob(all_text)
    polaridad_oraciones = []
    for sentence in blob.sentences:
        polaridad_oraciones.append((sentence, "Polarity:", sentence.sentiment.polarity))

    polaridad = ("Polaridad del texto: ", blob.sentiment.polarity)
    
    return entidades, polaridad