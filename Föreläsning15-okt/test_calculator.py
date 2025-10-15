# Vad är TDD?
# Test Driven Development
# Skriv tester först, sedan kod som gör att testerna går igenom
# Red -> Green -> Refactor -> Repeat
# Innebär att du skriver ett test som misslyckas (rött)
# Sedan skriver du precis så mycket kod att testet går igenom (grönt)
# Slutligen refaktorerar du koden för att förbättra den (Refactor
# Och upprepar processen (repeat)

import pytest
from calculator import add, subtract, divide


def test_add_two_numbers():
    assert add(2, 3) == 5
    assert add(1, 1) == 2
    assert add(0, 0) == 0
    assert add(1, 0) == 1

def test_subtract():
    assert subtract(10, 3) == 7

def test_divide():
    assert divide(8, 2) == 4
    assert divide(5, 2) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
      

