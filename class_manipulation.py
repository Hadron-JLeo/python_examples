class Car:
    wheels = 4  # Klassenattribut

    def __init__(self, brand: str):
        self.brand = brand

print(Car.__dict__)  # zeigt Klassenattribute

c = Car("Toyota")
print(c.__dict__)    # zeigt nur Instanzattribute → {'brand': 'Toyota'}

Car.wheels = 3
print(c.wheels, c.__dict__)      # → 3, aber immer noch kein 'wheels' in c.__dict__

c.wheels = 4         # Jetzt bekommt c ein eigenes wheels
print(c.__dict__)    # → {'brand': 'Toyota', 'wheels': 4}



### Wie entgegenwirken?
class Car2:
    __slots__ = ['brand']  # erlaubt nur das Attribut 'brand'

    def __init__(self, brand: str):
        self.brand = brand

c2 = Car2("Toyota")
c2.brand = "Honda"    # ok

c2.wheels = 4         # AttributeError!
