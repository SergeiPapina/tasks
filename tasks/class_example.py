
class Exchange_rate:
    @property
    def exchange_rate(self):
        return self._exchange_rate

    @exchange_rate.setter
    def exchange_rate(self, exchange_rate):
        self._exchange_rate = exchange_rate

    @exchange_rate.deleter
    def exchange_rate(self):
        print("attribute exchange_rate deleted")
        del self._exchange_rate

class Money(Exchange_rate, cl2, cl3):
    _list_unit = ['usd', 'eur', 'byr', 'rur']

    def __init__(self, value, unit):
        self._value = value
        self._unit = unit
        self._exchange_rate = 1.13

    # @property
    # def value(self):
    #     return self._value

    # @value.setter
    # def value(self, value):
    #     if value >= 0:
    #         self._value = value
    #     else:
    #         raise ValueError("Value must be positive")

    # @property
    # def unit(self):
    #     return self._unit

    # @unit.setter
    # def unit(self, unit):
    #     if unit in self._list_unit:
    #         self._unit = unit
    #     else:
    #         raise ValueError(f"Value must be from {self._list_unit}")



    @classmethod
    def one_dollar(cls):
        return cls(1, 'usd')

    @classmethod
    def one_euro(cls):
        return cls(1, 'eur')

    def out_value(self):
        print(self._value)

    def __str__(self):
        return f'result in {self._unit}: {self._value}'

    def __add__(self, other):
        if self._unit == other._unit:
            return Money(self._value + other._value, self._unit)
        else:
            return Money(self._value + other._value * other.exchange_rate, self._unit)



a = Money(20, 'usd')
b = Money(30, 'usd')
c = Money(10, 'eur')

res_d = a+b
res_d.out_value()

c.exchange_rate = 1.13

res_de = a+c
res_de.out_value()

dollar = Money.one_dollar()
euro = Money.one_euro()
euro.exchange_rate = 1.13

res = dollar + euro
res.out_value()

print(Money(1700, 'usd') + Money(300, 'eur'))

del res.exchange_rate
