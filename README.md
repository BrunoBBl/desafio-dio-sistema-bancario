# Sistema Bancário com Funções em Python

Projeto desenvolvido como desafio do **Bootcamp da DIO** (Digital Innovation One), com o objetivo de refatorar um sistema bancário simples de linha de comando, deixando o código modularizado por meio de funções.

## 📋 Sobre o desafio

A versão inicial do sistema era um único bloco de código sem separação de responsabilidades. O desafio consistiu em:

- Criar funções para as operações já existentes: **depositar**, **sacar** e **visualizar extrato**.
- Aplicar diferentes regras de passagem de argumentos em cada função, para exercitar os conceitos de **argumentos posicionais** e **argumentos nomeados** do Python.
- Evoluir o sistema para uma "versão 2", adicionando o cadastro de **usuários (clientes)** e a criação de **contas correntes** vinculadas a esses usuários.

## ⚙️ Funcionalidades

| Opção | Função | Descrição |
|-------|--------|-----------|
| `[c]` | Criar Usuário | Cadastra um novo cliente (nome, data de nascimento, CPF e endereço) |
| `[r]` | Criar Conta Corrente | Cria uma conta vinculada a um usuário já cadastrado, a partir do CPF |
| `[d]` | Depositar | Realiza um depósito na conta |
| `[s]` | Sacar | Realiza um saque, respeitando limite de valor e número de saques diários |
| `[e]` | Extrato | Exibe o histórico de movimentações e o saldo atual |
| `[lc]` | Listar Contas | Lista todas as contas cadastradas, com agência, número e titular |
| `[q]` | Sair | Encerra o programa |

## 🧠 Conceitos aplicados

O desafio pedia que cada função de operação bancária seguisse uma regra diferente de passagem de argumentos:

- **`deposito()`** — argumentos **somente posicionais** (`positional-only`), usando `/` na assinatura.
- **`saque()`** — argumentos **somente nomeados** (`keyword-only`), usando `*` na assinatura.
- **`exibir_extrato()`** — combinação de argumento **posicional** e **nomeado** na mesma função.

Além disso, o projeto trabalha com:

- Listas de dicionários para armazenar usuários e contas.
- Uma função auxiliar (`filtrar_usuarios`) para buscar um usuário pelo CPF, reaproveitada tanto na validação de CPF duplicado quanto no vínculo de conta corrente.
- Limpeza de CPF, mantendo apenas os dígitos informados, independentemente da formatação usada no cadastro (com ou sem pontos e traços).
- Retorno consistente de valores entre as funções, permitindo que o estado do sistema (saldo, extrato, número de saques, listas de usuários e contas) seja atualizado corretamente a cada operação.

## 📐 Regras de negócio

- Um usuário só pode ser cadastrado uma vez por CPF.
- O CPF é armazenado apenas com números, sem pontuação.
- O saldo, no depósito, aceita apenas valores positivos.
- O saque respeita três limites: saldo disponível, valor máximo por saque e número máximo de saques diários.
- A agência de todas as contas é fixa (`0001`).
- O número da conta é sequencial, iniciando em `1`.
- Um usuário pode ter mais de uma conta, mas cada conta pertence a um único usuário.

## ▶️ Como executar

```bash
python sistema_banco.py
```

O menu é exibido no terminal e a navegação acontece digitando a letra correspondente à opção desejada.

## 🛠️ Tecnologias

- Python 3 (utiliza recursos de argumentos `positional-only` e `keyword-only`, disponíveis a partir do Python 3.8)

## 🎓 Contexto

Projeto desenvolvido durante o **Bootcamp de Python da DIO**, como exercício de modularização de código e boas práticas na definição de funções.
