import sys
import io
import spacy

pln = spacy.load("es_core_news_sm")

# Configurar la codificación a UTF-8 para la salida estándar y de error
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

print(pln.Defaults.stop_words)

print(pln.vocab['no'].is_stop)

print(len(pln.Defaults.stop_words))

pln.Defaults.stop_words.add('buenas')

pln.vocab['buenas'].is_stop = False
