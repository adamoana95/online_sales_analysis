from product import Product

class Cart:
    def __init__(self):
        self.cart_items = []

    def adauga_produs(self, product):
        self.cart_items.append(product)
        print(f"Produsul {product.name} a fost adaugat in cos.")

    def valoare_totala(self):
        total = 0
        for product in self.cart_items:
            total += product.price * product.quantity
        return total

    def afisare_cos(self):
        if not self.cart_items:
            print("Cosul este gol.")
            return

        print("Produse in cos:")
        for product in self.cart_items:
            product.afisare_produs()