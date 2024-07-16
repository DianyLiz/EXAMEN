class Figura:
    def __init__(self):
        self.area = 0
        self.volumen = 0
        self.figura = input("Ingrese el tipo de figura: ")
        self.calcular()

    def calcular(self):
        if self.figura == "circulo":
            radio = float(input("Ingrese el radio del circulo: "))
            self.area = 3.1416 * (radio ** 2)
            self.volumen = (4 / 3) * 3.1416 * (radio ** 3)
        elif self.figura == "esfera":
            radio = float(input("Ingrese el radio de la esfera: "))
            self.area = 4 * 3.1416 * (radio ** 2)
            self.volumen = (4 / 3) * 3.1416 * (radio ** 3)
        else:
            print("Figura no encontrada.")
            return
        print(f"El area de la {self.figura} es: {self.area}")
        print(f"El volumen de la {self.figura} es: {self.volumen}")