class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def set_numerator(self, numerator):
        self.numerator = numerator

    def set_denominator(self, denominator):
        self.denominator = denominator

    def add(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator + other.numerator, self.denominator)

    def sub(self, other):
        if self.denominator == other.denominator:
            return Fraction(self.numerator - other.numerator, self.denominator)

    def __str__(self):
        return "{}/{}".format(self.numerator, self.denominator)

f1 = Fraction(3, 5)

print(f1)