import random

class Entrenador:
    def __init__(self, nombre):
        self.nombre = nombre

class Pokemon:
    def __init__(self, nombre):
        self.nombre = nombre
        self.max_ataque = random.randint(20, 100)
        self.vida_maxima = random.randint(150, 400)
        self.vida_actual = self.vida_maxima

    def recuperar(self):
        self.vida_actual = self.vida_maxima

def crearEntrenadorPokemon(numero):
    print(f"\nCreando entrenador {numero}")
    nombre_entrenador = input("Nombre del entrenador: ")
    nombre_pokemon = input("Nombre del Pokemon: ")

    entrenador = Entrenador(nombre_entrenador)
    pokemon = Pokemon(nombre_pokemon)

    if numero == 2:
        print(f"\nEstadisticas de {pokemon.nombre}:")
        print(f"Ataque maximo: {pokemon.max_ataque}")
        print(f"Vida maxima: {pokemon.vida_maxima}")

    return entrenador, pokemon

def valorDeAtaque(pokemon):
    return random.randint(0, pokemon.max_ataque)

def defender(pokemon, ataque):
    dado = random.randint(1, 6)
    if dado == 6:
        ataque = 0

    pokemon.vida_actual = pokemon.vida_actual - ataque
    return pokemon.vida_actual

entrenador1, pokemon1 = crearEntrenadorPokemon(1)
ganadas = 0
perdidas = 0

while True:
    print("\n\tMENU")
    print("P) Pelear")
    print("F) Finalizar")

    opcion = input("Elige una opcion: ").upper()

    if opcion == "P":
        pokemon1.recuperar()
        entrenador2, pokemon2 = crearEntrenadorPokemon(2)

        while True:
            print(f"\n{entrenador1.nombre} ataca con {pokemon1.nombre}")
            ataque1 = valorDeAtaque(pokemon1)
            vida2 = defender(pokemon2, ataque1)
            print(f"{pokemon2.nombre} tiene {vida2} de vida")

            if vida2 <= 0:
                print(f"\nGanaste {entrenador1.nombre} y {pokemon1.nombre} son los ganadores")
                ganadas = ganadas + 1
                break

            print(f"\n{entrenador2.nombre} ataca con {pokemon2.nombre}")
            ataque2 = valorDeAtaque(pokemon2)
            vida1 = defender(pokemon1, ataque2)
            print(f"{pokemon1.nombre} tiene {vida1} de vida")

            if vida1 <= 0:
                print(f"\nPerdiste {entrenador2.nombre} y {pokemon2.nombre} son los ganadores")
                perdidas = perdidas + 1
                break

    elif opcion == "F":
        print("\n\tEstadisticas")
        print(f"Entrenador: {entrenador1.nombre}")
        print(f"Pokemon: {pokemon1.nombre}")
        print(f"Ataque maximo: {pokemon1.max_ataque}")
        print(f"Vida maxima: {pokemon1.vida_maxima}")
        print(f"Encuentros ganados: {ganadas}")
        print(f"Encuentros perdidos: {perdidas}")
        break

    else:
        print("opcion invalida, intenta de nuevo")