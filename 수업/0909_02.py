class StockError(Exception): pass
class PriceError(Exception): pass

class ProductNotFoundError(Exception):
    pass

class Product:
    def __init__(self, name, price, quantity):
        if price < 0:
            raise PriceError("가격은 음수가 될 수 없습니다.")
        if quantity < 0:
            raise StockError("재고 수량은 음수가 될 수 없습니다.")
        self.name, self.price, self.quantity = name, price, quantity

    def set_price(self, price):
        if price < 0:
            raise PriceError("가격은 음수가 될 수 없습니다.")
        self.price = price

    def add_stock(self, amount):
        if amount <= 0:
            raise StockError("추가할 재고 수량은 0보다 커야 합니다.")
        self.quantity += amount

    def remove_stock(self, amount):
        if amount <= 0:
            raise StockError("제거할 재고 수량은 0보다 커야 합니다.")
        if amount > self.quantity:
            raise StockError("재고가 부족합니다.")
        self.quantity -= amount

    def total_value(self):
        return self.price * self.quantity
    def __str__(self):
        return f"상품명: {self.name}, 가격: {self.price}원, 재고: {self.quantity}개"

class Inventory:
    def __init__(self):
        self.products = {}  # key: 상품명(str), value: Product 객체

    def add_product(self, product: Product):
        if product.name in self.products:
            self.products[product.name].add_stock(product.quantity)
        else:
            self.products[product.name] = product

    def remove_product(self, name: str, amount: int):
        if name not in self.products:
            raise ProductNotFoundError(f"{name} 상품이 창고에 없습니다.")
        product = self.products[name]
        product.remove_stock(amount)
        if product.quantity == 0:
            del self.products[name]

    def set_price(self, name: str, new_price: int):
        if name not in self.products:
            raise ProductNotFoundError(f"{name} 상품이 창고에 없습니다.")
        self.products[name].set_price(new_price)

    def get(self, name: str) -> Product:
        if name not in self.products:
            raise ProductNotFoundError(f"{name} 상품이 창고에 없습니다.")
        return self.products[name]

    def total_inventory_value(self):
        return sum(p.total_value() for p in self.products.values())

    def __str__(self):
        if not self.products:
            return "창고가 비어 있습니다."
        return "\n".join(str(p) for p in self.products.values())

try:
    inv = Inventory()
    inv.add_product(Product("노트북", 1500000, 5))
    inv.add_product(Product("마우스", 30000, 20))
    inv.add_product(Product("노트북", 1500000, 3))  # 같은 이름 → 재고만 증가
    print(inv)

    inv.set_price("마우스", 35000)
    print("\n가격 변경 후:\n", inv)

    inv.remove_product("노트북", 8)  # 재고 모두 소진 → 창고에서 삭제
    print("\n노트북 제거 후:\n", inv)

    print("\n창고 총 가치:", inv.total_inventory_value(), "원")

except (ProductNotFoundError, StockError, PriceError) as e:
    print("에러 발생:", e)