import sys
import io
import spacy
from spacy.matcher import Matcher

# Configurar la codificación a UTF-8 para la salida estándar y de error
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Cargar el modelo de SpaCy para español
pln = spacy.load("es_core_news_sm")

# Crear el matcher
matcher = Matcher(pln.vocab)

# Definir el patrón
patron = [{'LOWER': 'nuclear'}]

# Añadir el patrón al matcher
matcher.add('NUCLEAR', [patron])

# Leer el texto del archivo
doc = pln("La energía nuclear es una forma de energía que se libera en reacciones nucleares, específicamente en la fisión nuclear o la fusión nuclear. En las centrales nucleares, la fisión nuclear se utiliza para generar electricidad. Este proceso involucra la división de núcleos atómicos pesados, como el uranio-235 o el plutonio-239, en núcleos más ligeros, liberando una gran cantidad de energía en forma de calor. Este calor se utiliza para producir vapor que impulsa turbinas eléctricas y, en última instancia, genera electricidad.")

# Buscar coincidencias en el documento  
matches = matcher(doc)

# Contar las coincidencias encontradas
print("\nSon encontradas {} coincidencias.".format(len(matches)))

# Mostrar las coincidencias encontradas
for id, start, end in matches:
    id_str = pln.vocab.strings[id]
    word = doc[start:end]
    print("{}: {} en {}".format(id_str, word, start))
    
