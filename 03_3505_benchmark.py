import random
import time
import AulasPraticas.AP_03_ordenacao as ordn
import sys

random.seed(1001)
sys.setrecursionlimit(10000)
Ns = [100, 500, 1000, 5000]
K = 50
def gerarListaRnd(n):
    return random.sample(range(1, n), n)

def gerarListaPior(n):
    return list(range(n,0,-1))


def calcMedioPior(f_ord):

    medio= [0] * len(Ns)
    pior = [0] * len(Ns)
    for i in range(len(Ns)):
        n = Ns[i]
        for _ in range(K):
            arrMedio = gerarListaRnd(n) 
            arrPior = gerarListaPior(n)
            
            startTimeMedio = time.perf_counter()
            f_ord(arrMedio)
            endTimeMedio = time.perf_counter()


            startTimePior = time.perf_counter()
            f_ord(arrPior)
            endTimePior = time.perf_counter()
            
            medio[i] += endTimeMedio - startTimeMedio
            pior[i] += endTimePior - startTimePior
        medio[i] /= K
        pior[i] /= K
    return [medio, pior]

# selection_sort
medio_selection_sort, pior_selection_sort = calcMedioPior(ordn.selection_sort)

# divide_and_conquer_sort
medio_divide_and_conquer_sort, pior_divide_and_conquer_sort = calcMedioPior(ordn.divide_and_conquer_sort)

# quick_sort
medio_quick_sort, pior_quick_sort = calcMedioPior(ordn.quick_sort)

# 1. Definindo o cabeçalho com alinhamento e largura fixa
print(f"{'N':^15} | {'Medio selection_sort':^25} | {'Pior selection_sort':^25} | {'Medio divide_and_conquer_sort':^30} | {'Pior divide_and_conquer_sort':^30} | {'Medio quick_sort':^30} | {'Pior quick_sort':^30}")
for i in range(len(Ns)):
    print(f"{Ns[i]:^{15}} | {medio_selection_sort[i]:^{25}} | {pior_selection_sort[i]:^{25}} | {medio_divide_and_conquer_sort[i]:^{30}} | {pior_divide_and_conquer_sort[i]:^{30}} | { medio_quick_sort[i]:^{30}} | {pior_quick_sort[i]:^{30}}")
