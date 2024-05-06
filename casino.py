from random import randint
from time import sleep

i = True # покуда есть деньги, играем
money = 100

while i:
    bet = input("ваша ставка (1 - чёрное, 2 - красное)")

    while bet != "1" and bet != "2":
        bet = input("ваша ставка (1 - чёрное, 2 - красное)")

    bet_is_ok = False
    while not(bet_is_ok):
        bank = input("сколько денег ставим?")
        # перед тем, как перевести в число, проверяем - это число ?
        while not(bank.isnumeric()):
            print("нужно ввести число !")
            bank = input("сколько денег ставим?")

        bank = int(bank)

        if bank > money:
            print("у тебя недостаточно средств")
        else:
            bet_is_ok = True

    print("Ставка на: ", bet, " сумма: ", bank)

    # крутится рулетка ..
    print(".")
    sleep(1)
    print("..")
    sleep(1)
    print("...")
    sleep(1)
    a = randint(1, 2)
    print("Выпадает: ", a)

    if int(bet) == a:
        money = money + bank
        print("Супер, ты выиграл", bank, "монет и у тебя", money, "золотых")
    else:
        money = money - bank
        print("Плохо, ты проиграл, у тебя", money, "денег")

    if money == 0:
        i = False

print("no money, no honey :-)")