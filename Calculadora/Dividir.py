from VerificarZero import verificarZero

def dividir(num1,num2):
    if verificarZero(num2):
        div="divisão por 0 é impossivel"
    else: 
        div=num1/num2
    return div