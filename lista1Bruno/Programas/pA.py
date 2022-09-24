def pA(lista):
    x = lista.split(" ")
    soma: int = 0
    for i in range(len(x)):
        if i % 2 != 0:
            soma += int(x[i])
    return str(soma)
