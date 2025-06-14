from Somar import somar
from Subtrair import subtrair
from Multiplicar import multiplicar
from Dividir import dividir

def main():
    while True:
        print("digite dois numeros")
        num1  = int(input("digite um numero "))
        num2  = int(input("digite outro numero "))


        print("escolha:\n1 para somar \n2para subtrair \n3 para multiplicar \n4 para dividir \n5 para sair")
        escolha = int(input("digite: "))

        if escolha ==1:
            print("a soma é: ", somar(num1,num2))
        elif escolha ==2:
            print(" a subtração é", subtrair(num1,num2))
        elif escolha ==3:
            print("a multiplicação é", multiplicar(num1,num2))
        elif escolha ==4:
            print("a divisão é", dividir(num1,num2))
        else: 
            break
        print("\n")
    print("fim do programa")
    return 0
main()