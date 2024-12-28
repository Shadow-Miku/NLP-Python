import spacy
from spacy import displacy

# Cargar el modelo de SpaCy para español
nlp = spacy.load("es_core_news_sm")

# Probar con un texto diferente
doc = nlp("Barack Obama fue el 44º presidente de los Estados Unidos.")

# Verificar las entidades reconocidas y sus propiedades
if doc.ents:
    for ent in doc.ents:
        print(f"Texto: {ent.text}, Etiqueta: {ent.label_}, Inicio: {ent.start_char}, Fin: {ent.end_char}")
else:
    print("No se encontraron entidades.")

# Visualizar entidades en el navegador
displacy.serve(doc, style='ent', host='127.0.0.1', port=5000)


""" 
doc2 = nlp("El sol es un cuerpo celeste que brilla de manera especial y se encuentra en el centro del sistema solar. La luz solar se encuentra en la parte superior de la atmosfera terrestre.")
frases = list(doc2.sents)
displacy.serve(frases, style='dep',options={'distance': 120,'color': 'green'}, host='127.0.0.1', port=5000)
"""

