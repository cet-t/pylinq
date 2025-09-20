from dataclasses import dataclass

from linq import linq


@dataclass
class Cat:
    name: str
    age: int


if __name__ == "__main__":
    cats = linq([Cat(f"Cat{i}", i) for i in range(10)])
    print("names:", cats.select(lambda c: c.name))
    print("ages:", cats.select(lambda c: c.age))
    print("even:", cats.where(lambda c: c.age % 2 == 0).select(lambda c: c.name))
