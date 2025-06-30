# Sistema Bancário Simples em Python

Esse projeto e uma versao 2.0 do [desafio anterior](./trilha-python-dio/Vivo%20-%20Python%20AI%20Backend%20Developer/001-Dominando%20Python%20e%20Suas%20Estruturas%20de%20Dados/003-Criando%20um%20Sistema%20Bancário%20com%20Python/desafio-01-sistema-bancario)


## Funcionalidades

- **Depósito**
  - Permite depósitos apenas com valores positivos.
  - Todos os depósitos são registrados no extrato.

- **Saque**
  - Limite de até 3 saques diários.
  - Cada saque tem um limite máximo de R$ 500,00.
  - Não é permitido sacar valores superiores ao saldo disponível.
  - Somente valores positivos são aceitos.
  - Todos os saques são registrados no extrato.

- **Extrato**
  - Exibe uma lista com todos os depósitos e saques realizados.
  - Mostra o saldo atual.
  - Caso não haja movimentações, informa que nenhuma foi realizada.

- **Usuários**
  - Cadastro de novo usuário com CPF único.
  - Armazena nome completo, data de nascimento e endereço.

- **Contas Bancárias**
  - Criação de novas contas vinculadas a um usuário já cadastrado.
  - Cada conta possui um número único e uma agência padrão (`0001`).
  - É possível listar todas as contas cadastradas com seus respectivos titulares.

- **Validações**
  - Entradas inválidas (como letras onde se esperam números ou valores negativos) são tratadas com mensagens apropriadas.
  - O sistema permite até 3 tentativas de entrada inválida antes de encerrar automaticamente.

## Como executar

1. Certifique-se de ter o **Python 3** instalado.
2. Clone este repositório ou copie o código para um arquivo chamado `banco.py`.
3. Execute o arquivo Python no terminal:

```bash
python banco.py