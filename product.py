class Product:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
        
    def __str__(self):
        return f"Product(name={self.name}, price={self.price})"
    
    def __repr__(self):
        return f"Product({self.name!r}, {self.price!r})"
    
    def __eq__(self, other):
        return isinstance(other, Product) and self.price == other.price
    
    def __lt__(self, other):
        return isinstance(other, Product) and self.price < other.price
    
