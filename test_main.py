import main


class TestMultiplication:
    def test_multiplication(self):
        assert {'total': 100} == main.multiply(10, 10)
