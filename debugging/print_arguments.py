#!/usr/bin/python3
import sys

if len(sys.argv) < 2:
    print("Veuillez fournir au moins un argument.")
    sys.exit(1)

args = sys.argv[1:]
for arg in args:
    print(arg)

