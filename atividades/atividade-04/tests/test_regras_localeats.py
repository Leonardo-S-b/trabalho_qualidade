"""Testes da regra 3. Responsável: Leonardo Souza Bezerra."""

import pytest

from src.regras_localeats import quantidade_itens_valida


def test_quantidade_dentro_da_faixa_e_valida():
    """TU01: uma quantidade comum deve ser aceita."""
    assert quantidade_itens_valida(3) is True


def test_quantidade_zero_e_invalida():
    """TU02: zero está imediatamente abaixo do limite inferior."""
    assert quantidade_itens_valida(0) is False


@pytest.mark.parametrize("quantidade", [1, 10], ids=["minimo-1", "maximo-10"])
def test_limites_da_faixa_sao_validos(quantidade):
    """TU03: ambos os extremos pertencem à faixa válida."""
    assert quantidade_itens_valida(quantidade) is True


def test_quantidade_acima_do_maximo_e_invalida():
    """TU04: o primeiro inteiro acima do máximo deve ser rejeitado."""
    assert quantidade_itens_valida(11) is False


def test_quantidade_negativa_gera_erro():
    """TU05: negativos devem gerar ValueError, não retornar False."""
    with pytest.raises(ValueError, match="negativa"):
        quantidade_itens_valida(-1)
