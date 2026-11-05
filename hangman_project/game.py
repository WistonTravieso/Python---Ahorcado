#!/usr/bin/env python3
"""Contiene la lógica del juego."""

from utils import get_random_word

class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        """Muestra el progreso actual del jugador."""
        display_word = ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
        print(f"Palabra: {display_word}")
        print(f"Letras adivinadas: {', '.join(self.guessed_letters)}")
        print(f"Errores: {self.errors}/{self.max_errors}")

game = HangmanGame(get_random_word())
game.display_progress()