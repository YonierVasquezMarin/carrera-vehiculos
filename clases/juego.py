from clases.moto import Moto
from clases.coche import Coche
from clases.camion import Camion
import random


class Juego:
    __vehiculos = []

    def iniciar(self):
        self.__iniciarVehiculos()
        self.__acelerarVehiculos()
        self.__mostrarEstadisticasVehiculos()
        self.__mostrarGanador()

    def __iniciarVehiculos(self):
        self.__vehiculos.append(Coche(200, 100))
        self.__vehiculos.append(Moto(150, 50))
        self.__vehiculos.append(Camion(100, 200))
        self.__vehiculos.append(Coche(250, 150))
        self.__vehiculos.append(Moto(200, 100))
        self.__vehiculos.append(Camion(150, 50))

    def __acelerarVehiculos(self):
        for vehiculo in self.__vehiculos:
            velocidadAleatoria = random.randint(10, 50)
            vehiculo.acelerar(velocidadAleatoria)

    def __mostrarEstadisticasVehiculos(self):
        for vehiculo in self.__vehiculos:
            vehiculo.mostrarEstadisticaDeRecorrido()

    def __mostrarGanador(self):
        vehiculoGanador = self.__vehiculos[0]
        for vehiculo in self.__vehiculos:
            if vehiculo.obtenerDistanciaRecorrida() > vehiculoGanador.obtenerDistanciaRecorrida():
                vehiculoGanador = vehiculo
        print("El vehiculo ganador es: ", vehiculoGanador.__class__.__name__)
