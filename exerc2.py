"Codigo para verificar se a entrada corresponde a sequencia de Fibonacci"

n = int(input("Digite qual numero você quer verificar se está na lista de Fibonacci: "))

def seq(n):
    fib = [0, 1]
    while fib[-1] < n:
        fib.append(fib[-1] + fib[-2])
    return fib

def verif(n):
    fib_seq = seq(n)
    return n in fib_seq


if verif(n):
    print(f"O número {n} pertence à sequência de Fibonacci.")
else:
    print(f"O número {n} NÃO pertence à sequência de Fibonacci.")
