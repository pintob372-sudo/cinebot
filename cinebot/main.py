import json
from modelos.peliculas import Pelicula

def cargar_peliculas():
    with open("datos/peliculas.json", "r", encoding="utf-8") as archivos:
        datos = json.load(archivos)
        peliculas = []
        for pelicula_data in datos:
            pelicula = Pelicula(
                id=pelicula_data['id'],
                titulo=pelicula_data['titulo'],
                genero=pelicula_data['genero'],
                rating=pelicula_data['rating'],
                anio=pelicula_data['anio'],
                director=pelicula_data['director']
            )
            peliculas.append(pelicula)
        return peliculas

def mostar_menu():
    print("\n==================================================")
    print("Bienvenido al sistema de gestión de películas")
    print("==================================================")
    print("1. Buscar película por título")
    print("2. Mostrar todas las películas")
    print("3. Filtrar películas por género")
    print("0. Salir")
    print("--------------------------------------------------")

def main():
    peliculas = cargar_peliculas()
    print(f"Se han cargado {len(peliculas)} películas desde el archivo JSON.")

    while True:
        mostar_menu()
        op = input("Opción: ")

        if op == "1":
            text = input("Titulo buscar: ").lower()
            encontrados = [p for p in peliculas if text in p.titulo.lower()]
            if encontrados:
                for p in encontrados: print(f" -> {p}")
            else:
                print("No se encontraron películas con ese título.")

        elif op == "2":
            print("\n--- LISTADO COMPLETO ---")
            for p in peliculas: print(p)

        elif op == "3":
            genero = input("Ingrese el género a filtrar: ").lower()
            encontradas = [p for p in peliculas if p.genero.lower() == genero]
            if encontradas:
                print(f"\n--- PELÍCULAS DEL GÉNERO '{genero}' ---")
                for p in encontradas: print(p)
            else:
                print(f"No se encontraron películas del género '{genero}'.")

        elif op == "0":
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()