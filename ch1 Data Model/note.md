# ch1 Data Model

## special methods
By implementing special methods, your objects can behave like the built-in types, enabling
the expressive coding style the community considers Pythonic.

1. advantages: easy to remember methods; use rich Python standard library

2. special methods should be called by the Python interpreter

3. better to call the related built-in function: len, iter, str, etc, faster than method calls

4. If we did not implement `__repr__`, vector instances would be shown in the console like <Vector object at 0x10e100070>.

5. when no custom `__str__` is available, Python will call `__repr__` as a fallback.

6. Python offers a rich selection of numeric types, from the built-ins to decimal.Decimal and fractions.Fraction,