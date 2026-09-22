# Atividade 3: Estratégia e Projeto de Testes do LocalEats

## 1. Identificação

**Unidade Curricular:** Qualidade de Software  
**Metodologia:** Problem-Based Learning (PBL)  
**Projeto:** LocalEats  
**Turma:** ads-2026-noite.  
**Modalidade:** Individual.  
**Data:** 22/09/2026.

| Nome | Usuário no GitHub |
|---|---|
| Leonardo Souza Bezerra | @Leonardo-S-b |

**Elemento de Competência:** EC4 — Planejar e projetar testes selecionando técnicas adequadas.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

## 2. Tarefa 1: Planejamento dos testes

### 2.1 Objetivo dos testes

Verificar se o LocalEats permite criar pedidos somente com quantidades válidas e se o total apresentado ao usuário é coerente com os preços exibidos no cardápio, as quantidades escolhidas e eventuais valores informados no fluxo.

### 2.2 Escopo

| Integrante | Funcionalidade incluída | O que será verificado |
|---|---|---|
| Leonardo Souza Bezerra | Fazer pedido | Inclusão de item no pedido, envio de quantidade válida ou inválida e coerência entre preço unitário exibido, quantidade e total estimado. |

| Funcionalidade não incluída | Justificativa |
|---|---|
| Criar conta | Não faz parte do fluxo de pedido selecionado para esta atividade individual. |

### 2.3 Abordagem

| Item | Decisão | Justificativa |
|---|---|---|
| Níveis de teste | Sistema e integração. | O fluxo será verificado pela aplicação e pelas respostas observáveis da requisição de pedido, envolvendo interface, API e dados do cardápio. |
| Tipos de teste | Funcional. | O foco é verificar regras de aceitação da quantidade e cálculo do total do pedido. |
| Perspectiva | Caixa-preta. | Serão considerados dados enviados e comportamentos retornados, sem análise do código-fonte ou do banco de dados. |
| Técnicas de teste | Particionamento de equivalência e análise de valor limite. | As técnicas permitem representar classes de quantidade válida/inválida e conferir os valores próximos ao limite inferior conhecido: zero e um. |

### 2.4 Ambiente e responsabilidades

| Item | Definição |
|---|---|
| Ambiente necessário | Aplicação LocalEats disponível em <https://local-eats-unisenac.vercel.app/>; navegador atualizado; conexão com a internet; conta de teste; restaurante com itens e preços exibidos; ferramentas do navegador ou cliente HTTP para enviar o pedido com dados alternativos. |
| Responsável pelo planejamento | Leonardo Souza Bezerra. |
| Responsável pela especificação dos casos | Leonardo Souza Bezerra. |
| Responsável pela futura execução | Leonardo Souza Bezerra, com apoio de QA e desenvolvimento caso a execução faça parte de uma equipe. |

### 2.5 Critérios

| Critério | Definição |
|---|---|
| Entrada | Aplicação e API de pedidos disponíveis; conta de teste autenticada; restaurante e item do cardápio disponíveis; preço unitário visível; dados de teste preparados. |
| Saída | Os três casos planejados executados em futura etapa, com resultado obtido registrado para cada caso; riscos R01 e R02 cobertos por pelo menos um caso. |
| Suspensão | Aplicação ou API indisponível, falha de autenticação que impeça o pedido, ausência de restaurantes ou itens disponíveis para teste, ou mudança no fluxo que inviabilize os passos especificados. |

## 3. Tarefa 2: Riscos e técnicas de teste

### 3.1 Análise dos riscos

