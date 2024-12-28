import spacy

# Cargar el modelo de SpaCy para español
nlp = spacy.load("es_core_news_sm")

# Texto a ser analizado
texto = "El sol es un cuerpo celeste que brilla de manera especial y se encuentra en el centro del sistema solar. La luz solar se encuentra en la parte superior de la atmosfera terrestre."

# Procesar el texto
doc = nlp(texto)

# Tokenizar y mostrar cada token
print("Tokens en el texto:")
for token in doc:
    print(f"Token: {token.text}, Lemma: {token.lemma_}, POS: {token.pos_}, Tag: {token.tag_}, Dep: {token.dep_}, Shape: {token.shape_}, is_alpha: {token.is_alpha}, is_stop: {token.is_stop}")

print("\nFrases en el texto:")
for token in doc: 
    print(token)