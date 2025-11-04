class Calculator:

    def add(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return a + b

    def subtract(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return a - b

    def multiply(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return a * b

    def divide(self, a: float, b: float) -> float:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b

    def power(self, base: float, exponent: float) -> float:
        if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
            raise ValueError("Оба аргумента должны быть числами")
        return base ** exponent

    def is_even(self, number: int) -> bool:
        if not isinstance(number, int):
            raise ValueError("Аргумент должен быть целым числом")
        return number % 2 == 0