"""Regras do exercício. Responsável: Leonardo Souza Bezerra."""


def quantidade_itens_valida(quantidade):
    """Aceita quantidades de 1 a 10; valores negativos geram ValueError.

    O exercício utiliza quantidades inteiras. Esta regra é independente
    da implementação do site e não comprova validações da API LocalEats.
    """
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")
    return 1 <= quantidade <= 10
