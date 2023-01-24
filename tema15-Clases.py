
import os

class OperasBas:
    #declaracion de propiedades
    num1=0
    num2=0
    res=0

    #declaracion de constructor
    def __init__(self, a, b):
        self.num1=a
        self.num2=b
    
    #declaracion de metodos de clases
    def suma(self):
        self.res=self.num1+self.num2
        print("La suma es: {}".format(self.res))

    def resta(self):
        self.res=self.num1-self.num2
        print("La resta es: {}".format(self.res))

    def multi(self):
        self.res=self.num1*self.num2
        print("La multiplicacion es: {}".format(self.res))

    def division(self):
        self.res=self.num1/self.num2
        print("La division es: {}".format(self.res))
         

def main():
        
        i = 0
        while i != 5:
            print(" ")
            print("Elige una opcion: ")
            print("1.- Sumar")
            print("2.- Restar")
            print("3.- Multiplicar")
            print("4.- Dividir")
            print("5.- Salir")
            i = int(input("Dame una opcion: "))
            if i >= 5:
                print("Las operaciones finalizaron")
                break
            print(" ")
            num1 = int(input("Dame el num1: "))
            num2 = int(input("Dame el num2: "))
            obj = OperasBas(num1,num2)
            if i == 1:
                #os.system('cls')
                print(" ")
                obj.suma() 
            elif i == 2:
                #os.system('cls')
                print(" ")
                obj.resta()
            elif i == 3:
                #os.system('cls')
                print(" ")
                obj.multi()
            elif i == 4:
                #os.system('cls')
                print(" ")
                obj.division()            
            

if __name__ == "__main__":
        main()
    