| ID | Integrante | Funcionalidade | Risco | Consequência | Probabilidade | Impacto | Prioridade | Justificativa |
|---|---|---|---|---|---|---|---|---|
| R01 | Leonardo Souza Bezerra | Fazer pedido | O sistema aceitar quantidade inválida, como zero, negativa, fracionada ou texto não numérico. | Usuário e restaurante podem receber um pedido inconsistente, com erro de cálculo, preparo ou registro. | Média | Alta | Alta | A quantidade é dado essencial do pedido. A exploração anterior mostrou validações para alguns casos; ainda assim, entradas alternativas podem chegar diretamente à API e precisam ser cobertas. |
| R02 | Leonardo Souza Bezerra | Fazer pedido | O total estimado divergir da multiplicação entre o preço exibido e a quantidade, sem taxa, desconto ou regra de arredondamento informada. | O usuário pode não confiar no valor e desistir do pedido; o restaurante pode receber valores percebidos como incorretos. | Média | Alta | Alta | Foi observada uma diferença de R$ 0,01 entre o preço exibido e o total para duas unidades durante a exploração da Atividade 1. Como o total afeta uma decisão de compra, o impacto é alto. |

### 3.2 Aplicação das técnicas

#### Técnica 1: Particionamento de equivalência

**Integrante responsável:** Leonardo Souza Bezerra  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R01  
**Técnica escolhida:** Particionamento de equivalência.

A técnica foi escolhida porque a regra de quantidade possui grupos de entrada que devem ter o mesmo comportamento. Em vez de testar todos os números e textos possíveis, um valor representativo é selecionado para cada classe.

| Classe | Situação | Valor representativo | Resultado esperado |
|---|---|---|---|
| Válida | Número inteiro maior que zero. | `2` | O pedido pode ser criado com quantidade 2. |
| Inválida | Número igual a zero. | `0` | O pedido é rejeitado e informa que a quantidade deve ser maior que zero. |
| Inválida | Número negativo. | `-1` | O pedido é rejeitado e informa que a quantidade é inválida. |
| Inválida | Número fracionado. | `1,5` | O pedido é rejeitado por não corresponder a uma quantidade inteira. |
| Inválida | Texto não numérico no campo de quantidade. | `"cem"` | O pedido é rejeitado por não corresponder a uma quantidade inteira. |

**Casos derivados:** CT01, CT02 e CT03.

#### Técnica 2: Análise de valor limite

**Integrante responsável:** Leonardo Souza Bezerra  
**Funcionalidade:** Fazer pedido  
**Risco relacionado:** R01 e R02  
**Técnica escolhida:** Análise de valor limite.

A exploração anterior indicou que o limite inferior para quantidade é maior que zero. Por isso, os valores 0, 1 e 2 são relevantes: 0 está fora da faixa válida; 1 é o primeiro valor válido; 2 representa o valor imediatamente acima da fronteira. O enunciado não informa um limite máximo de quantidade, portanto nenhum limite superior foi inventado.

| Valor | Relação com o limite inferior | Resultado esperado |
|---|---|---|
| 0 | Imediatamente abaixo da faixa válida. | Rejeitar o pedido. |
| 1 | Primeiro valor válido. | Permitir criar o pedido e apresentar total correspondente a uma unidade. |
| 2 | Imediatamente acima do primeiro valor válido. | Permitir criar o pedido e apresentar total correspondente a duas unidades, com arredondamento coerente com o preço exibido. |

**Casos derivados:** CT01 e CT02.

## 4. Tarefa 3: Casos de teste e rastreabilidade

### CT01: Criar pedido com quantidade mínima válida e total coerente

**Integrante responsável:** Leonardo Souza Bezerra  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R02 — total coerente com preço exibido e quantidade.  
**Técnica utilizada:** Análise de valor limite e particionamento de equivalência.

**Pré-condição:**  
Usuário de teste autenticado; restaurante disponível; produto do cardápio com preço unitário exibido; não há taxa ou desconto informado para o pedido.

**Dados de entrada:**  
Restaurante: restaurante disponível.  
Produto: um item do cardápio.  
Quantidade: `1`.

**Passos:**

1. Acessar um restaurante disponível.
2. Registrar o preço unitário exibido para um item do cardápio.
3. Adicionar uma unidade desse item ao pedido.
4. Finalizar o pedido.
5. Consultar a confirmação ou o histórico do pedido.

