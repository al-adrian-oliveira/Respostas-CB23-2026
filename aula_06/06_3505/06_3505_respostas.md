# Complexidade desenfileirar

Supondo que temos N itens na fila, sendo que $n_1$ estão em head e $n_2$ estão em tail ($n_1 + n_2 = N$), e queremos fazer N operações de desenfileirar. 

## Primeiros n1 (melhor caso):

Nesse caso cada operação tem tempo constante, visto que envolve apenas o pop de uma pilha. Resultando em $n_1$ operações

## Caso primeiro item em tail (pior caso):

Nesse caso todos os itens em tail são copiados para head ($n_2$ operações) e um pop é executado em head (1 operação). Resultando em $n_2 + 1$ operações

## Proximos n2 - 1 casos :
Aqui recaimos no melhor caso (quando todos os itens estão em head). Resultando em $n_2 - 1$ operações


Portanto, o custo médio de uma operação é o custo total dividido pelo número de operações:

$$\frac{n_1 + n_2 + 1 + n_2 - 1}{N} = \frac{N + n_2}{N} = 1 + \frac{n_2}{N}$$

Como: $$n_2 \le N$$


A complexida resultante é:
 $$O(2) = O(1)$$