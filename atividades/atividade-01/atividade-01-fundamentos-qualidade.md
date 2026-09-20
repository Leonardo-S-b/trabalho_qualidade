# Atividade 1: Fundamentos e Características da Qualidade no LocalEats

## 1. Identificação

**Turma:** A informar pelo estudante.  
**Modalidade:** Individual.  
**Data:** 20/09/2026.

| Nome | Usuário no GitHub |
|---|---|
| Leonardo Souza Bezerra | @Leonardo-S-b |

**Elemento de Competência:** Compreender os fundamentos de qualidade de software e sua aplicação no desenvolvimento de sistemas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

## 2. Tarefa 1: Fundamentos da qualidade

### 2.1 Necessidades explícitas e implícitas

| Tipo | Necessidade | Interessado | Consequência se não for atendida |
|---|---|---|---|
| Explícita | Permitir fazer pedidos nos restaurantes disponíveis. | Usuário e restaurante. | O usuário não consegue solicitar os produtos e o restaurante deixa de receber pedidos pela aplicação. |
| Explícita | Permitir consultar os pedidos realizados. | Usuário. | O usuário não consegue conferir as informações e a situação dos pedidos. |
| Implícita | Apresentar um total coerente com os preços unitários exibidos, as quantidades e eventuais taxas informadas. | Usuário e restaurante. | Diferenças de valores dificultam a conferência e reduzem a confiança no pedido. |
| Implícita | Impedir pedidos com quantidades inválidas e informar o motivo da rejeição. | Usuário e restaurante. | Pedidos inconsistentes podem causar erros de preparo, de cálculo e retrabalho. |

### 2.2 Questão sobre os fundamentos da qualidade

**Um sistema que implementa todas as funcionalidades explicitamente solicitadas pode, ainda assim, apresentar baixa qualidade?**

Sim. Ter as funcionalidades não garante que os resultados atendam às necessidades dos usuários. Um sistema pode permitir fazer e consultar pedidos, mas apresentar um total diferente do cálculo baseado nos preços exibidos. Nesse caso, deixa de atender à necessidade implícita de consistência dos valores, comprometendo a confiança na aplicação.

## 3. Tarefa 2: Exploração da aplicação

| Integrante | Funcionalidade | O que foi realizado | O que foi observado | Evidência |
|---|---|---|---|---|
| Leonardo Souza Bezerra | Fazer pedido. | Uso esperado: selecionei uma unidade do produto 19 no restaurante 6 e finalizei o pedido pela interface. Uso alternativo: reenviei a requisição POST /orders/ pelas ferramentas do navegador com quantidade "2" como texto. Também experimentei entradas inválidas, incluindo quantidade negativa e texto não numérico. | O pedido normal recebeu HTTP 200 e gerou o pedido 284, com total de R$ 87,12. A quantidade "2" foi aceita e retornada como número 2 no pedido 287, que apareceu no histórico. O total exibido foi R$ 174,25, enquanto duas unidades pelo preço mostrado de R$ 87,12 somam R$ 174,24. Na tentativa negativa, observei HTTP 400 e a mensagem "Quantity must be greater than 0"; para "cem", recebi erro int_parsing em quantity. Estes dois últimos retornos foram transcritos durante a exploração, sem captura correspondente disponível neste conjunto. | [Preço no cardápio](evidencias/leonardo-cardapio-preco.png); [pedido válido](evidencias/leonardo-pedido-valido-resposta.png); [envio de quantidade textual e HTTP 200](evidencias/leonardo-quantidade-textual-aceita.png); [histórico com os pedidos 284 e 287](evidencias/leonardo-historico-diferenca-total.png). |

### 3.1 Detalhamento do achado

O preço unitário apresentado no cardápio era R$ 87,12. Para duas unidades, o cálculo com esse preço resulta em R$ 174,24. O pedido 287 apareceu no histórico com duas unidades e total estimado de R$ 174,25: diferença de R$ 0,01.