**Resultado esperado:**  
O pedido é criado com uma unidade do item. O total exibido corresponde ao preço unitário registrado, exceto se houver taxa, desconto ou regra de arredondamento explicitamente apresentada ao usuário.

### CT02: Impedir pedido com quantidade zero

**Integrante responsável:** Leonardo Souza Bezerra  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01 — aceitação de quantidade inválida.  
**Técnica utilizada:** Análise de valor limite e particionamento de equivalência.

**Pré-condição:**  
Usuário de teste autenticado; restaurante e item do cardápio disponíveis; ferramenta do navegador ou cliente HTTP disponível para enviar uma requisição de pedido com dados alternativos.

**Dados de entrada:**  
Restaurante: restaurante disponível.  
Produto: item pertencente ao restaurante.  
Quantidade: `0`.

**Passos:**

1. Preparar uma requisição de criação de pedido para um item do restaurante.
2. Informar quantidade igual a zero.
3. Enviar a requisição.
4. Consultar o código de resposta e a mensagem retornada.

**Resultado esperado:**  
O sistema rejeita o pedido, não cria registro de pedido com quantidade zero e apresenta uma mensagem que informe que a quantidade deve ser maior que zero ou que é inválida.

### CT03: Impedir pedido com quantidade informada como texto não numérico

**Integrante responsável:** Leonardo Souza Bezerra  
**Funcionalidade:** Fazer pedido  
**Risco ou requisito relacionado:** R01 — aceitação de quantidade inválida.  
**Técnica utilizada:** Particionamento de equivalência.

**Pré-condição:**  
Usuário de teste autenticado; restaurante e item do cardápio disponíveis; ferramenta do navegador ou cliente HTTP disponível para enviar uma requisição de pedido com dados alternativos.

**Dados de entrada:**  
Restaurante: restaurante disponível.  
Produto: item pertencente ao restaurante.  
Quantidade: `"cem"` como texto no corpo da requisição.

**Passos:**

1. Preparar uma requisição de criação de pedido para um item do restaurante.
2. Informar a quantidade como texto não numérico `"cem"`, mantendo o restante do corpo da requisição válido.
3. Enviar a requisição.
4. Consultar o código de resposta, a mensagem retornada e o histórico de pedidos.

**Resultado esperado:**  
O sistema rejeita a requisição por não conseguir interpretar a quantidade como número inteiro e não cria um novo pedido. A resposta informa, de forma compreensível, que quantity deve ser um número inteiro.

### 4.1 Matriz de rastreabilidade

| Integrante | Funcionalidade | Risco ou requisito | Técnica utilizada | Casos de teste |
|---|---|---|---|---|
| Leonardo Souza Bezerra | Fazer pedido | R01 — aceitação de quantidade inválida. | Particionamento de equivalência e análise de valor limite. | CT02 e CT03. |
| Leonardo Souza Bezerra | Fazer pedido | R02 — total divergente do preço exibido e quantidade. | Análise de valor limite e particionamento de equivalência. | CT01. |

## 5. Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT.

**Como foi utilizada:** Como apoio para organizar o plano de testes, formular riscos, selecionar técnicas de caixa-preta e revisar a clareza dos casos de teste e da matriz de rastreabilidade.

**Uma sugestão que precisou ser alterada ou rejeitada:** A sugestão inicial de tratar a string numérica `"2"` como inválida foi rejeitada. Na exploração anterior, a API converteu esse valor para o número 2 e aceitou o pedido. Por isso, o caso foi reformulado com o texto não numérico `"cem"`, que representa uma classe inválida e foi rejeitado durante a exploração.

**Como as respostas foram verificadas:** Comparei os riscos com a exploração da Atividade 1, mantive apenas fatos observados como motivação e não como resultado de teste. Conferi que há dois riscos, pelo menos uma técnica aplicada, três casos de teste, resultados esperados observáveis e cobertura de todos os riscos na matriz.
