# Atividade 2: Organização da Qualidade no LocalEats

## 1. Identificação

**Unidade Curricular:** Qualidade de Software  
**Metodologia:** Problem-Based Learning (PBL)  
**Projeto:** LocalEats  
**Turma:** ads-2026-noite.  
**Modalidade:** Individual.  
**Data:** 20/09/2026.

| Nome | Usuário no GitHub |
|---|---|
| Leonardo Souza Bezerra | @Leonardo-S-b |

**Elemento de Competência:** EC2 — Identificar papéis, responsabilidades e competências relacionadas às atividades de qualidade e testes.

**Aplicação:** <https://local-eats-unisenac.vercel.app/>

## 2. Tarefa 1: Diagnóstico da situação

| Problema identificado | Possível consequência para o produto ou para a equipe |
|---|---|
| Os critérios para considerar uma funcionalidade pronta não estão claros. | Funcionalidades podem ser disponibilizadas sem validação consistente, com comportamentos diferentes do esperado ou pendências não percebidas. |
| Parte da equipe entende que somente o QA deve testar. | Os testes ficam concentrados e tardios; defeitos simples podem chegar ao QA ou aos usuários em vez de serem prevenidos durante desenvolvimento e revisão. |
| Defeitos não são sempre registrados e acompanhados. | A equipe perde informações sobre impacto, prioridade e estado da correção; o mesmo defeito pode reaparecer ou permanecer sem solução. |

A qualidade do LocalEats não deve ser responsabilidade exclusiva do QA. O QA organiza a estratégia de testes, apoia a investigação de defeitos e traz visibilidade sobre riscos, mas a qualidade é construída desde os requisitos. Produto define critérios claros, desenvolvimento implementa e testa, e liderança coordena a disponibilização. A colaboração entre esses papéis reduz defeitos e evita que os testes aconteçam apenas no final.

## 3. Tarefa 2: Papéis e competências

| Integrante | Papel analisado | Responsabilidades relacionadas à qualidade | Competências técnicas | Competências comportamentais |
|---|---|---|---|---|
| Leonardo Souza Bezerra | Responsável pelo produto (Product Owner) | Esclarecer necessidades dos usuários; definir e priorizar critérios de aceitação; validar se a funcionalidade entregue atende ao valor esperado antes da disponibilização. | Levantamento e priorização de requisitos, definição de critérios de aceitação, conhecimento do domínio de pedidos e restaurantes. | Comunicação clara, capacidade de decisão, escuta ativa, organização e negociação. |
| Leonardo Souza Bezerra | Desenvolvedor | Implementar a funcionalidade conforme os critérios; criar e manter testes unitários; participar de revisão de código; corrigir defeitos atribuídos e informar limitações técnicas. | Programação, testes unitários, depuração, controle de versão, revisão de código e compreensão de APIs. | Colaboração, responsabilidade, atenção a detalhes, abertura a feedback e pensamento crítico. |
| Leonardo Souza Bezerra | QA / Analista de qualidade | Planejar e executar testes do sistema; avaliar riscos; registrar defeitos com passos de reprodução e evidências; acompanhar correções e comunicar resultados. | Técnicas de teste, elaboração de cenários, testes funcionais e exploratórios, registro de defeitos, leitura de respostas HTTP e análise de evidências. | Curiosidade, comunicação objetiva, organização, imparcialidade e colaboração. |
| Leonardo Souza Bezerra | Liderança técnica | Definir padrões técnicos e de revisão; apoiar decisões sobre riscos; assegurar que a entrega esteja tecnicamente pronta para disponibilização; remover impedimentos da equipe. | Arquitetura de software, integração contínua, revisão de código, gestão de riscos técnicos e estratégia de testes. | Liderança, mediação, tomada de decisão, visão sistêmica e capacidade de orientar a equipe. |

## 4. Tarefa 3: Matriz de responsabilidades

**Legenda:** R = Responsável por executar; A = Aprovador; C = Consultado; I = Informado.

| Atividade de qualidade | Responsável pelo produto | Desenvolvedor | QA / Analista de qualidade | Liderança técnica |
|---|---|---|---|---|
| Definir critérios de aceitação | R/A | C | C | I |
| Revisar requisitos | A | C | R | I |
| Implementar a funcionalidade | C | R/A | C | I |
| Revisar o código | I | R | I | A |
| Criar testes unitários | I | R/A | C | I |
| Planejar e executar testes do sistema | C | C | R/A | I |
| Registrar e acompanhar defeitos | I | C | R/A | I |
| Priorizar a correção dos defeitos | R/A | C | C | I |
| Aprovar a disponibilização da versão | C | C | R | A |

### Lacuna ou conflito encontrado

A aprovação da disponibilização da versão poderia ficar sem responsável definido, pois o contexto informa que não está claro quem pode aprová-la. Também haveria conflito se Produto, QA e Liderança Técnica tentassem aprovar a mesma decisão. Na matriz, a Liderança Técnica é o único **A** porque responde pelo risco técnico da versão; o QA executa a validação e o responsável pelo produto é consultado sobre o valor e os critérios de aceitação.

### Práticas recomendadas

| Prática recomendada | Problema que ajuda a resolver | Papéis envolvidos |
|---|---|---|
| Definir uma *Definition of Done* para cada funcionalidade, incluindo critérios de aceitação atendidos, revisão de código, testes unitários, testes do sistema relevantes e registro de pendências conhecidas. | Falta de clareza sobre quando uma funcionalidade está pronta e disponibilização de itens incompletos. | Responsável pelo produto, Desenvolvedor, QA e Liderança técnica. |
| Realizar triagem periódica de defeitos em um quadro único, com descrição, evidência, severidade, prioridade, responsável e situação. | Defeitos sem acompanhamento e dificuldade para decidir quais correções devem ser tratadas primeiro. | QA, Responsável pelo produto, Desenvolvedor e Liderança técnica. |

## 5. Uso de inteligência artificial

**Ferramenta utilizada:** ChatGPT.

**Como foi utilizada:** Como apoio para interpretar o enunciado, diferenciar papéis, responsabilidades e competências, elaborar a matriz RACI e redigir a proposta de organização da qualidade.

**Como as respostas foram verificadas:** Conferi se cada atividade da matriz possui ao menos um responsável e apenas um aprovador. Também revisei a coerência entre os problemas apontados, os papéis definidos e as práticas recomendadas, verificando que a qualidade não ficou concentrada somente no QA.
