#!/usr/bin/env python3
"""Punto de entrada del juego del ahorcado."""

from utils import get_random_word
from game import HangmanGame

print("¡Bienvenido al juego del Ahorcado!")

def main():
    """Inicia el juego y solicita letras al jugador."""
    word = get_random_word()
    game = HangmanGame(word)

    while game.errors < game.max_errors and set(game.word) != set(game.guessed_letters):
        letter = input("Ingresa una letra: ").strip().lower()

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada inválida. Ingresa una sola letra.")

        elif letter in game.ingressed_letters:
            print("Ya ingresaste esa letra. Intenta con otra.")

        else:
            game.process_guess(letter)
            game.display_progress()
            
    if game.is_won():
        print("¡Ganaste!")
    if game.is_lost():
        print("¡Perdiste!")

if __name__ == "__main__":
    main()
