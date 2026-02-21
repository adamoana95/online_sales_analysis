from product_manager import ProductManager 

from product import Product

from cart import Cart

import random


manager = ProductManager()

produs1 = Product("Laptop", 4000, 4)
produs2 = Product("TV", 2500, 6)
produs3 = Product("PC", 3000, 3)
produs4 = Product("Telefon", 2000, 3)
produs5 = Product("Tastatura", 250, 7)

manager.adauga_produse(produs1)
manager.adauga_produse(produs2)
manager.adauga_produse(produs3)
manager.adauga_produse(produs4)
manager.adauga_produse(produs5)

manager.afisare_produse()
valoarea_totala = manager.afiseaza_val_totala()
print(f"Valoarea totala a inventarului este {valoarea_totala} lei")

manager.elimina_produs_dupa_nume("Laptop")
manager.afisare_produse()

cart = Cart()

produse_random = random.sample(manager.products, 3)
for produs in produse_random:
    cart.adauga_produs(produs)
    
cart.afisare_cos()

total = cart.valoare_totala()
print(f"Valoarea totala de plata: {total} lei")