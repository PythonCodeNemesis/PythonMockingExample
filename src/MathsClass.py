from decimal import DivisionByZero

class Maths_class:
    def maths_function_internal(self, x):
        return (x-5)
    def maths_function(self, x):
        try:
            y = 4/self.maths_function_internal(x)
            y = y**2
            return y
        except Exception as e:
            print(e)
            raise e

obj1 = Maths_class()
print(obj1.maths_function(x=10)) #divby0

obj1 = Maths_class()
print(obj1.maths_function(x=5))
        