import saludar


class TestSaludar:

    def test_saludo1(self):
        assert "Hola Jose Francisco desde el Master de DevSecOps" == saludar.saludo1()

    def test_saludo2(self):
        assert "Buenos días mi gente del Master" == saludar.saludo2()

    def test_saludo3(self):
        assert "Hola, ¿Qué tal llevas el Master?" == saludar.saludo3()
