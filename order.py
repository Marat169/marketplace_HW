from product import Product


class Order:
    _total_orders = 0
    _total_revenue = 0
    
    def __init__(self, products: list[Product]):
        self.products = products
        self.total_price = sum(product.price for product in products)
        Order._total_orders += 1
        Order._total_revenue += self.total_price
        
    @classmethod
    def total_orders(cls):
        return cls._total_orders
    
    @classmethod
    def total_revenue(cls):
        return cls._total_revenue
    
    def __str__(self):
        return f"Order(total_price={self.total_price}, items={len(self.products)})"
    
    def __repr__(self):
        return f"Order({self.total_price!r}, {len(self.products)} items)"
    