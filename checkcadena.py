def contienetoken(cadena, tokens):
    try:
        if not cadena:
             raise ValueError("La cadena de entrada no puede estar vacía.")
        if not tokens:
            raise ValueError("Debe ingresar al menos un token válido.")

        palabras_reservadas = [token for token in tokens if token in cadena]  # Filtra los tokens presentes en la cadena
        return palabras_reservadas, None  # Devuelve los tokens encontrados

    except Exception as e:
        #print(f"Error en el análisis léxico: {e}")
        return [], str[e]



#almacenamos los errores en variables
error_mensaje = None
error_tipo = None

try:
    # 📌 Se pide al usuario que ingrese los tokens separados por comas
    tokens_usuario = input("Ingrese los tokens separados por comas: ").strip()
    if not tokens_usuario:
        raise ValueError("Debe ingresar al menos un token válido.")

    tokens_predefinidos = [token.strip() for token in tokens_usuario.split(",") if token.strip()]
    if not tokens_predefinidos:
        raise ValueError("Debe ingresar al menos un token válido después del procesamiento.")

    # Se ingresa la cadena o texto
    cadena_entrada = input("Ingrese un texto: ").strip()
    if not cadena_entrada:
        raise ValueError("La cadena de entrada no puede estar vacía.")

    tokens_encontrados = contienetoken(cadena_entrada, tokens_predefinidos)  # Se busca en la cadena
#aca se validan los errores encontrados
    #if tokens_encontrados:  # Se valida si hay tokens encontrados
    #    print("Se encontraron los siguientes tokens:", tokens_encontrados)  # Se muestran los tokens en la cadena
    #else:
    #    print("No se encontraron tokens en la cadena.")  # Se confirma si no se encontraron tokens

except ValueError as ve:
    #print(f"Error de entrada: {ve}") aca se mostraran los errores
    error_mensaje = str(ve)
    error_tipo = str(ve)
except Exception as e:
    #print(f"Error inesperado: {e}") aca se mostraran los errores
    error_mensaje = str(e)
    error_tipo = str(e)