A resposta JSON do pedido 287, copiada durante a exploração, apresentou quantity: 2, price_at_time: 87.1225493226881 e total_amount: 174.245098645376. Esses valores são compatíveis com multiplicar o preço com todas as casas decimais e arredondar apenas para exibição. Esta é uma explicação inferida a partir da resposta, não uma inspeção do código ou do banco de dados.

O resultado é uma inconsistência entre o preço exibido e o total estimado. Não foi constatado pagamento ou cobrança real. A aceitação da string numérica "2", convertida em 2, não foi classificada como defeito. O pedido de duas unidades foi enviado pela API; não foi concluída uma repetição desse mesmo cenário exclusivamente pelos botões da interface.

### 3.2 Explorações complementares

| Cenário | Resultado e alcance da evidência |
|---|---|
| Quantidade -1 | HTTP 400 e mensagem "Quantity must be greater than 0", transcritos na conversa. A captura do código preparado não comprova sozinha a resposta. |
| Quantidade zero | Rejeição relatada pelo estudante; sem captura ou corpo de resposta específico disponível. |
| Quantidade fracionada | Erro de interpretação relatado pelo estudante; sem captura específica que permita verificar o valor e a categoria do erro. |
| Quantidade "cem" em JSON válido | Resposta transcrita com int_parsing, apontando para body → items → 0 → quantity. |
| JSON malformado com cem sem aspas | HTTP 422 e resposta json_invalid / JSON decode error / Expecting value. É rejeição de sintaxe do JSON, não prova de validação do tipo de quantity. Capturas no índice de evidências. |
| Expressão enviada como texto: '"2" + 3' | Captura mostra envio e HTTP 422. Corpo transcrito posteriormente apresentou int_parsing e input igual à expressão. Os erros vermelhos anteriores no console são de outras tentativas e não respostas dessa API. |
| Produto 26 (restaurante 8) em pedido do restaurante 6 | Resposta transcrita: "Menu item 26 not found in this restaurant". Há captura do pedido válido 288 que demonstra o vínculo do produto 26 com o restaurante 8; ela não é captura da rejeição. |
| Item sem quantity | Resposta transcrita com type: missing e msg: Field required, apontando para quantity do primeiro item. |
| Pedido com items: [] | Não há resultado confirmado; não foi usado como conclusão da atividade. |

## 4. Tarefa 3: Requisitos e características de qualidade

| Integrante | Requisito de Qualidade | Característica ou subcaracterística | Justificativa | Como avaliar |
|---|---|---|---|---|
| Leonardo Souza Bezerra | Ao finalizar um pedido, o total apresentado deve corresponder à soma dos preços unitários exibidos multiplicados pelas respectivas quantidades, acrescida apenas de taxas e descontada apenas de reduções explicitadas ao usuário, com uma regra consistente de arredondamento em centavos. | Adequação funcional — correção funcional. | No LocalEats, o usuário utiliza os preços do cardápio para decidir o que pedir. O cálculo deve produzir um resultado coerente com esses preços. A diferença observada de R$ 0,01 mostra que disponibilizar a função de pedido não garante a correção do resultado apresentado. | Selecionar produtos com quantidades diferentes, calcular os totais a partir dos preços mostrados no cardápio e comparar com carrinho, confirmação e histórico. Registrar a diferença em centavos, considerando taxas ou descontos informados. Incluir o caso de duas unidades de R$ 87,12, cujo resultado esperado, sem adicionais, é R$ 174,24. |

## 5. Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT.

**Como foi utilizada:** Como apoio à compreensão dos requisitos da atividade, elaboração de hipóteses de teste, interpretação das respostas HTTP e JSON, organização das capturas e redação das tabelas e do requisito de qualidade.

**Como as respostas foram verificadas:** Realizei a exploração no navegador e comparei as sugestões com as requisições, respostas e telas observadas. Conferi a diferença entre R$ 87,12 × 2 e o total exibido de R$ 174,25. As hipóteses iniciais sobre ausência de backend e aceitação irrestrita de valores não foram tratadas como conclusões. Foram diferenciados erros de sintaxe no console, JSON malformado e validações retornadas pela API. Resultados apenas transcritos ou relatados estão identificados, sem serem apresentados como capturas existentes.
