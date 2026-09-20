# Evidências da exploração — Leonardo

Capturas originais fornecidas pelo estudante em 20/09/2026, copiadas sem alterações e com nomes descritivos. Capturas de menus do navegador, código ainda não enviado e erros locais de edição foram excluídas quando não acrescentavam evidência de comportamento da aplicação.

| Arquivo | O que comprova |
|---|---|
| [Cardápio e preço](leonardo-cardapio-preco.png) | Produto 19 com preço exibido de R$ 87,12; resposta do cardápio com preço de várias casas decimais. |
| [Pedido válido](leonardo-pedido-valido-resposta.png) | Confirmação na interface e resposta do pedido 284 com uma unidade do produto 19. |
| [Quantidade textual aceita](leonardo-quantidade-textual-aceita.png) | Envio de quantity como string "2" e retorno HTTP 200. A captura isolada não mostra o corpo da resposta. |
| [Histórico e diferença de total](leonardo-historico-diferenca-total.png) | Pedido 284 com uma unidade por R$ 87,12 e pedido 287 com duas unidades por R$ 174,25. |
| [JSON inválido: envio](leonardo-json-invalido-envio.png) | cem sem aspas dentro do JSON e HTTP 422. Não é teste de string válida. |
| [JSON inválido: resposta](leonardo-json-invalido-resposta.png) | json_invalid, JSON decode error e Expecting value. |
| [Expressão textual rejeitada](leonardo-expressao-textual-rejeitada.png) | Envio correto da expressão como texto via JSON.stringify e HTTP 422, na parte inferior. O erro vermelho acima corresponde a tentativa anterior que não foi enviada. |
| [Produto 26 no restaurante 8](leonardo-produto26-restaurante8.png) | Pedido válido 288; a resposta vincula o produto 26 ao restaurante 8. Não demonstra, sozinha, a rejeição de um vínculo incorreto. |
| [Produto 21 aceito](leonardo-produto21-pedido-aceito.png) | POST com restaurante 6, produto 21 e quantity "2", retornando HTTP 200. Combinação válida, não teste de produto de outro restaurante. |

Os retornos de quantidade negativa, zero, fracionada, texto cem em JSON válido, quantidade ausente e combinação incorreta de restaurante/produto não possuem capturas específicas neste conjunto. Seus limites estão descritos no documento principal. Transcrições não foram convertidas em imagens nem apresentadas como prints originais.
