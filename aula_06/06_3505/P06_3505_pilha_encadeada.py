class Node:
    def __init__(self,valor=None):
        self.valor = valor
        self.proximo = None

class PilhaEncadeada:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self,data):
        """ Insere o item no topo da pilha.
            Complexidade: O(1)"""
        if not self.head:
            self.head = Node(data)
        else:
            newHead = Node(data)
            newHead.proximo = self.head
            self.head = newHead
        self.size += 1
    
    def pop(self):
        """ Remove e retorna o item do topo; levanta IndexError se a pilha estiver vazia.
            Complexidade: O(1)"""
        if self.size == 0:
            raise IndexError("Sem itens")
        v = self.head.valor
        self.head = self.head.proximo
        self.size -= 1
        return v

    def topo(self):
        """ Retorna o item do topo sem removê-lo; levanta IndexError se a pilha estiver vazia.
            Complexidade: O(1)"""
        if self.size == 0:
            raise IndexError("Sem itens")
        return self.head.valor

    def esta_vazia(self):
        """ Retorna True quando não há elementos armazenados.
            Complexidade: O(1)"""
        return self.size == 0


    def __len__(self):
        """ Retorna a quantidade de elementos.
            Complexidade: O(1)"""
        return self.size

    def __repr__(self):
        """ Representação textual legível, do topo para a base.
            Complexidade: O(N)"""
        n = self.head
        arr = []
        while n:
            arr.append(str(n.valor))
            n = n.proximo
        return " ".join(arr) if len(arr) != 0 else ""

if __name__ == "__main__":
    pe = PilhaEncadeada()
    pe.push(1)
    pe.push(2)
    pe.push(3)
    print(repr(pe))
    print(pe.topo())
    print(len(pe))
    print(pe.pop())
    print(pe)
    print(pe.esta_vazia())
    pe.pop()
    pe.pop()
    print(len(pe))
    print(pe.esta_vazia())
    print(repr(pe))
