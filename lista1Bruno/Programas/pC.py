from pA import pA
from pB import pB

def pC(lista):
    i2 = int(pA(lista))
    i3 = int(pB(lista))

    if(i3 > i2):
        return 'true'
    else:
        return 'false'
