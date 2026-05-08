#!/usr/bin/python3
"""
Script permettant de calculer la factorielle d'un nombre.
Il s'exécute en ligne de commande et intègre une gestion des erreurs de saisie.
"""
import sys

def factorial(n):
	"""
	Calcule la factorielle d'un nombre entier positif.

	Args:
		n (int): Le nombre entier positif dont on veut calculer la factorielle.

	Returns:
		int: Le résultat du calcul de la factorielle.
	"""
	result = 1
	while n > 1:
		result *= n
		n -= 1
	return result

# Vérifie si un argument a bien été fourni lors de l'exécution du script
if len(sys.argv) < 2:
	print("Usage: python script.py <nombre>")
	sys.exit(1)

try:
	# Tente de convertir l'argument fourni en nombre entier
	number = int(sys.argv[1])

	# Les factorielles ne sont définies que pour les entiers positifs ou nuls
	if number < 0:
		print("Veuillez fournir un entier positif.")
	else:
		f = factorial(number)
		print(f"La factorielle de {number} est {f}")

except ValueError:
	# Capture l'erreur si l'utilisateur entre des lettres ou un nombre à virgule
	print("Erreur : Veuillez fournir un nombre entier valide.")