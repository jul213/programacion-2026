def cifrar_mensaje(mensaje, llave):
    resultado = ""
    for caracter in mensaje:
        valor_original = ord(caracter)

        valor_cifrado = valor_original ^ llave

        resultado += chr(valor_cifrado) 
    return resultado