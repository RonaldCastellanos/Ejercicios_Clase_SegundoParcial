import os 
os.system('cls' if os.name == 'nt' else 'clear')

class Aritmeticas:

    def __init__(self,a,b):

        self.a=a
        self.b=b

#suma
def suma(self):
   print( self.a+self.b)
def potencia (self,a,b):
    print( a**b)

op=Aritmeticas(int(input("a:")),int(input("b:")))
op.suma()
op.potencia (5,5)


