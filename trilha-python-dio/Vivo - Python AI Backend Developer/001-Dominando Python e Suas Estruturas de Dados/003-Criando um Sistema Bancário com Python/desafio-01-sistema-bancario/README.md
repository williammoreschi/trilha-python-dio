# Sistema Bancário Simples em Python

Este é um projeto desenvolvido como parte do curso de Python. O sistema simula um banco simples com suporte para as seguintes operações:

- Depósito
- Saque
- Extrato

## Funcionalidades

- **Depósito**: permite depósitos apenas com valores positivos. Todos os depósitos são registrados no extrato.
- **Saque**:
  - Limite de até 3 saques diários.
  - Cada saque tem um limite máximo de R$ 500,00.
  - Não é permitido sacar valores superiores ao saldo disponível.
  - Somente valores positivos são aceitos.
  - Todos os saques são registrados no extrato.
- **Extrato**: exibe uma lista com todos os depósitos e saques realizados, além do saldo atual.
- **Validações**:
  - Entradas inválidas (como letras ou valores negativos) são tratadas com mensagens apropriadas.
  - O sistema permite até 3 tentativas de entrada inválida antes de encerrar automaticamente.


## Como executar

1. Certifique-se de ter o Python 3 instalado.
2. Clone este repositório ou copie o código.
3. Execute o arquivo Python no terminal:

```bash
python banco.py
