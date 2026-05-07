# przykładowe funkcje utils.py
"""Moduł utils.py zawiera podstawowe funkcje matematyczne: dodawanie, odejmowanie, mnożenie i dzielenie."""
def add(a: int, b: int) -> int:
    """"Funkcja dodająca dwie liczby całkowite."""
    return a + b

def subtract(a: int, b: int) -> int:
    """Funkcja odejmująca dwie liczby całkowite."""
    return a - b

def multiply(a: int, b: int) -> int:
    """Funkcja mnożąca dwie liczby całkowite."""
    return a * b

def divide(a: int, b: int) -> float:
    """Funkcja dzieląca dwie liczby całkowite."""
    #if b == 0:
    #    raise ValueError("Cannot divide by zero")
    return a / b