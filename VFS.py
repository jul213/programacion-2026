import time

class Inodo:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo  # "file" o "dir"
        self.links = 2 if tipo == "dir" else 1
        self.permisos = "rwxr-xr-x"
        self.bloques = [] # Aquí irían las direcciones físicas del disco

class Nodo:
    def __init__(self, nombre, es_directorio=True, contenido="", inodo_id=0):
        self.nombre = nombre
        self.es_directorio = es_directorio
        self.contenido = contenido
        self.hijos = {}
        self.padre = None
        self.inodo = Inodo(inodo_id, "dir" if es_directorio else "file")
        self.fecha_creacion = time.ctime()

    def obtener_tamaño(self):
        if not self.es_directorio:
            return len(self.contenido)
        return sum(hijo.obtener_tamaño() for hijo in self.hijos.values())

class SistemaArchivos:
    def __init__(self):
        self.raiz = Nodo("/", inodo_id=1)
        self.actual = self.raiz
        self.proximo_inodo = 2

    def mkdir(self, nombre):
        if nombre in self.actual.hijos:
            print(f"Error: '{nombre}' ya existe.")
            return
        nuevo_dir = Nodo(nombre, es_directorio=True, inodo_id=self.proximo_inodo)
        nuevo_dir.padre = self.actual
        self.actual.hijos[nombre] = nuevo_dir
        self.actual.inodo.links += 1 # Al crear un hijo, el padre gana un enlace (..)
        self.proximo_inodo += 1
        print(f"Directorio '{nombre}' creado.")

    def touch(self, nombre, texto=""):
        nuevo_archivo = Nodo(nombre, es_directorio=False, contenido=texto, inodo_id=self.proximo_inodo)
        nuevo_archivo.padre = self.actual
        self.actual.hijos[nombre] = nuevo_archivo
        self.proximo_inodo += 1
        print(f"Archivo '{nombre}' creado.")

    def ls(self):
        print(f"\nExplorando: {self.get_pwd()}")
        print(f"{'TIPO':<7} {'NOMBRE':<15} {'LINKS':<7} {'TAMAÑO'}")
        print("-" * 45)
        for nombre, nodo in self.actual.hijos.items():
            tipo = "DIR" if nodo.es_directorio else "FILE"
            links = nodo.inodo.links
            tam = nodo.obtener_tamaño()
            print(f"{tipo:<7} {nombre:<15} {links:<7} {tam} bytes")

    def cd(self, nombre):
        if nombre == "..":
            if self.actual.padre:
                self.actual = self.actual.padre
            return
        if nombre in self.actual.hijos and self.actual.hijos[nombre].es_directorio:
            self.actual = self.actual.hijos[nombre]
        else:
            print(f"Error: No se puede entrar a '{nombre}'.")

    def get_pwd(self):
        
        ruta = []
        temp = self.actual
        while temp:
            ruta.append(temp.nombre)
            temp = temp.padre
        # Invertimos la lista porque fuimos de hijo a raíz
        return "/" + "/".join(reversed(ruta)).replace("//", "/")

# --- USO DEL VFS ---
fs = SistemaArchivos()
fs.mkdir("home")
fs.cd("home")
fs.mkdir("usuario")
fs.cd("usuario")
fs.touch("notas.txt", "Aprender informatica requiere disciplina.")
fs.ls()
print(f"\nRuta actual: {fs.get_pwd()}")