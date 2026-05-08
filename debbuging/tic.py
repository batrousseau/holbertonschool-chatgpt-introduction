#!/usr/bin/python3

def print_board(board):
	"""
	Affiche la grille du morpion dans le terminal avec un formatage visuel.

	Args:
		board (list of lists): Une matrice 3x3 représentant l'état actuel de la grille.
							   Les cases vides contiennent " ", et les cases jouées "X" ou "O".
	"""
	for i, row in enumerate(board):
		print(" | ".join(row))
		# On n'affiche pas la ligne de séparation après la dernière ligne
		if i < 2:
			print("-" * 9)

def check_winner(board):
	"""
	Vérifie si l'un des joueurs a aligné 3 symboles identiques (ligne, colonne ou diagonale).

	Args:
		board (list of lists): La matrice 3x3 du jeu actuel.

	Returns:
		bool: True si un joueur a gagné, False sinon.
	"""
	# Lignes
	for row in board:
		if row.count(row[0]) == len(row) and row[0] != " ":
			return True

	# Colonnes
	for col in range(len(board[0])):
		if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
			return True

	# Diagonales
	if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
		return True
	if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
		return True

	return False

def is_board_full(board):
	"""
	Vérifie si toutes les cases de la grille ont été jouées (pour détecter une égalité).

	Args:
		board (list of lists): La matrice 3x3 du jeu actuel.

	Returns:
		bool: True si la grille est pleine, False s'il reste au moins une case vide.
	"""
	for row in board:
		if " " in row:
			return False
	return True

def tic_tac_toe():
	"""
	Gère la boucle principale du jeu de Morpion.
	
	Cette fonction initialise la grille, gère les tours des joueurs à tour de rôle,
	sécurise les entrées utilisateur (gestion des erreurs) et détermine la fin 
	de la partie (victoire d'un joueur ou match nul).
	"""
	board = [[" "]*3 for _ in range(3)]
	player = "X"
	
	while True:
		print_board(board)
		
		try:
			row = int(input(f"Enter row (0, 1, or 2) for player {player}: "))
			col = int(input(f"Enter column (0, 1, or 2) for player {player}: "))
		except ValueError:
			print("\nErreur : Entrée invalide ! Veuillez entrer un nombre (0, 1 ou 2).")
			continue
			
		if not (0 <= row <= 2 and 0 <= col <= 2):
			print("\nErreur : Coordonnées hors limites ! Veuillez entrer 0, 1 ou 2.")
			continue

		if board[row][col] == " ":
			board[row][col] = player
			
			if check_winner(board):
				print_board(board)
				print(f"\nPlayer {player} wins!")
				break
				
			if is_board_full(board):
				print_board(board)
				print("\nIt's a tie! (Match nul)")
				break
			
			player = "O" if player == "X" else "X"
			print() 
			
		else:
			print("\nThat spot is already taken! Try again.")

if __name__ == "__main__":
	tic_tac_toe()