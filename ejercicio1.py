from datetime import datetime, timedelta

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None and mes is None and año is None:
            hoy = datetime.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.año = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"
    
    def __add__(self, otrodato):
        if isinstance(otrodato, Fecha):
            raise TypeError("No se puede sumar dos fechas.")
        elif isinstance(otrodato, int):
            fecha = datetime(self.año, self.mes, self.dia)
            nueva_fecha = fecha + timedelta(days=otrodato)
            return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)
        else:
            raise TypeError("El operando debe ser un número entero.")
    
    def __eq__(self, otrodato):
        if isinstance(otrodato, Fecha):
            return self.dia == otrodato.dia and self.mes == otrodato.mes and self.año == otrodato.año
        return False

    def calcular_dif_fecha(self, otra_fecha):
        if not isinstance(otra_fecha, Fecha):
            raise TypeError("Debe ser una instancia de Fecha.")
        
        fecha1 = datetime(self.año, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        
        diferencia = abs((fecha2 - fecha1).days)
        return diferencia

fecha1 = Fecha(1, 1, 2022)
fecha2 = Fecha(9, 5, 2021)
print(fecha1) 
print(fecha2)  
print(fecha1.calcular_dif_fecha(fecha2))  

fecha3 = Fecha()  
print(fecha3)  

fecha4 = fecha1 + 10  
print(fecha4)  

print(fecha1 == fecha2)  
print(fecha1 == Fecha(1, 1, 2022))  

def __eq__(self, otrodato):
        if isinstance(otrodato, Fecha):
            return self.dia == otrodato.dia and self.mes == otrodato.mes and self.año == otrodato.año
        return False

def calcular_dif_fecha(self, otra_fecha):
        if not isinstance(otra_fecha, Fecha):
            raise TypeError("Debe ser una instancia de fecha.")
        
        fecha1 = datetime(self.año, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        
        diferencia = abs((fecha2 - fecha1).days)
        return diferencia

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }
    
    def __str__(self):
        return (f"Nombre: {self.datos['Nombre']}, "
                f"DNI: {self.datos['DNI']}, "
                f"Fecha de Ingreso: {self.datos['FechaIngreso']}, "
                f"Carrera: {self.datos['Carrera']}")
    
    def __eq__(self, otrodato):
        if isinstance(otrodato, Alumno):
            return self.datos["DNI"] == otrodato.datos["DNI"]
        return False
    
    def cambiar_datos(self, **kwargs):   
        for key, value in kwargs.items():
            if key in self.datos:
                self.datos[key] = value
    
    def antiguedad(self):
        fecha_actual = Fecha()
        return fecha_actual.calcular_dif_fecha(self.datos["FechaIngreso"])

fecha_ingreso = Fecha(15, 3, 2020)
alumno = Alumno("Tomatti Daniel", 29626680, fecha_ingreso, "tec universitaria de programacion")

print(alumno)  

alumno.cambiar_datos(Nombre="messi el mas grande", Carrera="diseño de goles")
print(alumno)  

print(alumno.antiguedad())

alumno2 = Alumno("Varela romina", 28854665, Fecha(9, 5, 2022), "Tecnica quimica")
print(alumno == alumno2) 

import random

class Nodo:
    def __init__(self, alumno):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def insertar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
    
    def __iter__(self):
        self.actual = self.cabeza
        return self
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            alumno = self.actual.alumno
            self.actual = self.actual.siguiente
            return alumno
    
    def lista_ejemplo(self, cantidad):
        nombres = ["mariano", "Manuela", "Pedro", "Juliana", "Lucas", "Lucía", "Carlos", "Lara"]
        carreras = ["Ingeniería", "Medicina", "Derecho", "Arquitectura", "Economía", "Informática"]
        
        for _ in range(cantidad):
            nombre = random.choice(nombres) + " " + random.choice(["Pérez", "Gómez", "Rodríguez", "López"])
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), random.randint(2015, 2023))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.insertar_al_final(alumno)

lista = ListaDoblementeEnlazada()
lista.lista_ejemplo(5)

for alumno in lista:
    print(alumno)


