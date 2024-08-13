import os
from datetime import datetime
#'-.-.', '.-', '.-.', '---', '.-..', '..', '-.', '.-'

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
    print('1. Converte uma palavra ou frase em código Morse')
    print('2. Decifrar um código Morse')
    print('3. Sair do programa\n')

def carrega_codigo_morse(): #Função para carregar o dicionário Morse
    dicionario_morse = {".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F","--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L","--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R","...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X","-.--": "Y", "--..": "Z", "-----": 0, ".----": 1, "..---": 2, "...--": 3,"....-": 4, ".....": 5, "-....": 6, "--...": 7, "---..": 8, "----.": 9}
    return dicionario_morse
 
def decodifica_codigo_morse(): #Função para decodificar o código morse
    mensagem = input('Digite a mensagem em código Morse: ')
    codigo_morse = carrega_codigo_morse()

    #print(codigo_morse) #ertificando que careguei o dicionario para dentro da função 

    palavras = mensagem.split('  ') #Separar palavras - Dois espaços
    mensagem_decodificada = []

    for palavra in palavras:
        letras = palavra.split(' ')  # Separar letras - Um espaço 
        palavra_decodificada = ''.join([codigo_morse.get(letra, '') for letra in letras])
        mensagem_decodificada.append(palavra_decodificada)

    #print(mensagem_decodificada) #Retorna a lista 
    return ' '.join(mensagem_decodificada)
    
def salva_mensagem(mensagem_decodificada, file_path): #Função que salva a menage em um arquivo txt    
    with open(file_path, 'a') as file:
        file.write(f"Mensagem decodificada: {mensagem_decodificada} | Data e hora: {datetime.now()}:\n")
        
def escolha_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))

    if opcao_escolhida == 1:
        print('Escolheu a opção 1')

    elif opcao_escolhida == 2:
        decodifica_codigo_morse()
        print('Um arquivo foi criado com a mensagem decodificada!')
        #TETSE
    elif opcao_escolhida == 3:
        print('Finalizando o programa...')
        
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
