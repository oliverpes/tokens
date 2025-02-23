def contienetoken(cadena, tokens):
    palabras_reservadas = [token for token in tokens if token in cadena ]#obtenemos los tokens que estan dentro de la cadena
    return palabras_reservadas#devuelve los tokens dentro de la cadena

tokens_predefinidos  = ["clase", "alumnos"] #definiomos los okens reservados

cadena_entrada = input("ingrese un texto: ")#se ingresa la cadena de texto por el usuario

tokens_encontrados = contienetoken(cadena_entrada,tokens_predefinidos)#se ingresa la cadena a la funcion y los tokens predefinidos 

if tokens_predefinidos:#se validan los tokens dentro de la cadena de texto
    print("se encontraron los siguientes tokens:", tokens_encontrados)#se muestran los tokens en la cadena
else:#se valida el caso contrario
    print("no se encontraron tokens en la cadena")#se confirma si no se encontraron tokens definidos en la cadena