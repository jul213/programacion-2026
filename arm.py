class MicroProcesador:
    def __init__(self):
        self.registros = {"R1": 0, "R2": 0}
        self.pc = 0 # Program Counter

    def ejecutar(self, programa):
        while self.pc < len(programa):
            instruccion = programa[self.pc].split()
            op = instruccion[0]

            if op == "SET":
                reg, val = instruccion[1], int(instruccion[2])
                self.registros[reg] = val
            elif op == "ADD":
                reg1, reg2 = instruccion[1], instruccion[2]
                self.registros[reg1] += self.registros[reg2]
            elif op == "PRN":
                print(f"SALUDA CPU: {self.registros[instruccion[1]]}")
            
            self.pc += 1 # El PC siempre avanza

# --- NUESTRO CÓDIGO "BINARIO" ---
codigo = [
    "SET R1 50",
    "SET R2 30",
    "ADD R1 R2",
    "PRN R1"
]

mi_cpu = MicroProcesador()
mi_cpu.ejecutar(codigo)