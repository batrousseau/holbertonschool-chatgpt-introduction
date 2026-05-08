#!/usr/bin/python3
import random
import os

def clear_screen():
	# Nettoie la console selon le système d'exploitation (Windows vs Linux/Mac)
	os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
	def __init__(self, width=10, height=10, mines=10):
		self.width = width
		self.height = height
		# Stockage de la position des mines sous forme d'indices (1D) dans un set pour la rapidité
		self.mines = set(random.sample(range(width * height), mines))
		self.field = [[' ' for _ in range(width)] for _ in range(height)]
		self.revealed = [[False for _ in range(width)] for _ in range(height)]

	def print_board(self, reveal=False):
		clear_screen()
		print('  ' + ' '.join(str(i) for i in range(self.width)))
		for y in range(self.height):
			print(y, end=' ')
			for x in range(self.width):
				# Si la partie est finie (reveal=True) ou que la case a été jouée
				if reveal or self.revealed[y][x]:
					if (y * self.width + x) in self.mines:
						print('*', end=' ')
					else:
						count = self.count_mines_nearby(x, y)
						print(count if count > 0 else ' ', end=' ')
				else:
					print('.', end=' ')
			print()

	def count_mines_nearby(self, x, y):
		count = 0
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				nx, ny = x + dx, y + dy
				if 0 <= nx < self.width and 0 <= ny < self.height:
					if (ny * self.width + nx) in self.mines:
						count += 1
		return count

	def reveal(self, x, y):
		# Si on tombe sur une mine, on renvoie False (défaite)
		if (y * self.width + x) in self.mines:
			return False
			
		self.revealed[y][x] = True
		
		# Si aucune mine autour, on révèle récursivement les cases adjacentes
		if self.count_mines_nearby(x, y) == 0:
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					nx, ny = x + dx, y + dy
					if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
						self.reveal(nx, ny)
		return True

	def check_win(self):
		# Vérifie si chaque case qui n'est pas une mine a bien été révélée
		for y in range(self.height):
			for x in range(self.width):
				if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
					return False
		return True

	def play(self):
		while True:
			self.print_board()
			try:
				x = int(input(f"Enter x coordinate (0-{self.width - 1}): "))
				y = int(input(f"Enter y coordinate (0-{self.height - 1}): "))
				
				# Vérification des limites de la grille (Sécurité)
				if not (0 <= x < self.width and 0 <= y < self.height):
					print("Coordinates out of bounds! Press Enter to try again.")
					input() # Met le jeu en pause pour laisser le temps de lire le message
					continue

				# Révèle la case. Si c'est une mine (False), c'est perdu !
				if not self.reveal(x, y):
					self.print_board(reveal=True)
					print("Game Over! You hit a mine.")
					break
				
				# Vérifie si le joueur a gagné après cette action
				if self.check_win():
					self.print_board(reveal=True)
					print("Congratulations! You cleared the minefield!")
					break

			except ValueError:
				print("Invalid input. Please enter numbers only. Press Enter to continue.")
				input()

# Point d'entrée correct du programme
if __name__ == "__main__":
	game = Minesweeper()
	game.play()