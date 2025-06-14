def main():
    num1=int(input("digite um numero "))
    num2=int(input("digite outro numero "))

    soma=num1+num2
    sub=num1-num2
    mult=num1*num2

    if num2 == 0:
        div="divisão por 0 é imossivel"
    else:    
        div=num1/num2

    print("\na soma de ",num1," + ",num2,"=", soma)
    print("a sub de ",num1," - ",num2,"=", sub)
    print("a mult de ",num1," * ",num2,"=", mult)
    print("a div de ",num1," / ",num2,"=", div)
    return 0
main()