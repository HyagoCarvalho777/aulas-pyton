import random
def main():
    notas=[0.0]*4

    i = 0
    média = 0.0
    while i<4:
        notas[i] = random.uniform(0.0,10.0)
        média += notas[i]
        i = i+1
    média /= 4
    
    #print(notas)
    #print(média)
    print(f"primeira nota é {notas[0]:,.2}\nsegunda nota {notas[1]:,.2} ")
    print(f"terceira nota é {notas[2]:,.2}\nquarta nota é {notas[3]:,.2}")
    print(f"e a média é {média:,.2}")

    if média >= 6:
        print("aprovado")
    elif média >= 4:
        print("recuperação")
    else:
        print("reprovado")

    return 0
main()