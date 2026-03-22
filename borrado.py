import os

def triturador_forense(ruta_archivo, pasadas=3):
    if not os.path.isfile(ruta_archivo):
        print("Error: El archivo no existe.")
        return

    tamano = os.path.getsize(ruta_archivo)
    
    with open(ruta_archivo, "ba+", buffering=0) as f:
        for i in range(pasadas):
            print(f"Pasada {i+1}: Sobreescribiendo con basura aleatoria...")
            f.seek(0)
            # TRUCO: Escribimos bits aleatorios exactamente del mismo tamaño
            f.write(os.urandom(tamano))
            f.flush()
            os.fsync(f.fileno()) # Forzamos al Sistema Operativo a escribir al disco YA
            
    os.remove(ruta_archivo)
    print("¡Archivo destruido físicamente!")

# PRUEBA: Crea un archivo notas.txt y luego pásale el triturador.