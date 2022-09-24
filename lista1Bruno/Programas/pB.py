def pB(lista):
    x = lista.split(" ")
    soma: int = 0
    for i in range(1, len(x)+1):
        if i % 3 == 0:
            soma += int(x[i-1])
            i += 3
    return str(soma)
