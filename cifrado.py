def cifrar_mensaje(mensaje, llave):
    resultado = ""
    for caracter in mensaje:
        valor_original = ord(caracter)

        valor_cifrado = valor_original ^ llave

        resultado += chr(valor_cifrado) 
    return resultado

LLAVE_SECRETA = 157 
mensaje_original = "SISTEMA OPERATIVO COMPROMETIDO"


encriptado = cifrar_mensaje(mensaje_original, LLAVE_SECRETA)
print(f"Mensaje Cifrado (Basura para espías): {encriptado}")

# Desciframos (Usando la misma lógica)
desencriptado = cifrar_mensaje(encriptado, LLAVE_SECRETA)
print(f"Mensaje Recuperado: {desencriptado}")