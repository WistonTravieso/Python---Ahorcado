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
            if letter in self.guessed_letters:
                display_word.append(letter)
            else:
                display_word.append('_')

        print(f"Palabra: {' '.join(display_word)}")
        print(f"Letras adivinadas: {', '.join(self.guessed_letters)}")
        print(f"Errores: {self.errors}/{self.max_errors}")
