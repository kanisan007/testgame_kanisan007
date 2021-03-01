def printsquaresstatus(squarestatus: list):
    squareinfo = []
    for i in range(9):
        if squarestatus[i] == 0:
            squareinfo.append(' ')
        elif squarestatus[i] == 1:
            squareinfo.append('〇')
        elif squarestatus[i] == 2:
            squareinfo.append('×')
        else:
            raise SyntaxError('kiekie')
    return squareinfo

def nokorihantei(squarestatus: list):
    nokori = []
    for i in range(9):
        if squarestatus[i] == 0:
            nokori.append(i+1)
        else:
            pass
    return nokori

def winhantei(squarestatus: list, syurui: int):
    kie = []
    for i in range(9):
        if squarestatus[i] == syurui:
            kie.append(i+1)
        else:
            pass
    kekka = 0
    if 1 in kie:
        if 2 in kie:
            if 3 in kie:
                kekka = 1

        elif 4 in kie:
            if 7 in kie:
                kekka = 1

        elif 5 in kie:
            if 9 in kie:
                kekka = 1

    elif 2 in kie:
        if 8 in kie:
            kekka = 1

    elif 3 in kie:
        if 5 in kie:
            if 7 in kie:
                kekka = 1

        elif 6 in kie:
            if 9 in kie:
                kekka = 1

    elif 4 in kie:
        if 5 in kie:
            if 6in kie:
                kekka = 1

    elif 7 in kie:
        if 8 in kie:
            if 9 in kie:
                kekka = 1

    if kekka == 1:
        kekka = syurui
    return kekka
