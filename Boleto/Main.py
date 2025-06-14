def main():
    boleto = "140.857.987.451"
    i = 0
    j = 0
    boletoCerto = ""
    #quando tiver certeza do ponto
    for i in boleto:
        if boleto[j] != ".":
            boletoCerto += boleto[j]
        j += 1
    print(boletoCerto)
    return 0
main()