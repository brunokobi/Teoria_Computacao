import utils
from utils import rf
from universal import universal

I = 'yes'
S1 = utils.ESS(rf('P.py'), rf('Q.py'))

# String unica de entrada
S = utils.ESS(S1, I)


def applyBothTwice(S):
    (S1, I) = utils.DESS(S)
    (P, Q) = utils.DESS(S1)

    # Q(P(Q(P(I)))) formato de saida desejado
    x1 = universal(P, I)
    x2 = universal(Q, x1)
    x3 = universal(P, x2)
    x4 = universal(Q, x3)

    return x4
