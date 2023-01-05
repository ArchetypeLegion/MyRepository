pile_s1 = int(input("введите количество камней в 1 куче\n"))
pile_s2 = int(input("введите количество камней в 2 куче\n"))

while True:
    choose = int(input("выберите кучу из которой возьмете камни \n"))
    if choose == 1:
        while pile_s1 > 0:
            take = int(input("возьмите n количество камней\n"))
            pile_s1 -= take
            if pile_s1 > 0:
                print(pile_s1, pile_s2)
            else:
                take -= pile_s1
                if pile_s1 < 0:
                    pile_s1 = 0
                print(pile_s1, pile_s2)

    elif choose == 2:
        while pile_s2 > 0:
            take = int(input("возьмите n количество камней\n"))
            pile_s2 -= take
            if pile_s2 > 0:
                print(pile_s1, pile_s2)
            else:
                take -= pile_s2
                if pile_s2 < 0:
                    pile_s2 = 0
                print(pile_s1, pile_s2)
    if pile_s1 == 0 and pile_s2 == 0:
        print("в кучах не осталось камней")
        break
