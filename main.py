from product_manager import ProductManager 

from product import Product

manager = ProductManager()

produs1 = Product("Consola", 4000, 4)
produs2 = Product("Frigider", 2500, 6)
produs3 = Product("Cuptor", 3000, 3)

manager.adauga_produse(produs1)
manager.adauga_produse(produs2)
manager.adauga_produse(produs3)


manager.elimina_produs_dupa_nume("Laptop")
manager.afisare_produse()