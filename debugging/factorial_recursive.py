#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Appel de la fonction factorial avec l'argument passé en ligne de commande
f = factorial(int(sys.argv[1]))

# Impression du résultat
print(f)

