
import os

def exibir_nome_do_programa():
    print('''
░█████╗░░█████╗░██████╗░██╗░██████╗░░█████╗░  ███╗░░░███╗░█████╗░██████╗░░██████╗███████╗
██╔══██╗██╔══██╗██╔══██╗██║██╔════╝░██╔══██╗  ████╗░████║██╔══██╗██╔══██╗██╔════╝██╔════╝
██║░░╚═╝██║░░██║██║░░██║██║██║░░██╗░██║░░██║  ██╔████╔██║██║░░██║██████╔╝╚█████╗░█████╗░░
██║░░██╗██║░░██║██║░░██║██║██║░░╚██╗██║░░██║  ██║╚██╔╝██║██║░░██║██╔══██╗░╚═══██╗██╔══╝░░
╚█████╔╝╚█████╔╝██████╔╝██║╚██████╔╝╚█████╔╝  ██║░╚═╝░██║╚█████╔╝██║░░██║██████╔╝███████╗
░╚════╝░░╚════╝░╚═════╝░╚═╝░╚═════╝░░╚════╝░  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝\n''')

def exibir_opcoes_menu():
    print('Escololha uma das opções abaixo: \n')
    print('1. Criar uma mensagem em código Morse')
    print('2. Decifrar um código Morse')
    print('3. Sair do programa\n')

def escolha_opcao():
    '''Exibi a solicitação de cada função que deve ser escolhida pelo usuário
    Outputs:
    -Executa a opção escolhida pelo usuário.
    '''
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Você escolheu a opção 01')
    elif opcao_escolhida == 2:
        print('Você escolheu a opção 02')
    elif opcao_escolhida == 3:
        print('você escolheu a opcao 03')
    else:
        print('Sinto muito, essa não é uma opcao válida!')


def main():
    ''' Função principal que inicia o programa '''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes_menu()
    escolha_opcao()

if __name__ == '__main__':
    main()
