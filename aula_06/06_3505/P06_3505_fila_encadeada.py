import math
from P06_3505_pilha_encadeada import PilhaEncadeada

class FilaEncadeada:
    def __init__(self):
        self.head = PilhaEncadeada()
        self.tail = PilhaEncadeada()

    def enfileirar(self, item):
        """ Insere o item no fim da fila. 
            Complexidade: O(1)."""
        self.tail.push(item)

    def desenfileirar(self):
        """ Remove e retorna o item da frente; levanta IndexError se a fila estiver vazia.
            Complexidade: O(1) amortizada (caso médio)."""
        self._organizar()
        return self.head.pop()

    def frente(self):
        """ Retorna o item da frente sem removê-lo; levanta IndexError se a fila estiver vazia.
            Complexidade: O(1) amortizada (caso médio)."""
        self._organizar()
        return self.head.topo()

    def esta_vazia(self):
        """ Retorna True quando não há elementos armazenados.
            Complexidade: O(1)."""
        return len(self) == 0

    def __len__(self):
        """ Retorna a quantidade de elementos da fila.
            Complexidade: O(1)"""
        return len(self.head) + len(self.tail)

    def __repr__(self):
        """ Representação textual legível, da frente para o fim.
            Complexidade: O(N)"""
        return repr(self.head) + " " * (len(self.head) != 0)   +  repr(self.tail)[::-1]

    def _organizar(self):
        """ Preenche a pilha self.head caso esta esteja vazia e hajam items em self.tail; 
            Levanta IndexError se a fila estiver vazia.
            Complexidade: O(1) amortizada (caso médio).
            """
        if self.esta_vazia():
            raise IndexError("Sem itens")
        if len(self.head) != 0:
            return 
        while len(self.tail) != 0:
            self.head.push(self.tail.pop())


if __name__ == "__main__":
    pe = FilaEncadeada()
    pe.enfileirar(1)
    pe.enfileirar(2)
    pe.enfileirar(3)
    print(repr(pe))
    pe.frente()
    print(repr(pe))
    pe.enfileirar(4)
    print(repr(pe))
