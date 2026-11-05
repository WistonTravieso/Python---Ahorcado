#!/usr/bin/env python3
""" Funciones auxiliares como validar la entrada o mostrar el estado actual."""

import random

def get_random_word():
    """Devuelve una palabra aleatoria de la lista de palabras."""
    with open("wordlist.txt", "r") as file:
        words = file.readlines()
        return random.choice(words).strip()

get_random_word()

