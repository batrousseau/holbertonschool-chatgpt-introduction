class Checkbook:
	"""
	Représente un carnet de chèques (compte bancaire) basique.
	Permet d'effectuer des dépôts, des retraits et de consulter le solde.
	"""
	
	def __init__(self):
		"""Initialise le carnet de chèques avec un solde à zéro."""
		self.balance = 0.0

	def deposit(self, amount):
		"""
		Dépose un montant sur le compte.

		Args:
			amount (float): Le montant à déposer. Doit être strictement positif.
		"""
		# Gestion du cas limite : Dépôt d'un montant négatif ou nul
		if amount <= 0:
			print("Erreur : Le montant du dépôt doit être supérieur à zéro.")
			return

		self.balance += amount
		print("Déposé : ${:.2f}".format(amount))
		print("Solde actuel : ${:.2f}".format(self.balance))

	def withdraw(self, amount):
		"""
		Retire un montant du compte si les fonds sont suffisants.

		Args:
			amount (float): Le montant à retirer. Doit être strictement positif.
		"""
		# Gestion du cas limite : Retrait d'un montant négatif ou nul
		if amount <= 0:
			print("Erreur : Le montant du retrait doit être supérieur à zéro.")
			return

		# Gestion du cas limite : Solde insuffisant
		if amount > self.balance:
			print("Fonds insuffisants pour effectuer ce retrait.")
		else:
			self.balance -= amount
			print("Retiré : ${:.2f}".format(amount))
			print("Solde actuel : ${:.2f}".format(self.balance))

	def get_balance(self):
		"""Affiche le solde actuel du compte."""
		print("Solde actuel : ${:.2f}".format(self.balance))


def main():
	"""
	Fonction principale gérant l'interface utilisateur en boucle.
	Gère les entrées de l'utilisateur et attrape les erreurs de frappe.
	"""
	cb = Checkbook()
	
	while True:
		# .strip() nettoie les espaces avant/après, .lower() gère la casse (ex: "ExiT")
		action = input("\nQue souhaitez-vous faire ? (deposit, withdraw, balance, exit) : ").strip().lower()
		
		if action == 'exit':
			print("Au revoir !")
			break
			
		elif action == 'deposit':
			try:
				# Tente de convertir l'entrée en nombre décimal
				amount = float(input("Entrez le montant à déposer : $"))
				cb.deposit(amount)
			except ValueError:
				# Gestion du cas limite : L'utilisateur a entré du texte au lieu d'un nombre
				print("Erreur : Veuillez entrer un montant numérique valide.")
				
		elif action == 'withdraw':
			try:
				amount = float(input("Entrez le montant à retirer : $"))
				cb.withdraw(amount)
			except ValueError:
				print("Erreur : Veuillez entrer un montant numérique valide.")
				
		elif action == 'balance':
			cb.get_balance()
			
		else:
			# Gestion du cas limite : Commande non reconnue
			print("Commande invalide. Veuillez réessayer.")

# Point d'entrée sécurisé du programme (corrigé avec le saut de ligne)
if __name__ == "__main__":
	main()