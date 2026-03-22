
def revisar_luces(byte_entrada):
    print(f"Estado del sistema (Decimal: {byte_entrada}, Binario: {bin(byte_entrada)})")

    for i in range(8):
        mask = 1 << i
        

