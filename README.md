# projeto-integrador-helpdesk
Projeto Integrador de Análise e Desenvolvimento de Sistemas - HelpDesk Pro.
# Projeto Integrador: HelpDesk Pro

> **Sistema de Gestão de Chamados e Ativos de TI**  
> **Instituição:** UCEFF — Análise e Desenvolvimento de Sistemas  
> **Aluno:** Kevin Josué Moya Bermúdez  

---

## 1. Apresentação do Escopo

### Introdução
O presente projeto consiste no desenvolvimento de uma aplicação web voltada para a gestão otimizada de suporte técnico em ambientes corporativos, denominada HelpDesk Pro. A solução foi concebida para centralizar o atendimento de chamados de TI, o registro de ocorrências e o controle básico de inventário de hardware e software, permitindo que equipes de suporte organizem suas demandas com maior eficiência e rastreabilidade.

Tecnologicamente, o sistema adota uma arquitetura web moderna baseada em Python com o framework Django para o back-end, garantindo segurança, escalabilidade e rapidez no processamento de dados, integrando-se a um banco de dados relacional robusto. A interface foi projetada para ser intuitiva, responsiva e de fácil navegação, priorizando a agilidade na abertura, triagem e encerramento de tickets de suporte técnico.

Com a implementação desta ferramenta, espera-se mitigar os gargalos tradicionais de atendimento helpdesk, como a perda de chamados por e-mail ou mensagens informais, proporcionando relatórios gerenciais e histórico centralizado que auxiliam na tomada de decisões estratégicas para a infraestrutura de TI da organização.

### Problema
A falta de centralização e rastreabilidade no atendimento de chamados de suporte técnico em pequenas e médias empresas, o que gera lentidão na resolução de problemas, perda de solicitações e ausência de histórico estruturado dos equipamentos e ocorrências dos usuários.

### Justificativa
A desorganização no suporte técnico impacta diretamente a produtividade dos colaboradores e sobrecarrega a equipe de TI. Resolver esse problema é importante para otimizar o tempo de atendimento, garantir indicadores claros de desempenho (SLA) e proporcionar uma experiência profissional e organizada tanto para o analista quanto para o usuário final.

### Objetivo Geral
Desenvolver um sistema web de gestão de chamados e suporte técnico, integrando o cadastro de usuários, abertura de tickets, atribuição de técnicos e controle de status, garantindo a resolução eficiente das demandas de TI.

### Objetivos Específicos
* Desenvolver a interface web responsiva para abertura e acompanhamento de chamados.
* Implementar módulos de autenticação e controle de acesso (Perfis: Administrador, Técnico e Usuário/Cliente).
* Criar o banco de dados relacional para gerenciar chamados, categorias, prioridades e histórico de movimentações.
* Disponibilizar relatórios básicos de atendimento para acompanhamento gerencial.

### Delimitação do Tema
A aplicação entregue neste ciclo não contemplará integração automatizada com ferramentas de monitoramento de rede (como Zabbix), nem gestão financeira avançada ou emissão de notas fiscais de peças de reposição.

---

## 2. Planejamento e Requisitos

### Requisitos Funcionais
* **RF01:** O sistema deve permitir o cadastro, edição e exclusão de usuários (clientes e técnicos).
* **RF02:** O usuário deve conseguir abrir um novo chamado informando título, descrição, categoria e nível de prioridade.
* **RF03:** O técnico deve poder assumir, atualizar o status (Aberto, Em Andamento, Concluído, Cancelado) e adicionar interações/comentários ao chamado.
* **RF04:** O sistema deve gerar uma listagem com filtros por status e prioridade para acompanhamento das demandas.

### Requisitos Não Funcionais
* **RNF01:** O sistema deve ser desenvolvido como uma aplicação Web.
* **RNF02:** O back-end deve utilizar Python com o framework Django.
* **RNF03:** O banco de dados utilizado será o PostgreSQL ou SQLite (para ambiente de desenvolvimento).
* **RNF04:** A interface deve ser responsiva, compatível com os principais navegadores web do mercado.

---

## 3. Cronograma Inicial

| Etapa / Tarefa | Descrição | Prazo Estimado | Responsável |
| :--- | :--- | :--- | :--- |
| **Fase 1: Concepção** | Definição de escopo, tecnologias e diagramas | Semana 1 | Kevin Josué |
| **Fase 2: Banco de Dados** | Criação das tabelas e scripts DDL/DML | Semana 2 | Kevin Josué |
| **Fase 3: Back-end** | Configuração do Django, models e rotas | Semana 3 | Kevin Josué |
| **Fase 4: Front-end** | Criação das telas de login, dashboard e chamados | Semana 4 | Kevin Josué |
| **Fase 5: Testes e Ajustes** | Validação de requisitos e entrega final | Semana 5 | Kevin Josué |

---

## 4. Modelagem Inicial (UML e MER)

### Diagrama de Caso de Uso (UML)
* **Atores:** Cliente/Usuário e Técnico de TI.
* **Principais Ações:** Autenticação no sistema, Abertura de chamados, Atribuição de tickets, Atualização de status e Gestão de comentários.

### Diagrama Entidade-Relacionamento (MER)
* **Tabela `Usuario`:** `id_usuario` (PK), `nome`, `email`, `senha`, `tipo_perfil`.
* **Tabela `Chamado`:** `id_chamado` (PK), `titulo`, `descricao`, `prioridade`, `status`, `data_criacao`, `id_usuario` (FK).
* **Tabela `Comentario`:** `id_comentario` (PK), `texto`, `data_comentario`, `id_chamado` (FK), `id_usuario` (FK).
