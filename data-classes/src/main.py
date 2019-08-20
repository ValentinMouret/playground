import dataclasses


@dataclasses.dataclass
class MyClass:
    height: int
    weight: int
    bmi: int = dataclasses.field(init=False)

    def __post_init__(self):
        self.bmi = self.weight / (self.height ** 2)


@dataclasses.dataclass
class MyChildClass(MyClass):
    name: str


def main():
    me = MyClass(1.8, 70)
    print(me)

    print(MyClass(**{"height": 1.8, "weight": 70}))

    child = MyChildClass(name="max", height=180, weight=70)
    print(child)


if __name__ == "__main__":
    main()
