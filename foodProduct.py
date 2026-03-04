from product import Product
class FoodProduct(Product):
    def __init__(self, pid, pname, cat, quantity, unit, price):
        super().__init__(pid, pname, cat, quantity, unit, price)

    def calculateGst(self):
        gst_rate = 0.12
        gst_amount = (self.price*gst_rate)
        # final_price = self.price+gst_amount
        return gst_amount