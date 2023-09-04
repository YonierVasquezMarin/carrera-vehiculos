class Vehiculo:
    __velocidadMaxima = 0
    __distanciaRecorrida = 0
    __capacidadCombustible = 0

    def __init__(self, velocidadMaxima, capacidadCombustible):
        self.__velocidadMaxima = velocidadMaxima
        self.__capacidadCombustible = capacidadCombustible

    def acelerar(self, distancia):
        if (distancia <= self.__velocidadMaxima):
            self.__distanciaRecorrida += distancia

    def frenar(self, distancia):
        if (distancia <= self.__distanciaRecorrida):
            self.__distanciaRecorrida -= distancia

    def obtenerDistanciaRecorrida(self):
        return self.__distanciaRecorrida

    def mostrarEstadisticaDeRecorrido(self):
        print("Distancia recorrida: ", self.__class__.__name__,
              self.__distanciaRecorrida)
