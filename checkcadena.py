def contienetoken(cadena, tokens):
    palabras_reservadas = [token for token in tokens if token in cadena]  # Filtra los tokens presentes en la cadena
    return palabras_reservadas  # Devuelve los tokens encontrados

# 📌 Se pide al usuario que ingrese los tokens separados por comas
tokens_usuario = input("Ingrese los tokens separados por comas: ")
tokens_predefinidos = [token.strip() for token in tokens_usuario.split(",")]  # Elimina espacios extra

cadena_entrada = input("Ingrese un texto: ")  # Se ingresa la cadena de texto por el usuario

tokens_encontrados = contienetoken(cadena_entrada, tokens_predefinidos)  # Se busca en la cadena

if tokens_encontrados:  # Se valida si hay tokens encontrados
    print("Se encontraron los siguientes tokens:", tokens_encontrados)  # Se muestran los tokens en la cadena
else:  
    print("No se encontraron tokens en la cadena.")  # Se confirma si no se encontraron tokens
