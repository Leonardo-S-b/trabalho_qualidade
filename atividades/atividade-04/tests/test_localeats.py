"""Teste pela interface real. Responsável: Leonardo Souza Bezerra."""

from pathlib import Path

from playwright.sync_api import Page, expect


def test_criar_conta_exibe_formulario_de_cadastro(page: Page):
    """TF01: trocar o formulário de login pelo de cadastro."""
    page.goto("https://local-eats-unisenac.vercel.app/")

    # Pré-condição: o formulário de login aparece na entrada do site.
    expect(page.get_by_placeholder("teste@teste.com", exact=True)).to_be_visible()
    page.get_by_role("button", name="Criar Conta", exact=True).click()

    # Resultados observáveis da interação, com espera automática do Playwright.
    expect(page.get_by_placeholder("Seu nome", exact=True)).to_be_visible()
    expect(page.get_by_placeholder("novo@teste.com", exact=True)).to_be_visible()
    expect(page.get_by_placeholder("Min. 3 caracteres", exact=True)).to_be_visible()
    expect(page.get_by_role("button", name="Registrar", exact=True)).to_be_visible()
    expect(page.get_by_placeholder("teste@teste.com", exact=True)).to_be_hidden()
    expect(page.get_by_placeholder("Sua senha secreta", exact=True)).to_be_hidden()

    evidencias = Path(__file__).resolve().parents[1] / "evidencias"
    evidencias.mkdir(exist_ok=True)
    page.screenshot(
        path=str(evidencias / "TF01-formulario-cadastro.png"),
        full_page=True,
        animations="disabled",
    )
