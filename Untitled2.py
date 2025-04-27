print('Jogo da Adivinhação')
Tentativa = None
Modo = None
Nivel = None
num1 = 7
num2 = 82
num3 = 453

#laço para escolha do modo
while True:
    print('Se deseja jogar a versão Maior/Menor digite "M" \nSe deseja jogar a versão Diferença digite "D"')
    Modo = input()
    if ((Modo == 'M') or (Modo == 'm')):
    
    #Laço para escolha do nível (Modo Maior/Menor)
    
        while True:
            print('Digite qual nível deseja jogar:\n \"nivel1 (números de 1 a 10)\" \n \"nivel2 (números de 1 a 100)\" \n \"nivel3 (números de 1 a 1000)\" \n menu anterior = \"x\"')
            Nivel = input()
            if (Nivel == 'nivel1'):
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    if (Tentativa > num1):
                        print('O número é menor do que o escolhido')
                    elif (Tentativa < num1):
                        print('O número é maior do que o escolhido')
                    else:
                        break
                print('Você acertou o número')
            elif (Nivel == 'nivel2'):
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    if (Tentativa > num2):
                        print('O número é menor do que o escolhido')
                    elif (Tentativa < num2):
                        print('O número é maior do que o escolhido')
                    else:
                        break
                print('Você acertou o número')
            elif (Nivel == 'nivel3'):
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    if (Tentativa > num3):
                        print('O número é menor do que o escolhido')
                    elif (Tentativa < num3):
                        print('O número é maior do que o escolhido')
                    else:
                        break
                
                print('Você acertou o número')
            else:
                break
            
    elif ((Modo == 'D') or (Modo == 'd')):
        
        #laço para escolha do nível (Modo Diferença)
        
        while True:
            print('Digite qual nível deseja jogar:\n \"nivel1 (números de 1 a 10)\" \n \"nivel2 (números de 1 a 100)\" \n \"nivel3 (números de 1 a 1000)\" \n menu anterior = \"x\"')
            Nivel = input()
            if (Nivel == 'nivel1'):
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    diferença = abs(num1 - Tentativa)
                    if (Tentativa != num1):
                        print(f'A diferença entre seu chute para o número é de {diferença}')
                    else:
                        break
                print(f'Você acertou, o número correto é {Tentativa}')
            elif (Nivel == 'nivel2'):
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    diferença = abs(num2 - Tentativa)
                    if (Tentativa != num2):
                        print(f'A diferença entre seu chute para o número é de {diferença}')
                    else:
                        break
                print(f'Você acertou, o número correto é {Tentativa}')
            elif (Nivel == 'nivel3'):
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    diferença = abs(num3 - Tentativa)
                    if (Tentativa != num3):
                        print(f'A diferença entre seu chute para o número é de {diferença}')
                    else:
                        break

                print(f'Você acertou, o número correto é {Tentativa}')
            else:
                break
    else:
        print('Escolha inválida')