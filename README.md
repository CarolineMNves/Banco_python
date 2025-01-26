# Sistema de Gerenciamento de Contas Bancárias 🏦
Este projeto é um sistema de gerenciamento de contas bancárias simples, desenvolvido em Python para fins educacionais.
Ele permite criar clientes, gerenciar contas, realizar depósitos, saques, transferências e consultar saldos. 

📁 Estrutura
├── models/
│   ├── conta.py          # Classe Conta, gerencia as operações bancárias
│   ├── cliente.py        # Classe Cliente, armazena informações do cliente
├── utils/
│   ├── helper.py         # Funções auxiliares para formatação de data e valores
├── banco.py              # Sistema principal com interface de texto
├── README.md             # Documentação do projeto

⚙️ Funcionalidades
1. Gerenciamento de Contas:
  Criação de contas com cliente associado.
  Listagem de todas as contas cadastradas.

3. Operações Bancárias
  Depósito: Adicionar saldo à conta.
  Saque: Retirar valores, respeitando o saldo e o limite disponível.
  Transferência: Enviar valores entre contas cadastradas.
  Consulta de Saldo: Exibir o saldo total de uma conta.

5. Sistema com Interface Simples
  Menu interativo no terminal para navegar pelas funcionalidades.
