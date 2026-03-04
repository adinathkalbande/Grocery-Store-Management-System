from product import Product
class DailyProduct(Product):
    def __init__(self, pid, pname, cat, quantity, unit, price):
        super().__init__(pid, pname, cat, quantity, unit, price)

    def calculateGst(self):
        gst_rate = 0.18
        gst_amount = (self.price*gst_rate)
        return gst_amount
    
# s1 = DailyProduct(101, 'Brush', 'Staple', 20, 'kg', 30)
# print(s1.calculateGst())
