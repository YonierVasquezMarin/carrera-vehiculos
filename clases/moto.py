from clases.vehiculo import Vehiculo


class Moto(Vehiculo):
    def __init__(self, velocidadMaxima, capacidadCombustible):
        super().__init__(velocidadMaxima, capacidadCombustible)

    def acelerar(self, distancia):
        super().acelerar(distancia+20)

    def frenar(self, distancia):
        super().frenar(distancia-10)
