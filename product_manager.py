from product import Product


class ProductManager:
    def __init__(self):
        self.products = []
    
    def adauga_produse(self, product):
        self.products.append(product)
        
    def afisare_produse(self):
        for product in self.products:
            product.afisare_produs() 
            
    def afiseaza_val_totala(self):
        total = 0
        for product in self.products:
            total += product.price * product.quantity
        return total