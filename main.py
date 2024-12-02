import csv

# Clases Base
class Vehiculo:
    def __init__(self, marca, modelo, nro_ruedas):
        self.marca = marca
        self.modelo = modelo
        self.nro_ruedas = nro_ruedas

    def __str__(self):
        return f"Marca {self.marca}, Modelo {self.modelo}, {self.nro_ruedas} ruedas"

class Automovil(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada):
        super().__init__(marca, modelo, nro_ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        base = super().__str__()
        return f"{base} {self.velocidad} Km/h, {self.cilindrada} cc"

class Particular(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, nro_puestos):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.nro_puestos = nro_puestos

    def __str__(self):
        return f"{super().__str__()} Puestos: {self.nro_puestos}"

class Carga(Automovil):
    def __init__(self, marca, modelo, nro_ruedas, velocidad, cilindrada, carga):
        super().__init__(marca, modelo, nro_ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return f"{super().__str__()} Carga: {self.carga} Kg"

class Bicicleta(Vehiculo):
    def __init__(self, marca, modelo, nro_ruedas, tipo):
        super().__init__(marca, modelo, nro_ruedas)
        self.tipo = tipo

    def __str__(self):
        return f"{super().__str__()} Tipo: {self.tipo}"

class Motocicleta(Bicicleta):
    def __init__(self, marca, modelo, nro_ruedas, tipo, motor, cuadro, nro_radios):
        super().__init__(marca, modelo, nro_ruedas, tipo)
        self.motor = motor
        self.cuadro = cuadro
        self.nro_radios = nro_radios

    def __str__(self):
        return f"{super().__str__()} Motor: {self.motor}, Cuadro: {self.cuadro}, Nro Radios: {self.nro_radios}"

# Funciones para manejo de CSV
def guardar_datos_csv(vehiculos, nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "w", newline="") as archivo:
            writer = csv.writer(archivo)
            for vehiculo in vehiculos:
                writer.writerow([vehiculo.__class__, vehiculo.__dict__])
    except Exception as e:
        print(f"Error al guardar datos: {e}")

def leer_datos_csv(nombre_archivo="vehiculos.csv"):
    try:
        with open(nombre_archivo, "r") as archivo:
            reader = csv.reader(archivo)
            for row in reader:
                print(row)
    except Exception as e:
        print(f"Error al leer datos: {e}")

# Programa principal
if __name__ == "__main__":
    # Parte 1: Insertar Automóviles
    vehiculos = []
    cantidad = int(input("Cuantos Vehiculos desea insertar: "))

    for i in range(cantidad):
        print(f"Datos del automóvil {i + 1}")
        marca = input("Inserte la marca del automóvil: ")
        modelo = input("Inserte el modelo: ")
        nro_ruedas = int(input("Inserte el número de ruedas: "))
        velocidad = int(input("Inserte la velocidad en km/h: "))
        cilindrada = int(input("Inserte el cilindraje en cc: "))
        vehiculo = Automovil(marca, modelo, nro_ruedas, velocidad, cilindrada)
        vehiculos.append(vehiculo)

    print("\nImprimiendo por pantalla los Vehículos:")
    for i, v in enumerate(vehiculos, start=1):
        print(f"Datos del automóvil {i} : {v}")

    # Parte 2: Instancias Adicionales y Relaciones
    particular = Particular("Ford", "Fiesta", 4, "180", "500", 5)
    carga = Carga("Daft Trucks", "G 38", 10, 120, "1000", "20000")
    bicicleta = Bicicleta("Shimano", "MT Ranger", 2, "Carrera")
    motocicleta = Motocicleta("BMW", "F800s", 2, "Deportiva", "2T", "Doble Viga", 21)

    vehiculos.extend([particular, carga, bicicleta, motocicleta])

    print("\nImprimiendo nuevas instancias:")
    for vehiculo in vehiculos[-4:]:
        print(vehiculo)

    print("\nVerificación de relaciones:")
    print(f"Motocicleta es instancia con relación a Vehiculo: {isinstance(motocicleta, Vehiculo)}")
    print(f"Motocicleta es instancia con relación a Automovil: {isinstance(motocicleta, Automovil)}")
    print(f"Motocicleta es instancia con relación a Particular: {isinstance(motocicleta, Particular)}")
    print(f"Motocicleta es instancia con relación a Carga: {isinstance(motocicleta, Carga)}")
    print(f"Motocicleta es instancia con relación a Bicicleta: {isinstance(motocicleta, Bicicleta)}")
    print(f"Motocicleta es instancia con relación a Motocicleta: {isinstance(motocicleta, Motocicleta)}")

    # Parte 3: Guardar y Leer desde CSV
    guardar_datos_csv(vehiculos)
    print("\nDatos guardados en vehiculos.csv. Leyendo datos guardados:")
    leer_datos_csv()
