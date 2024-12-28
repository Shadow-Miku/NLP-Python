import spacy

# Cargar el modelo de SpaCy para español (modelo grande)
nlp = spacy.load("es_core_news_lg")

# Obtener el vector de la palabra "gato"
gato_vector = nlp(u'gato').vector
print("Vector de la palabra 'gato':")
print(gato_vector)
print('\n')

# Obtener el vector del texto completo
text = nlp(u'El gato es un animal doméstico')
text_vector = text.vector
print("Vector del texto 'El gato es un animal doméstico':")
print(text_vector)
print('\n')

# Analizar la similitud entre palabras
words = nlp(u'gato pez ave')
print("Similitud entre palabras:")
for word1 in words:
    for word2 in words:
        # Calcular y mostrar la similitud entre pares de palabras
        similarity = word1.similarity(word2)
        print(f"{word1.text} - {word2.text}: {similarity:.2f}")
