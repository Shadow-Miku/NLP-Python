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

# Definir los patrones
patron1 = [{'LOWER': 'nuclear'}]
patron2 = [{'LOWER': 'energía'}]

# Añadir los patrones al matcher de manera individual
matcher.add('NUCLEAR', [patron1])
matcher.add('ENERGÍA', [patron2])

# Leer el texto del archivo
with open('energia-nuclear.txt', 'r', encoding='utf-8') as file:
    doc = pln(file.read())

# Buscar coincidencias en el documento
matches = matcher(doc)

# Diccionario para almacenar las coincidencias por patrón
coincidencias_por_patron = {'NUCLEAR': [], 'ENERGÍA': []}

# Mostrar las coincidencias encontradas con su posición
for match_id, start, end in matches:
    span = doc[start:end]
    id_str = pln.vocab.strings[match_id]
    # Guardar texto y posiciones
    coincidencias_por_patron[id_str].append({
        'texto': span.text,
        'start_char': span.start_char,
        'end_char': span.end_char
    })

# Imprimir las coincidencias con posiciones
for patron, coincidencias in coincidencias_por_patron.items():
    print(f"Patrón '{patron}':")
    for c in coincidencias:
        print(f"  - {c['texto']} (posición: {c['start_char']}-{c['end_char']})")

# Contar las coincidencias encontradas
print(f"\nSe encontraron {len(matches)} coincidencias en total.")
