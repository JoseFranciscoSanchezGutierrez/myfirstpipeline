import calcular


class TestCalcular:

    def test_suma(self):
        num1 = 10
        num2 = 5
        resultado = num1 + num2
        assert resultado == calcular.suma(num1, num2)

    def test_resta(self):
        num1 = 10
        num2 = 5
        resultado = num1 - num2
        assert resultado == calcular.resta(num1, num2)
