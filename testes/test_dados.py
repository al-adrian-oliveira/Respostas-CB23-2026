"""Seus testes do Marco 1 (veja a seção 6 do ENUNCIADO_MARCO1.md).

Regras: pelo menos 8 testes seus (o exemplo abaixo não conta), uma docstring em cada teste
dizendo qual caso ele cobre, e floats comparados com assertAlmostEqual ou np.allclose.
"""
import unittest

from elevatoria.dados import por_tag
from elevatoria.serie import SerieTemporal
import numpy as np

class TestPorTagExemplo(unittest.TestCase):
    """Exemplo do formato. `por_tag` é código existente da base."""

    def test_lista_vazia(self):
        """Sem registros, por_tag devolve uma lista vazia."""
        self.assertEqual(por_tag([], "PT101"), [])
# Acrescente abaixo as suas classes de teste, começando pelos testes de regressão da
# issue #4 (escreva-os ANTES de corrigir o defeito e confirme que falham).

class TestRegressaoMediaMovel(unittest.TestCase):

    def test_media_movel_600_leituras_janela_30(self):
        """Verifica que 600 leituras com janela 30 produzem 571 médias."""
        s = SerieTemporal.de_lista(np.arange(600, dtype=float))

        resultado = s.media_movel(30)

        self.assertEqual(len(resultado), 571)
        self.assertIsInstance(resultado, SerieTemporal)
        self.assertTrue(
            np.allclose(resultado, np.arange(571) + 14.5)
        )
        
if __name__ == "__main__":
    unittest.main()
