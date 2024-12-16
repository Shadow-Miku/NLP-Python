import re

def encontrar_correos(texto):
    patron = r'\b[\w.-]+@[\w.-]+\.\w+\b' #expresión regular más robusta que captura correos electrónicos, incluyendo caracteres comunes como puntos (.) y guiones (-).
    
    coincidencias = re.findall(patron, texto)
    
    return coincidencias

# Ejemplo de uso
texto = "Puedes contactarme en usuario@example.com o en otro.correo@gmail.com."
print(encontrar_correos(texto))  # Debería imprimir ['usuario@example.com', 'otro.correo@gmail.com']

# Ejemplo con texto vacío
texto_vacio = ""
print(encontrar_correos(texto_vacio))  # Debería imprimir []
