class Calculator:
    def add(self, a, b):
        return a + b

    def div(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return a / b

    def mul(self, a, b):
        return a * b

    def minus(self, a, b):
        return a - b

    def power(self, a, b):
        # result = a
        # for _ in range(b - 1):

        
        #     result = result * a
        # return result
        return a ** b