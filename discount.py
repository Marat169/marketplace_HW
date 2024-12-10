class Discount:
    def __init__(self, description: str, discount_percent: float):
        self.description = description
        self.discount_percent = discount_percent
        
    @staticmethod   
    def apply_discount(price: float, discount_percent: float) -> float:
        """Метод принимает цену и вычисляет скидку"""
        return price * (1 - discount_percent / 100)
    
    def __str__(self):
        return f"Discount(description={self.description}, discount_percent={self.discount_percent})"
    
    def __repr__(self):
        return f"Discount({self.description!r}, {self.discount_percent!r})"
    
       
    