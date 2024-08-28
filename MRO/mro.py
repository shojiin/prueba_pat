class A:
    def hablar(self):
        print("hola desde A")

class B(A):
    def hablar(self):
        print("hola desde B")
        
class C(A):
   def hablar(self):
        print("hola desde C")
        
class D(B,C):
    def hablar(self):
        print("hola desde D")

d = D()
#se puede llamar una clase de mas arriba pasandole el parametro de mas abajo
B.hablar(d)
#print(D.mro())

