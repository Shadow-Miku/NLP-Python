import spacy

# Cargar el modelo de SpaCy para inglés
nlp = spacy.load("en_core_web_sm")

# Función para mostrar las entidades en un documento
def mostrar_entidades(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + " - " + ent.label_ + " - " + str(spacy.explain(ent.label_)))
    else:
        print("No se encontraron entidades.")
        
# Ejemplo de uso sin entidades
doc = nlp("Barack Obama was the 44th president of the United States.")
mostrar_entidades(doc)

print("\n")

# Ejemplo de uso con entidades
doc = nlp("I will go to New York. I will visit the Empire State Building.")
mostrar_entidades(doc)