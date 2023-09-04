def turbo(func):
    def decorador(self, distancia):
        return func(self, distancia + 7)
    return decorador


