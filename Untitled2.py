import random
print('Jogo da Adivinhação')
Tentativa = None
Modo = None
Nivel = None
contador = 0

#laço para escolha do modo

while True:
    print('Se deseja jogar a versão Maior/Menor digite "M" \nSe deseja jogar a versão Diferença digite "D"')
    Modo = input()
    if ((Modo == 'M') or (Modo == 'm')):
        #Laço para escolha do nível (Modo Maior/Menor)
    
        while True:
            print('Digite 1 para Nível 1 (números de 1 a 10) \nDigite 2 para Nível 2 (números de 1 a 100) \nDigite 3 para Nível 3 (números de 1 a 1000) \nDigite X para Menu Anterior')
            Nivel = input()
            if (Nivel == '1'):
                num1 = random.randint(1,10)                
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())   
                    contador += 1                 
                    if (Tentativa > num1):
                        print('O número é menor do que o escolhido')                        
                    elif (Tentativa < num1):
                        print('O número é maior do que o escolhido')                        
                    else:
                        break
                print(f'Você acertou o número em {contador} tentativas')
            elif (Nivel == '2'):
                num2 = random.randint(1,100)
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    contador += 1
                    if (Tentativa > num2):
                        print('O número é menor do que o escolhido')
                    elif (Tentativa < num2):
                        print('O número é maior do que o escolhido')
                    else:
                        break
                print(f'Você acertou o número em {contador} tentativas')
            elif (Nivel == '3'):                
                num3 = random.randint(1,1000)
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    contador += 1
                    if (Tentativa > num3):
                        print('O número é menor do que o escolhido')
                    elif (Tentativa < num3):
                        print('O número é maior do que o escolhido')
                    else:
                        break
                
                print(f'Você acertou o número em {contador} tentativas')
            else:
                break
            
    elif ((Modo == 'D') or (Modo == 'd')):        
        #laço para escolha do nível (Modo Diferença)        
        while True:
            print('Digite 1 para Nível 1 (números de 1 a 10) \nDigite 2 para Nível 2 (números de 1 a 100) \nDigite 3 para Nível 3 (números de 1 a 1000) \nDigite X para Menu Anterior')
            Nivel = input()
            if (Nivel == '1'):
                num1 = random.randint(1,10)                
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    contador += 1
                    diferença = abs(num1 - Tentativa)
                    if (Tentativa != num1):
                        print(f'A diferença entre seu chute para o número é de {diferença}')
                    else:
                        break
                print(f'Você acertou o número em {contador} tentativas')
            elif (Nivel == '2'):                
                num2 = random.randint(1,100)                
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    contador += 1
                    diferença = abs(num2 - Tentativa)
                    if (Tentativa != num2):
                        print(f'A diferença entre seu chute para o número é de {diferença}')
                    else:
                        break
                print(f'Você acertou o número em {contador} tentativas')
            elif (Nivel == '3'):                
                num3 = random.randint(1,1000)
                while True:
                    print('Qual você acha que é o número? ')
                    Tentativa = int(input())
                    contador += 1
                    diferença = abs(num3 - Tentativa)
                    if (Tentativa != num3):
                        print(f'A diferença entre seu chute para o número é de {diferença}')
                    else:
                        break

                print(f'Você acertou o número em {contador} tentativas')
            else:
                break
    else:
        print('Escolha inválida')