class Product:
    def __init__ (self, name, price, quantity):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        
    def afisare_produs(self):
        print(f"Produsul {self.name} are pretul de {self.price} lei si este in cantitatea de {self.quantity} bucati")
        
    def actualizare_cantitate(self, new_quantity):
        self.quantity = new_quantity
        print (f"Noua cantitate a produsului este {new_quantity}") 
    

