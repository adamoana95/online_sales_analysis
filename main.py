from product_manager import ProductManager 

from product import Product

manager = ProductManager()

produs1 = Product("Laptop", 4000, 4)
produs2 = Product("TV", 2500, 6)
produs3 = Product("PC", 3000, 3)

manager.adauga_produse(produs1)
manager.adauga_produse(produs2)
manager.adauga_produse(produs3)

manager.afisare_produse()
valoarea_totala = manager.afiseaza_val_totala()
print(f"Valoarea totala a inventarului este {valoarea_totala} lei")

manager.elimina_produs_dupa_nume("Laptop")
manager.afisare_produse()