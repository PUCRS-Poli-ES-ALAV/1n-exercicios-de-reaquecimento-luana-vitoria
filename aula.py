# Multiplicação de dois números naturais, através de somas sucessivas (Ex.: 6 ∗ 4 = 4 + 4 + 4 + 4 + 4 + 4)

def multiplicacao(a, b, resultado=0):
    if b == 0:
        return resultado
    return multiplicacao(a, b - 1, resultado + a)

# Soma de dois números naturais, através de incrementos sucessivos (Ex.: 3 + 2 = + + (+ + + 1)).
def incremento_sucessivos(a, b):
    if b == 0:
        return a
    return incremento_sucessivos(a + 1, b - 1)

# Cálculo de 1 + 1/2 + 1/3 + 1/4 + ... + 1/N.
def soma_fracao(n):
    if n == 1:
        return 1
    return 1/n + soma_fracao(n-1)

# Inversão de uma string.
def inverte_string(palavra, tam, resultado):
    resultado += palavra[tam-1]
    if tam == 1:
        return resultado
    return inverte_string(palavra, tam -1, resultado)

'''
   1. Gerador da sequência dada por:
         * F(1) = 1
         * F(2) = 2
         * F(n) = 2 ∗ F(n − 1) + 3 ∗ F(n − 2).'''
def gerador_sequencia(a):
    if(a==1):
        return 1
    if(a==2):
        return 2
    return 2 * gerador_sequencia(a-1) + 3 * gerador_sequencia(a-2)
'''
   1.  Gerador de Sequência de Ackerman:
         * A(m, n) = n + 1, se m = 0
         * A(m, n) = A(m − 1, 1), se m != 0 e n = 0
         * A(m, n) = A(m − 1, A(m, n − 1)), se m != 0 e n != 0.'''
def ackerman(m, n):

if __name__ == "__main__":
    print(multiplicacao(6, 4))
    print(incremento_sucessivos(3, 2))
    print(soma_fracao(4))
    print(inverte_string("flor", 4, ""))
    print(gerador_sequencia(4))