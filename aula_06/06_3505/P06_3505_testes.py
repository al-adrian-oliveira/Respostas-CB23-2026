import unittest
from P06_3505_pilha_encadeada import PilhaEncadeada
from P06_3505_fila_encadeada import FilaEncadeada

class TestPilha(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.pilha = PilhaEncadeada()

    def test_push_pop(self):
        self.pilha.push(2)
        self.pilha.push(1)
        result1 = self.pilha.pop()
        result2 = self.pilha.pop()
        self.assertEqual(result1, 1)
        self.assertEqual(result2, 2)

    def test_pop_vazio(self):
        with self.assertRaises(IndexError):
            self.pilha.pop()

    def test_topo_vazio(self):
        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_len(self):
        self.assertEqual(len(self.pilha), 0)
        self.pilha.push(1)
        self.pilha.push(1)
        self.assertEqual(len(self.pilha), 2)
        self.pilha.pop()
        self.pilha.pop()
        self.assertEqual(len(self.pilha), 0)

    def test_armazenamento_de_itens(self):
        arr = ["word", 1, 1, 1.2, {1:1}, [1,2], (1,2), {1,2}, None]
        for item in arr:
            self.pilha.push(item)
        for item in reversed(arr):
            result = self.pilha.pop()
            self.assertEqual(result, item)

class TestFila(unittest.TestCase):

    
    def setUp(self):
        self.fila = FilaEncadeada()

    def test_fifo(self):
        self.fila.enfileirar(2)
        self.fila.enfileirar(1)
        result1 = self.fila.desenfileirar()
        result2 = self.fila.desenfileirar()
        self.assertEqual(result1, 2)
        self.assertEqual(result2, 1)

    def test_intercalar(self):
        self.fila.enfileirar(1)
        result = self.fila.desenfileirar()
        self.assertEqual(result, 1)

    def test_esvaziar_reusar(self):
        self.fila.enfileirar(1)
        while not self.fila.esta_vazia():
            self.fila.desenfileirar()
        self.fila.enfileirar(2)
        self.assertEqual(len(self.fila), 1)
        self.assertEqual(self.fila.desenfileirar(), 2)

    def test_desenfileirar_vazio(self):
        print(repr(self.fila))
        self.assertEqual(len(self.fila), 0)
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()

    def test_frente_vazio(self):
        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_coerencia_len(self):
        for i in range(1,101):
            self.fila.enfileirar(i)
            self.assertEqual(len(self.fila), i)

        for i in range(100,0):
            self.assertEqual(len(self.fila), i)
            self.fila.desenfileirar()

if __name__ == '__main__':
    unittest.main()