import random
from funciones import *

"""
Inicia el juego. El jugador debe adivinar el número correcto en cada ronda.
"""

print("""
====================================================
    Bienvenido al Juego de Adivinanza en Binario
        ¡Seleccione el modo de juego!
====================================================

[B]  Adivinar binarios
    (te damos un número binario y respondés en decimal)

[D]  Adivinar decimales
    (te damos un número decimal y respondés en binario)

""")

puntaje = 0
rondas = int(input("Ingrese cuantas rondas quiere jugar: "))
rondas = numero_de_rondas(verificar_positivo(rondas))
modo_juego = input("Ingrese su modo de juego (B o D): ").upper()
for ronda in range(1, rondas + 1):
    numero = random.randint(1, 31) # Limitar entre 1 y 31
    if modo_juego == "B":
            print(f"\nRonda {ronda}")
            binario = decimal_a_binario(numero)
            respuesta = input(f"¿Cuál es el número decimal de este binario? {binario} = ")
            if respuesta.isdigit() and int(respuesta) == numero:
                print("¡Correcto!")
                puntaje += 1
            else:
                print(f"Incorrecto. La respuesta correcta era {numero}.")
    elif modo_juego == "D":
            print(f"\nRonda {ronda}")
            respuesta = input(f"¿Cuál es el número binario de este decimal? {numero} = ")
            if respuesta == decimal_a_binario(numero):
                print("¡Correcto!")
                puntaje += 1
            else:
                print(f"Incorrecto. La respuesta correcta era {decimal_a_binario(numero)}.")
print(f"\n Juego terminado. Tu puntaje final es: {puntaje} de {rondas}")