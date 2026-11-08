#!/usr/bin/env python3
"""Punto de entrada del juego del ahorcado."""

from utils import get_random_word
from game import HangmanGame


def main():
    """Inicia el juego y solicita letras al jugador."""
    word = get_random_word()
    game = HangmanGame(word)

    while True:
        letter = input("Ingresa una letra: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada inválida. Ingresa una sola letra.")

        elif letter in game.guessed_letters:
            print("Ya ingresaste esa letra. Intenta con otra.")

        else:
            if game.process_guess(letter):
                print(f"¡Correcto! La letra {letter} está en la palabra.")
            else:
                print(f"Incorrecto. La letra {letter} no está en la palabra.")

            game.display_progress()

            if game.is_won():
                print("¡Ganaste!")
                break

            elif game.is_lost():
                print("Fin del juego")
                break


if __name__ == "__main__":
    main()
