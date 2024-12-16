import sys
import io
import spacy

# Configurar la codificación a UTF-8 para la salida estándar y de error
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Cargar el modelo de SpaCy para español
pln = spacy.load("es_core_news_sm")

# Procesar un texto de ejemplo
doc = pln("Hola, ¿cómo estás?")

# Iterar sobre las palabras del documento y mostrar sus etiquetas POS (Part of Speech)
for palabra in doc:
    print(palabra, palabra.pos_)

# Procesar otro texto que contiene múltiples frases
doc2 = pln("Esta es la primera frase. La segunda frase. La tercera frase.")

# Iterar sobre las frases (oraciones) del documento y mostrarlas
for frase in doc2.sents:
    print(frase)

# Procesar un texto más complejo
doc3 = pln("Los vehículos eléctricos serán decisivos para afrontar las nuevas megatendencias de la sociedad del futuro.")

# Iterar sobre los grupos nominales del documento y mostrarlos
for parte in doc3.noun_chunks:
    print(parte)


# Represantación gráfica
from spacy import displacy

doc4 = pln("Publicada en 1967, Cien Años de Soledad nos adentra en la historia de la familia Buendía a lo largo de varias generaciones en el ficticio pueblo de Macondo.")
displacy.render(doc4, style="ent")

displacy.serve(doc4, style="dep")