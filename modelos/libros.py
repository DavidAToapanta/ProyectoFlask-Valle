#Modelos/libros.py
class Libro:
    def __init__(self, titulo, autor, isbn):

        """"Constructor de la clase libro: aqui definimos que tipo de datos vamos a utilizar 
            para crear un libro
        """
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

    #1. Informacion desde Angular
    @classmethod
    def desde_json_angular(cls, datos_json_angular):
        
        return cls(
            titulo=datos_json_angular.get('titulo'),
            autor=datos_json_angular.get('autor'),
            isbn=datos_json_angular.get('isbn')
        )

    #2 De python a Angular

    def a_dicccionario(self):
        return {
            'titulo': self.titulo,
            'autor': self.autor,
            'isbn': self.isbn
        }

    #3
