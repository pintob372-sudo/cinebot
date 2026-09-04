class Pelicula:
    def __init__(self, id, titulo, genero, rating, anio, director):
        self._id = id
        self._titulo = titulo
        self._genero = genero
        self._rating = rating
        self._anio = anio
        self._director = director

    @property
    def titulo(self):
        return self._titulo

    @property
    def genero(self):
        return self._genero

    @property
    def rating(self):
        return self._rating

    def __repr__(self):
        return f"{self.titulo} ({self._anio})- {self._genero} - {self._rating}/10 - Dirigida por {self._director}"