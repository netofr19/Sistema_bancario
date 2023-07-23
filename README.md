# Modelo de sistema bancário

## Objetivo
Este projeto tem como objetivo a modelagem de um sistema bancário composto pelas seguintes funções:
 - Saque;
 - Depósito;
 - Visualização do extrato.

## Funcionalidades
O projeto desenvolvido tem algumas restrições nas suas funcionalidades impostas pelo solicitantes, que são:

### Depósito
 - Nas operações de depósito, só deve ser possível depositar valores maiores do que zero;
 - Não há a necessidade de identificar agência e conta bancária para o depósito, visto que o sistema funciona com uma conta única.

### Saque
 - Serão permitidos até 3 saques diários;
 - Cada saque tem um limite máximo de R$ 500,00;
 - Intuitivamente, o valor do saque deverá ser maior do que o saldo no momento do saque, ou seja, não será permitida a utilização de empréstimos ou cheque especial.

### Extrato
 - No extrato, deverão ser listadas todas as operações de `depósito` e `saque` realizadas;
 - Porém se não houver qualquer movimentação na conta, o sistema deverá indicar ao usuário que não houve qualquer movimentação na conta;
  - Por fim, deverá ser exibido para o usuário o `saldo atual` da conta.

## Observações
Para a utilização do sistema bancário desenvolvido, é necessário apenas a instalação do Python 3.10+.