class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None and mes is None and año is None:
            hoy = datetime.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.año = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"
    
    def __add__(self, otrodato):
        if isinstance(otrodato, Fecha):
            raise TypeError("No se puede sumar dos fechas.")
        elif isinstance(otrodato, int):
            fecha = datetime(self.año, self.mes, self.dia)
            nueva_fecha = fecha + timedelta(days=otrodato)
            return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)
        else:
            raise TypeError("El operando debe ser un número entero.")
    
    def __eq__(self, otrodato):
        if isinstance(otrodato, Fecha):
            return self.dia == otrodato.dia and self.mes == otrodato.mes and self.año == otrodato.año
        return False

    def calcular_dif_fecha(self, otra_fecha):
        if not isinstance(otra_fecha, Fecha):
            raise TypeError("Debe ser una instancia de fecha.")
        
        fecha1 = datetime(self.año, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        
        diferencia = abs((fecha2 - fecha1).days)
        return diferencia

    def __lt__(self, otrodato):
        return datetime(self.año, self.mes, self.dia) < datetime(otrodato.año, otrodato.mes, otrodato.dia)

class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }
    
    def __str__(self):
        return (f"Nombre: {self.datos['Nombre']}, "
                f"DNI: {self.datos['DNI']}, "
                f"Fecha de Ingreso: {self.datos['FechaIngreso']}, "
                f"Carrera: {self.datos['Carrera']}")
    
    def __eq__(self, otrodato):
        if isinstance(otrodato, Alumno):
            return self.datos["DNI"] == otrodato.datos["DNI"]
        return False
    
    def cambiar_datos(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.datos:
                self.datos[key] = value
    
    def antiguedad(self):
        fecha_actual = Fecha()
        return fecha_actual.calcular_dif_fecha(self.datos["FechaIngreso"])

class Nodo:
    def __init__(self, alumno):
        self.alumno = alumno
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.cabeza = None
        self.cola = None
    
    def insertar_al_final(self, alumno):
        nuevo_nodo = Nodo(alumno)
        if self.cabeza is None:
            self.cabeza = self.cola = nuevo_nodo
        else:
            self.cola.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.cola
            self.cola = nuevo_nodo
    
    def __iter__(self):
        self.actual = self.cabeza
        return self
    
    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            alumno = self.actual.alumno
            self.actual = self.actual.siguiente
            return alumno
    
    def lista_ejemplo(self, cantidad):
        nombres = ["mariano", "Manuela", "Pedro", "Juliana", "Lucas", "Lucía", "Carlos", "Lara"]
        carreras = ["Ingeniería", "Medicina", "Derecho", "Arquitectura", "Economía", "Informática"]
        
        for _ in range(cantidad):
            nombre = random.choice(nombres) + " " + random.choice(["Pérez", "Gómez", "Rodríguez", "López"])
            dni = random.randint(10000000, 99999999)
            fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), random.randint(2015, 2023))
            carrera = random.choice(carreras)
            alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
            self.insertar_al_final(alumno)
    
    def ordenar_por_fecha_ingreso(self):
        if self.cabeza is None or self.cabeza.siguiente is None:
            return  
        
        actual = self.cabeza.siguiente
        while actual is not None:
            clave = actual.alumno
            nodo_anterior = actual.anterior
            
            while nodo_anterior is not None and nodo_anterior.alumno.datos["FechaIngreso"] > clave.datos["FechaIngreso"]:
                nodo_anterior.siguiente.alumno = nodo_anterior.alumno
                nodo_anterior = nodo_anterior.anterior
            
            if nodo_anterior is None:
                self.cabeza.alumno = clave
            else:
                nodo_anterior.siguiente.alumno = clave
            
            actual = actual.siguiente

lista = ListaDoblementeEnlazada()
lista.lista_ejemplo(5)

print("Lista antes de ordenar:")
for alumno in lista:
    print(alumno)

lista.ordenar_por_fecha_ingreso()

print("\nLista después de ordenar por fecha de ingreso:")
for alumno in lista:
    print(alumno)

import os

class Fecha:
    def __init__(self, dia=None, mes=None, año=None):
        if dia is None and mes is None and año is None:
            hoy = datetime.today()
            self.dia = hoy.day
            self.mes = hoy.month
            self.año = hoy.year
        else:
            self.dia = dia
            self.mes = mes
            self.año = año
    
    def __str__(self):
        return f"{self.dia:02d}/{self.mes:02d}/{self.año}"
    
    def __add__(self, otrodato):
        if isinstance(otrodato, Fecha):
            raise TypeError("No se puede sumar dos fechas.")
        elif isinstance(otrodato, int):
            fecha = datetime(self.año, self.mes, self.dia)
            nueva_fecha = fecha + timedelta(days=otrodato)
            return Fecha(nueva_fecha.day, nueva_fecha.month, nueva_fecha.year)
        else:
            raise TypeError("El operando debe ser un número entero.")
    
    def __eq__(self, otrodato):
        if isinstance(otrodato, Fecha):
            return self.dia == otrodato.dia and self.mes == otrodato.mes and self.año == otrodato.año
        return False

    def calcular_dif_fecha(self, otra_fecha):
        if not isinstance(otra_fecha, Fecha):
            raise TypeError("Debe ser una instancia de fecha.")
        
        fecha1 = datetime(self.año, self.mes, self.dia)
        fecha2 = datetime(otra_fecha.año, otra_fecha.mes, otra_fecha.dia)
        
        diferencia = abs((fecha2 - fecha1).days)
        return diferencia

    def __lt__(self, otrodato):
        return datetime(self.año, self.mes, self.dia) < datetime(otrodato.año, otrodato.mes, otrodato.dia)


