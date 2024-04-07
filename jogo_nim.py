res = True
r = 0
def usuario_escolhe_jogada(n,m):
    tira = int(input('Quantas peças você vai tirar? '))
    while tira > m or tira <= 0 or tira > n:
        print('Oops! Jogada inválida! Tente de novo.')
        tira = int(input('Quantas peças você vai tirar? '))
    n -= tira
    if tira > 1:
        print('Voce tirou',tira,'peças.')
    else:
        print('Você tirou uma peça.')
    if n > 1:
        print('Agora restam',n,'peças no tabuleiro.')
    elif n == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
    else:
        print('Fim do jogo! O usuário ganhou!')
        n= (-2)
    return tira
def computador_escolhe_jogada(n,m):
    tira = m
    tiramsm = 0
    while tira > 0:
        resto = n - tira
        if resto % (m+1) == 0:
            tiramsm = tira
        tira -= 1
    if tiramsm == 0:
        tiramsm = m
    n -= tiramsm
    if tiramsm > 1:
        print('O computador tirou',tiramsm,'peças.')
    else:
        print('O computador tirou uma peça.')
    if n > 1:
        print('Agora restam',n,'peças no tabuleiro.')
    elif n == 1:
        print('Agora resta apenas uma peça no tabuleiro.')
    else:
        print('Fim do jogo! O computador ganhou!')
        n = (-1)
    return tiramsm

def partida():
    tira = n = m = 0
    while n <= 0:
        auxn = input('Quantas peças? ')
        if auxn.isnumeric() == True:
            n = int(auxn)
    while m <= 0:
        auxm = input('Limite de peças por jogada? ')
        if auxm.isnumeric() == True:
            m = int(auxm)
            if n<m:
                m=0
    if n % (m+1) == 0:
        print('Voce começa!')
        while n > 0:
            tira = usuario_escolhe_jogada(n,m)
            n-=tira
            if n > 0:
                tira=computador_escolhe_jogada(n,m)
                n-=tira
            else:
                return (-2)
        return (-1)
    else:
        print('Computador começa!')
        while n > 0:
            tira = computador_escolhe_jogada(n,m)
            n-=tira
            if n > 0:
                tira=usuario_escolhe_jogada(n,m)
                n-=tira
            else:
                return(-1)
        return (-2)
def campeonato():
    camp = 0
    u = c = 0
    while camp < 3:
        camp+=1
        print('**** Rodada', camp,'****')
        if partida()  == (-1):
            c+=1
        else:
            u+=1
    print('Placar: Você',u,'X',c,'Computador')

    
print('Bem-vindo ao jogo do NIM! Escolha:')
print('')
print('1 - para jogar uma partida isolada')
print('2 - para jogar um campeonato 2')
while res == True:
    r = input('R: ')
    if r == '1':
        print('Voce escolheu uma partida!')
        res = False
        partida()
    elif r == '2':
        print('Voce escolheu um campeonato!')
        res = False
        campeonato()
    else:
        res = True
#Na função usuario_escolhe_jogada, é preciso retornar a jogada, não o número de peças restantes.