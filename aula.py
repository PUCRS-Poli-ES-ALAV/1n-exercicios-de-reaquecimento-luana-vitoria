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
    if(m == 0):
        return n + 1
    if(m != 0 and n == 0):
        return ackerman(m-1, 1)
    if(m != 0 and n != 0):
        return ackerman(m-1, ackerman(m, n-1))
    
#   A partir de um vetor de números inteiros, calcule a soma e o produto dos elementos do vetor.
def soma_produto(vetor, tam, soma, produto):
    if tam == 0:
        return soma, produto
    return soma_produto(vetor, tam - 1, soma + vetor[tam - 1], produto * vetor[tam - 1])

#   Verifique se uma palavra é palíndromo (Ex. aba, abcba, xyzzyx).
def palindromo(palavra, fim, inicio=0):
    if inicio >= fim-1:
        return True
    if palavra[inicio] != palavra[fim-1]:
        return False
    
    return palindromo(palavra, fim - 1, inicio + 1)

# Dado um número n, gere todas as possíveis combinações com as n primeiras letras do alfabeto. Ex.: n = 3. Resposta: ABC, ACB, BAC, BCA, CAB, CBA.
# TENTAR NOVAMENTE!
alfabeto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
combinacoes = []
def combinacoes_letras(qnt):
    if qnt == 0:
        return ""
    return alfabeto[qnt-1] + combinacoes_letras(qnt-1)

''' Defina uma sequência de Fibonacci generalizada, de f0 a f1 como sequência
fibg(f0, f1, 0), fibg(f0, f1, 1), fibg(f0, f1, 2), ..., onde:
         * fibg(f0, f1, 0) = f0
         * fibg(f0, f1, 1) = f1
         * fibg(f0, f1, n) = fibg(f0, f1, n − 1) + fibg(f0, f1, n − 2), se n > 1.'''

def sequencia_fib_generalizada(f0, f1, n):
    if n == 0:
        return f0
    if n == 1:
        return f1
    return sequencia_fib_generalizada(f0, f1, n-1) + sequencia_fib_generalizada(f0, f1, n-2)

if __name__ == "__main__":
    print(multiplicacao(6, 4))
    print(incremento_sucessivos(3, 2))
    print(soma_fracao(4))
    print(inverte_string("flor", 4, ""))
    print(gerador_sequencia(4))
    print(ackerman(0,8))
    print(soma_produto([2,5,7], 3, 0, 1))
    print(palindromo("xyyx", 4))
    print(combinacoes_letras(3))
    print(sequencia_fib_generalizada(0, 6, 5))