class Alumno:
    def __init__(self, nombre, dni, fecha_ingreso, carrera):
        self.datos = {
            "Nombre": nombre,
            "DNI": dni,
            "FechaIngreso": fecha_ingreso,
            "Carrera": carrera
        }
    
    def __str__(self):
        return (f"Nombre: {self.datos['Nombre']}, "
                f"DNI: {self.datos['DNI']}, "
                f"Fecha de Ingreso: {self.datos['FechaIngreso']}, "
                f"Carrera: {self.datos['Carrera']}")
    
    def __eq__(self, otrodato):
        if isinstance(otrodato, Alumno):
            return self.datos["DNI"] == otrodato.datos["DNI"]
        return False
    
    def cambiar_datos(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.datos:
                self.datos[key] = value
    
    def antiguedad(self):
        fecha_actual = Fecha()
        return fecha_actual.calcular_dif_fecha(self.datos["FechaIngreso"])


def generar_lista_alumnos(cantidad):
    nombres = ["mariano", "Manuela", "Pedro", "Juliana", "Lucas", "Lucía", "Carlos", "Lara"]
    carreras = ["Ingeniería", "Medicina", "Derecho", "Arquitectura", "Economía", "Informática"]
    lista_alumnos = []
    
    for _ in range(cantidad):
        nombre = random.choice(nombres) + " " + random.choice(["Pérez", "Gómez", "Rodríguez", "López"])
        dni = random.randint(10000000, 99999999)
        fecha_ingreso = Fecha(random.randint(1, 28), random.randint(1, 12), random.randint(2015, 2023))
        carrera = random.choice(carreras)
        alumno = Alumno(nombre, dni, fecha_ingreso, carrera)
        lista_alumnos.append(alumno)
    
    return lista_alumnos


def guardar_lista_alumnos_en_archivo(ruta_directorio, nombre_archivo, lista_alumnos):
    try:
        if not os.path.exists(ruta_directorio):
            os.makedirs(ruta_directorio)
        
        ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
        
        with open(ruta_archivo, 'w') as archivo:
            for alumno in lista_alumnos:
                archivo.write(str(alumno) + '\n')
        
        print(f"Archivo {nombre_archivo} guardado en {ruta_directorio}")
        return ruta_archivo
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")


def mover_directorio(ruta_origen, ruta_destino):
    try:
        if not os.path.exists(ruta_destino):
            os.makedirs(ruta_destino)
        
        nuevo_path = os.path.join(ruta_destino, os.path.basename(ruta_origen))
        os.rename(ruta_origen, nuevo_path)
        
        print(f"Directorio movido a {nuevo_path}")
        return nuevo_path
    except Exception as e:
        print(f"Error al mover el directorio: {e}")


def borrar_archivo_y_directorio(ruta_archivo, ruta_directorio):
    try:
        if os.path.exists(ruta_archivo):
            os.remove(ruta_archivo)
            print(f"Archivo {ruta_archivo} eliminado")
        
        if os.path.exists(ruta_directorio):
            os.rmdir(ruta_directorio)
            print(f"Directorio {ruta_directorio} eliminado")
    except Exception as e:
        print(f"Error al eliminar el archivo o directorio: {e}")

lista_alumnos = generar_lista_alumnos(5)
ruta_directorio = "./directorio_alumnos"
nombre_archivo = "lista_alumnos.txt"

ruta_archivo = guardar_lista_alumnos_en_archivo(ruta_directorio, nombre_archivo, lista_alumnos)

nueva_ruta_directorio = "./nuevo_directorio_alumnos"
nueva_ruta_completa = mover_directorio(ruta_directorio, nueva_ruta_directorio)

if nueva_ruta_completa:
    nuevo_ruta_archivo = os.path.join(nueva_ruta_completa, nombre_archivo)
    borrar_archivo_y_directorio(nuevo_ruta_archivo, nueva_ruta_completa)

