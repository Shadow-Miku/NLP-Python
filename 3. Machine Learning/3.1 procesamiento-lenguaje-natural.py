import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Leer y cargar los mensajes desde un archivo
# La primera parte del código carga las líneas desde un archivo, eliminando los caracteres de nueva línea
mensajes = [line.rstrip() for line in open("./sms+spam+collection/SMSSpamCollection")]

# Mostrar el primer mensaje y algunos datos iniciales
print("Primer mensaje:\n", mensajes[0])
print("\nCantidad total de mensajes:\n", len(mensajes))
print("\nPrimeros 10 mensajes:\n")
for index, mensaje in enumerate(mensajes[:10]):
    print(f"{index + 1}: {mensaje}")
print("\n")

# Cargar los datos en un DataFrame para un mejor manejo
df_mensajes = pd.read_csv(
    "./sms+spam+collection/SMSSpamCollection", sep="\t", names=["label", "sms_message"]
)

# Inspeccionar los primeros registros del DataFrame
print("Primeros registros del DataFrame:\n", df_mensajes.head(), "\n")

# Agregar una columna para la longitud de los mensajes
df_mensajes["longitud"] = df_mensajes["sms_message"].apply(len)
print("DataFrame con columna de longitud:\n", df_mensajes.head(), "\n")

# Contar la cantidad de mensajes por etiqueta (label)
print("Cantidad de mensajes por etiqueta:\n", df_mensajes["label"].value_counts(), "\n")

# Visualización de la distribución de longitudes de mensajes
plt.figure(figsize=(10, 6))
plt.hist(df_mensajes["longitud"], bins=300, color='blue', alpha=0.7)
plt.title("Distribución de longitudes de mensajes")
plt.xlabel("Longitud del mensaje")
plt.ylabel("Frecuencia")
plt.show()

# Estadísticas descriptivas de las longitudes de los mensajes
print("Estadísticas descriptivas de la longitud de los mensajes:\n", df_mensajes["longitud"].describe(), "\n")

# Graficar histogramas separados por etiqueta (spam o no spam)
# Graficar histogramas separados por etiqueta (spam o no spam)
plt.figure(figsize=(12, 6))
for label in df_mensajes["label"].unique():
    subset = df_mensajes[df_mensajes["label"] == label]
    plt.hist(subset["longitud"], bins=200, alpha=0.6, label=f"Etiqueta: {label}")
plt.title("Distribución de longitudes por etiqueta")
plt.xlabel("Longitud del mensaje")
plt.ylabel("Frecuencia")
plt.legend()
plt.tight_layout()
plt.show()


# Documentación:
# Este código analiza un conjunto de datos SMS etiquetados como spam o no spam.
# 1. Carga el archivo "SMSSpamCollection" y lo organiza en un DataFrame con columnas "label" y "sms_message".
# 2. Agrega una columna "longitud" que representa el número de caracteres en cada mensaje.
# 3. Genera gráficos para visualizar la distribución de longitudes y compara entre mensajes spam y no spam.
# 4. Realiza un conteo de las etiquetas y presenta estadísticas descriptivas de la longitud de los mensajes.
