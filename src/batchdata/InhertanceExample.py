class calculation1:
    def sum(self,a,b):
        return a + b;
class calculation2:
    def mul(self,a,b):
        return a * b;
class child(calculation1,calculation2):
    def divide(self,a,b):
        return a / b;
d=child()
print(d.mul(2,3))
print(d.divide(2,3))
print(d.sum(2,3))
