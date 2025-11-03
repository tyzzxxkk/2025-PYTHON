class StockError(Exception): #재고와 관련된 예외
    pass

class PriceError(Exception): #가격과 관련된 예외
    pass

class Product:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise PriceError("가격은 음수가 될 수 없음")
        if quantity < 0:
            raise StockError("재고 수량은 음수가 될 수 없음")

        self.name = name
        self.price = price
        self.quantity = quantity

    def set_price(self, price):
        if price < 0:
            raise PriceError("가격은 음수가 될 수 없음")
        self.price = price

    def add_stock(self, amount):
        if amount <= 0:
            raise StockError("추가할 재고 수량은 0보다 커야함")
        self.quantity += amount

    def remove_stock(self, amount):
        if amount <= 0:
            raise StockError("제거할 재고 수량은 0보다 커야함")
        if self.quantity < amount:
            raise StockError("재고가 부족함")
        self.quantity -= amount

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"상품명: {self.name}, 가격: {self.price}원, 재고: {self.quantity}개"

try:
    p1 = Product("노트북", 1500000, 10)
    print(p1)

    p1.set_price(1600000)
    print("가격 변경 후 :", p1)

    p1.add_stock(5)
    print("재고 추가 후 :", p1)

    p1.remove_stock(3)
    print("재고 감소 후 :", p1)

    print("총 재고 가치 :", p1.total_value(), "원")

except (StockError, PriceError) as e:
    print("에러 발생 :", e)