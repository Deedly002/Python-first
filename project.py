print('Добро пожаловать в квест!\nВы очнулись на траве без вещей.')
inventory = []
dangers = {
    1: ('змея'),
    2: ('яма'),
    3: ('бандиты'),
    4: ('молния рядом с деревьями')
}

firstTurnDescription = 'Перед вами 3 пути(укажи нужный путь напечатав цифру):\n1 - город, 2 - лес, 3 - дом.\nПо какому пути можно идти? \nТвой выбор: '
# первая часть: выбор пути
firstTurn = int(input(firstTurnDescription))
if firstTurn == 1:
    print('Пройдя по пути и дойдя до моста ты увидишь кучку бандитов, они замечают тебя и бегут к тебе. Game over.')
elif firstTurn == 2:
    print('Ты прошёл и упал в яму со змеями. Game over.')
elif firstTurn == 3:
    print('Тебе успешно удалось проникнуть в дом!')
    print('Первая часть пройдена!')
# вторя часть: выжить
print('Вторая часть началась!')
secondTurnDescription = ('перед вами стоит выбор'
                         '\n так как дом оказался не заброшен вы слышите шаги,судя по скрипу понимаете что'
                         ' кто-то спускался со второго этажа(укажи нужный путь напечатав цифру): '
                         '\n1 - выпрыгнуть в окно, 2 - попытаться договориться, 3 - спрятаться.\nТвой выбор - что зделать? '
                         '\nТвой выбор: ')
secondTurn = int(input(secondTurnDescription))
if secondTurn == 1:
    print('Вы выпрыгнули в окно, но упали неудачно и сломали ногу, умерли от кровотечения. Game over.')
elif secondTurn == 2:
    print(
        'вы подходите к человеку и пытаетесь договориться о том - чтобы поспать здесь \n'
        'он требует деньги, ты говоришь что беден и тебя обокрали,\n'
        ' он не захотел тебя слушать и вышвырнул тебя, но ты выживаешь и'
        'тебя ловят стражники. Видя что у тебя нету паспорта они отправят тебя на рудники.\n Споткнулся, упал, кирка в голове. '
        'Game over.')
elif secondTurn == 3:
    print('Вы попытались спрятаться в шкаф\n вам удалось спрятаться, но он подходит и закрывает окно - вы выживаете')
    print('Вторая часть завершена!')
# третья часть: intruder
print('Nретья часть началась!')
ThirdTurnDescription = 'Вы видите как он нажимает на факел и открывается дверь в стене,\nон спускается туда? перед вами стоит два выбора(укажи нужный путь напечатав цифру):\n1 - спустится за ним, 2 - открыть окно и осторожжно выслесть. \n Твой выбор: '
thirdTurn = int(input(ThirdTurnDescription))
if thirdTurn == 1:
    print(
        'Спускаясь за ним вы видите лабороторию и кучу людей за стеклом,\nно из за того что люди вас заметили и начали просить о помощи - он почуял неладное и решил проверить лестницу. Вы строяли за поворотом поэтому ему не составило труда вас поймать. Game over')
elif thirdTurn == 2:
    print('Вам удачно удалось слезть с окна,\n но стражники видят как вы вылезли из окна - они побежали за тобой. Ты рассказал что произошло,\nно они не поверили в бредни и посадили тебя за ограбление. Game over')
