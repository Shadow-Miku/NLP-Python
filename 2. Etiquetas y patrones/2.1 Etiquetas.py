import sys
import io
import spacy

# Configurar la codificación a UTF-8 para la salida estándar y de error
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# Cargar el modelo de SpaCy para español
nlp = spacy.load("es_core_news_sm")

# Función para explicar etiquetas
def mostrar_etiquetas(documento):
    print(f"\n{'Texto':<12} {'POS':<12} {'Etiqueta':<12} {'Explicación':<30}")
    print('-' * 60)
    for word in documento:
        pos_explicacion = spacy.explain(word.pos_)  # Explicación de POS
        tag_explicacion = spacy.explain(word.tag_)  # Explicación de Tag
        print(f"{word.text:<12} {word.pos_:<12} {word.tag_:<12} {pos_explicacion or tag_explicacion}")

# Primer documento
documento = nlp("La energía nuclear es una fuente de energía limpia y potente. La energía es vital para el desarrollo.")
print("Primer Documento:")
mostrar_etiquetas(documento)

# Segundo documento
documento2 = nlp("El sol es un cuerpo celeste que brilla de manera especial y se encuentra en el centro del sistema solar. La luz solar se encuentra en la parte superior de la atmosfera terrestre.")
print("\nSegundo Documento:")
mostrar_etiquetas(documento2)
