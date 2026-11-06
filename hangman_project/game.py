#!/usr/bin/env python3
"""Contiene la lógica del juego."""


class HangmanGame:
    """Representa el estado de una partida."""

    def __init__(self, word):
        self.word = word.lower()
        self.guessed_letters = []
        self.ingressed_letters = set()
        self.max_errors = 6
        self.errors = 0

    def process_guess(self, letter):
        """Procesa la letra ingresada por el jugador."""

        self.ingressed_letters.add(letter)

        if letter in self.word:
            print(f"¡Correcto! La letra {letter} está en la palabra.")
            self.guessed_letters.append(letter)

        else:
            self.errors += 1
            print(f"Incorrecto. La letra {letter} no está en la palabra.")

    def display_progress(self):
        """Muestra el progreso actual del jugador."""
        display_word = []

        for letter in self.word:
            if letter in self.guessed_letters:
                display_word.append(letter)
            else:
                display_word.append('_')

        print(f"Palabra: {' '.join(display_word)}")
        print(f"Letras ingresadas: {', '.join(self.ingressed_letters)}")
        print(f"Errores: {self.errors}/{self.max_errors}")
        print(f"Palabra: {self.word}")

    def is_won(self):
        """Verifica si el jugador ha ganado."""
        return all(letter in self.guessed_letters for letter in self.word)

    def is_lost(self):
        """Verifica si el jugador ha perdido."""
        return self.errors >= self.max_errors
