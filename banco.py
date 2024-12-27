from typing import List
from time import sleep

from models.cliente import Cliente
from models.conta import Conta
from utils.helper import formata_float_str_moeda

contas: List[Conta] = []

def main() -> None:
    menu()
    
    
def menu() -> None:
    print('================================================')
    print('=================== CMN ========================')
    print('================ CM BANK =======================')
    print('================================================')
    
    print('Selecione uma opção para continuar: ')
    print('1 - Criar conta')
    print('2 - Efetuar saque')
    print('3 - Efetuar deposito')
    print('4 - Efetuar transferência')
    print('5 - Listar contas')
    print('6 - Consultar saldo')
    print('7 - Sair do sistema')
    
    opcao:  int = int(input())
    
    if opcao == 1:
        criar_conta()
    elif opcao ==2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        consultar_saldo()
    elif opcao == 7:
        print('Volte sempre')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        exit(0)



def criar_conta() -> None:
    print ('Informe os dados do cliente: ')
    nome: str = input("Nome do cliente: ")
    email: str = input("Email do cliente: ")
    cpf: str= input('CPF do cliente: ')
    data_nasc: str= input('Data de nascimento do cliente: ')
    
    cliente: Cliente = Cliente(nome, email, cpf, data_nasc)
    
    conta: Conta= Conta(cliente)
    contas.append(conta)
    
    print('Conta criada com sucesso!')
    print('Dados da conta: ')
    print('========================')
    print(conta)
    sleep(2)
    menu()
    
    
def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int= int(input('Informe o numero da sua conta: '))
        conta: Conta = buscar_conta_por_num(numero)
        
        if conta:
            valor: float = float(input('Informe o valor de saque: '))
            conta.sacar(valor)
        else:
            print(f'Não foi encontrada a conta de número: {numero}')
            
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()
    
def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da conta para realizar o depósito: '))
        
        conta: Conta = buscar_conta_por_num(numero)
        
        if conta:
            valor: float= float(input('Informe o valor de depósito'))
            conta.depositar(valor)
        else:
            print('N]ao foi encontrada a conta de número: {numero}')
            
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu() 
        


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))
        
        conta_o: Conta =buscar_conta_por_num(numero_o)

        
        if conta_o:
            numero_d: int = int(input('Informe o número da conta de destino: '))
            conta_d: Conta = buscar_conta_por_num(numero_d)
            
            if conta_d:
                valor: float=  float(input('Informe o valor da transferência: '))
                conta_o.transferir(conta_d, valor)
            else:
                print(f'A conta de destino de número {numero_d} não foi encontrada. Tente novamente')
                
        else:
            print(f'Não foi encontrada sua conta de número: {numero_o}')
            
    else:
        print('Ainda não existem contas cadastradas')
        
    sleep(2)
    menu()
    
def consultar_saldo() -> None:
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))
        conta: Conta = buscar_conta_por_num(numero)
        
        if conta:
            print(f'Saldo da conta {numero}: {formata_float_str_moeda(conta.saldo_total)}')
        else:
            print(f'Não foi encontrada a conta de número: {numero}')
    else:
        print('Ainda não existem contas cadastradas')
    
    sleep(2)
    menu()



def listar_contas() -> None:
    if len(contas) > 0:
        print('Listagem de contas')
        
        for conta in contas:
            print(conta)
            print('--------------------')
            sleep(1)    
        
    else:
        print('Ainda não existem contas cadastradas')
    sleep(2)
    menu()


def buscar_conta_por_num(numero: int) -> Conta:
    c: Conta = None
    
    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta   
    return c


if __name__ == '__main__':
    main()