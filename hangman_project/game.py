#!/usr/bin/env python3
"""Contiene la lógica del juego."""


class HangmanGame:
    """Representa el estado de una partida."""

    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Muestra el progreso actual del jugador."""
        display_word = []

        for letter in self.word:
            if not letter.isalpha() or letter in self.guessed_letters:
                display_word.append(letter)
            else:
                display_word.append('_')

        print(f"Palabra: {' '.join(display_word)}")
        print(f"Letras adivinadas: {', '.join(self.guessed_letters)}")
        print(f"Intentos restantes: {self.max_errors - self.errors}")

    def process_guess(self, letter):
        """Procesa una letra ingresada por el jugador."""
        self.guessed_letters.append(letter)

        if letter in self.word:
            return True
        else:
            self.errors += 1
            return False

    def is_won(self):
        """Comprueba si se adivinaron todas las letras."""
        return all(letter in self.guessed_letters
                   for letter in self.word if letter.isalpha())

    def is_lost(self):
        """Comprueba si se agotaron los intentos."""
        return self.errors >= self.max_errors
