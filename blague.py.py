import tkinter as tk
import random
import time

# Liste de messages effrayants mais inoffensifs
messages = [
    "Alerte ! Virus détecté!",
    "Fichiers corrompus. Impossible de les récupérer.",
    "Impossible d'arrêter le processus. Tentative de suppression du programme.",
    "Erreur fatale du système. Veuillez redémarrer immédiatement.",
    "Attention ! Votre ordinateur est sur le point de s'éteindre !"
]

# Fonction pour afficher un pop-up avec un message aléatoire
def show_popup(message):
    root = tk.Tk()
    root.title("Alerte Système")
    label = tk.Label(root, text=message, font=("Helvetica", 16), fg="red")
    label.pack(padx=50, pady=50)
    root.after(3000, root.destroy)  # Ferme la fenêtre après 3 secondes
    root.mainloop()

# Choisir un message aléatoire et afficher le pop-up
message = random.choice(messages)
show_popup(message)

# Attendre avant d'afficher un autre pop-up
time.sleep(1)
show_popup("Systeme redémarré. Problème critique !")
