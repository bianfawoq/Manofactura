class Pieza:
    def __init__(self, forma, dimension, material, diametro=None, longitud=None, largo=None, ancho=None, espesor=None):
        self.forma = forma
        self.dimension = dimension
        self.material = material
        self.diametro = diametro
        self.longitud = longitud
        self.largo = largo
        self.ancho = ancho
        self.espesor = espesor

def recomendacion_mecanizado(pieza, operacion):
    if operacion == "Torneado en torno convencional" and pieza.forma == "cilindrica":
        if pieza.material == "cobre":
            precio_kilo = 29150
        elif pieza.material == "acero 1020":
            precio_kilo = 5000
        elif pieza.material == "estaño":
            precio_kilo = 24500

        volumen = 3.14159 * (pieza.diametro / 2) ** 2 * pieza.longitud
        precio_total = volumen * precio_kilo / 1000  # Convertir a kilogramos
        return f"{operacion}\nPrecio total estimado: ${precio_total:.2f}"

    elif operacion == "Fresado en fresadora CNC" and pieza.forma == "cubica":
        if pieza.material == "cobre":
            precio_kilo = 29150
        elif pieza.material == "acero 1020":
            precio_kilo = 5000
        elif pieza.material == "estaño":
            precio_kilo = 24500

        volumen = pieza.largo * pieza.ancho * pieza.espesor
        precio_total = volumen * precio_kilo / 1000  # Convertir a kilogramos
        return f"{operacion}\nPrecio total estimado: ${precio_total:.2f}"

    return "Recomendación no disponible"

def main():
    while True:
        print("Selecciona la forma de la pieza:")
        print("1. Cilíndrica")
        print("2. Cúbica")
        forma_pieza = input("Ingresa el número de la forma (1-2): ")

        if forma_pieza not in ["1", "2"]:
            print("Opción no válida. Por favor, ingresa un número del 1 al 2.")
            continue

        dimension = float(input("Ingresa la dimensión de la pieza en milímetros: "))
        material = input("Ingresa el material de la pieza (cobre/acero 1020/estaño): ")

        if forma_pieza == "1":  # Cilíndrica
            diametro = float(input("Ingresa el diámetro de la pieza en milímetros: "))
            longitud = float(input("Ingresa la longitud de la pieza en milímetros: "))
            pieza = Pieza("cilindrica", dimension, material, diametro=diametro, longitud=longitud)
        else:  # Cúbica
            largo = float(input("Ingresa el largo de la pieza en milímetros: "))
            ancho = float(input("Ingresa el ancho de la pieza en milímetros: "))
            espesor = float(input("Ingresa el espesor de la pieza en milímetros: "))
            pieza = Pieza("cubica", dimension, material, largo=largo, ancho=ancho, espesor=espesor)

        operacion = "Torneado en torno convencional" if forma_pieza == "1" else "Fresado en fresadora CNC"
        recomendacion = recomendacion_mecanizado(pieza, operacion)
        print(f"Recomendación de mecanizado para la pieza: {recomendacion}")

        salir = input("¿Deseas salir? (s/n): ")
        if salir.lower() == "s":
            break

if __name__ == "__main__":
    main()
