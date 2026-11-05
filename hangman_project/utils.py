#!/usr/bin/env python3
"""Funciones auxiliares del juego."""

import random


def get_random_word():
    """Devuelve una palabra aleatoria de la lista de palabras."""
    with open("wordlist.txt", "r") as file:
        words = [line.strip() for line in file
                 if line.strip().isalpha()]

    return random.choice(words)
