from kiekie import printsquaresstatus
from kiekie import nokorihantei
from kiekie import winhantei

squaresstats = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
whowin = 0

while whowin == 0:
    nokori = nokorihantei(squaresstats)
    sentaku = int(input(f'player1のターンです。マスを数字で選択してください\n残っているマスは{nokori}です。\n>'))
    print(f'マス{sentaku}を〇で塗りつぶします。')
    squaresstats[sentaku- 1] = 1

    whowin = winhantei(squaresstats, 1)
    print(printsquaresstatus(squaresstats))

    nokori = nokorihantei(squaresstats)
    sentaku = int(input(f'player2のターンです。マスを数字で選択してください\n残っているマスは{nokori}です。\n>'))
    print(f'マス{sentaku}を×で塗りつぶします。')
    squaresstats[sentaku- 1] = 2

    whowin = winhantei(squaresstats, 2)
    print(printsquaresstatus(squaresstats))

if whowin == 1:
    print('player1の勝利です')
elif whowin == 2:
    print('player2の勝利です')
else:
    raise SyntaxError('unkunkunk')



