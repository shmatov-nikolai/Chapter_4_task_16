from heroes import Hero_1, Hero_2
from towers import Tower_1, Tower_2, Tower_3, Tower_4, Castle_1, Castle_2
import time
from clint.textui import progress

# def zahvat_tower(tower_name, units_tower, tower_id, units_hero, hero_id):
#     start = time.time()
#     print("\n!!!Битва началась!!!")
#     time.sleep(5)
#     if units_hero < units_tower:
#         print("Сожалею Милорд, но эту битву Вы проиграли")
#         print(f'Ваши потери сотавили {units_hero} солдат, потери противника составили {units_tower - units_hero} солдат')
#         units_tower -= units_hero
#         units_hero = 0 
#     else:
#         print(f"\nУ Вас {units_hero} солдат .vs. {units_tower} солдат противника")
#         print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_name} в Ваших владениях.")
#         print(f"Потери в битве составили {units_hero-(units_hero-units_tower)} солдат")
#         units_hero = units_hero - units_tower,
#         units_tower = 0,
#         tower_id = hero_id
#         # return { units_hero,
#         #         units_tower,
#         #         tower_id
#                 # }

def main():
    print("Добро пожаловать в игру 'Лорды' \
\
\n\tПравила игры: Победа присуждается Лорду игрока, который уничтожает замок противника. Для уничтожения замка необходимо\
    убить гарнизон замка и создание катапульты на которую потребуется 1000 солдат Лорда. Катапульта создается в замке Лорда."
      )
    vvod = int(input("\
1 - начать игру\
\n2 - выйти из игры\
\nВаш выбор:"))
    if vvod == 2:
        print("До скорой встречи Милорд")
        
    elif vvod == 1:
        print("---------ИГРА НАЧАЛАСЬ---------")
        
        day = 0 
        hero_1 = Hero_1()
        hero_2 = Hero_2()
        tower_1 = Tower_1()
        tower_2 = Tower_2()
        tower_3 = Tower_3()
        tower_4 = Tower_4()
        castle_1 = Castle_1()
        castle_2 = Castle_2()
        pobeda = False
        while 1:
            if pobeda == True:
                print("Игра Завершена")
                break
            day +=1
            tower_1.update_soldat()
            tower_2.update_soldat()
            tower_3.update_soldat()
            tower_4.update_soldat()
            castle_1.update_soldat()
            castle_2.update_soldat()

            print(f'\n------------День {day}------------')
            
            for i in progress.bar(range(24)):
                time.sleep(0.05)
            print('\nСписок Башень')
            if tower_1.id != hero_1.id_:
                print(tower_1)
                print("--------------------------")
            if tower_2.id != hero_1.id_:
                print(tower_2)
                print("--------------------------")
            if tower_3.id != hero_1.id_:
                print(tower_3)
                print("--------------------------")
            if tower_4.id != hero_1.id_:
                print(tower_4)
                print("--------------------------")

            print(f"\nХод игрока {hero_1.name}")
            print(hero_1)
            print(castle_1)
            print(f"Башни в имении Лорда, сторона '{hero_1.id_}':")
            print('-------------------------------')
            if tower_1.id == hero_1.id_:
                print(tower_1)
                print("--------------------------")
            if tower_2.id == hero_1.id_:
                print(tower_2)
                print("--------------------------")
            if tower_3.id == hero_1.id_:
                print(tower_3)
                print("--------------------------")
            if tower_4.id == hero_1.id_:
                print(tower_4)
                print("--------------------------")
            
            
            if tower_1.id == hero_1.id_:
                print(f"\n4.{tower_1.name} это башня в Ваших владениях, Выберите чтобы посетить её")
            if tower_2.id == hero_1.id_:
                print(f"\n5.{tower_2.name} это башня в Ваших владениях, Выберите чтобы посетить её")
            if tower_3.id == hero_1.id_:
                print(f"\n6.{tower_3.name} это башня в Ваших владениях, Выберите чтобы посетить её")
            if tower_4.id == hero_1.id_:
                print(f"\n7.{tower_4.name} это башня в Ваших владениях, Выберите чтобы посетить её")
            
            while 1:
                if pobeda == True:
                    break
                print(f"\nЧто Вы будете делать Милорд?:\
                    \n0.Передать ход противнику\
                    \n1.Захватить Башню\
                    \n2.Использовать Сверхсилу\
                    \n3.Показать информацию о Лорде, Замке и башнях\
                    \n4,5,6,7 действия с Башнями в ваших владениях\
                    \n8.Отправиться в Замок Лорда\
                    \n9.Атаковать вражеский замок (если Вы не сможете захватить Замок, Вам засчитается поражение)")
                vibor = int(input('\nВаш выбор Милорд:'))

                if vibor == 0:
                    start = time.time()
                    print(f"Ход передан Лорду {hero_2.name}")
                    time.sleep(3)
                    break

                if vibor == 1:
                    print(f"На какую Башню Вы хотите напасть Милорд?:\n")
                    if tower_1.id == "Нейтральная" and tower_1.id != hero_1.id_:
                        print(f"1. {tower_1}")
                        print("--------------------------")
                    if tower_2.id == "Нейтральная" and tower_2.id != hero_1.id_:
                        print(f"2. {tower_2}")
                        print("--------------------------")
                    if tower_3.id == "Нейтральная" and tower_3.id != hero_1.id_:
                        print(f"3. {tower_3}")
                        print("--------------------------")
                    if tower_4.id == "Нейтральная" and tower_4.id != hero_1.id_:
                        print(f"4. {tower_4}")
                        print("--------------------------")

                    vibor_ = int(input("Решайтесь Милорд:"))

                    if vibor_ == 1:
                        if tower_1.id == hero_1.id_:
                            print("Это Башня уже Ваша!")
                            continue
                        
                        start = time.time()
                        print("\n!!!Битва началась!!!")
                        time.sleep(5)
                        
                        if hero_1.units < tower_1.units:
                            print("Сожалею Милорд, но эту битву Вы проиграли")
                            print(f'Ваши потери сотавили {hero_1.units} солдат')
                            tower_1.units -= hero_1.units
                            hero_1.units = 0
                            break 
                        else:
                            print(f"\nУ Вас {hero_1.units} солдат .vs. {tower_1.units} солдат противника")
                            print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_1.name} в Ваших владениях.")
                            print(f"Потери в битве составили {hero_1.units-(hero_1.units-tower_1.units)} солдат")
                            hero_1.units -= tower_1.units
                            tower_1.units = 0
                            tower_1.id = hero_1.id_
                            break
                        # zahvat_tower(tower_1.name, tower_1.units, tower_1.id, hero_1.units, hero_1.id_)

                    if vibor_ == 2:
                        if tower_2.id == hero_1.id_:
                            print("Это Башня уже Ваша!")
                            continue
                        
                        start = time.time()
                        print("\n!!!Битва началась!!!")
                        time.sleep(5)
                        
                        if hero_1.units < tower_2.units:
                            print("Сожалею Милорд, но эту битву Вы проиграли")
                            print(f'Ваши потери сотавили {hero_1.units} солдат')
                            tower_2.units -= hero_1.units
                            hero_1.units = 0
                            break 
                        else:
                            print(f"\nУ Вас {hero_1.units} солдат .vs. {tower_2.units} солдат противника")
                            print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_2.name} в Ваших владениях.")
                            print(f"Потери в битве составили {hero_1.units-(hero_1.units-tower_2.units)} солдат")
                            hero_1.units -= tower_2.units
                            tower_2.units = 0
                            tower_2.id = hero_1.id_
                            break
                    
                    if vibor_ == 3:
                        if tower_3.id == hero_1.id_:
                            print("Это Башня уже Ваша!")
                            continue
                        
                        start = time.time()
                        print("\n!!!Битва началась!!!")
                        time.sleep(5)
                        
                        if hero_1.units < tower_3.units:
                            print("Сожалею Милорд, но эту битву Вы проиграли")
                            print(f'Ваши потери сотавили {hero_1.units} солдат')
                            tower_3.units -= hero_1.units
                            hero_1.units = 0
                            break 
                        else:
                            print(f"\nУ Вас {hero_1.units} солдат .vs. {tower_3.units} солдат противника")
                            print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_3.name} в Ваших владениях.")
                            print(f"Потери в битве составили {hero_1.units-(hero_1.units-tower_3.units)} солдат")
                            hero_1.units -= tower_3.units
                            tower_3.units = 0
                            tower_3.id = hero_1.id_
                            break

                    if vibor_ == 4:
                        if tower_4.id == hero_1.id_:
                            print("Это Башня уже Ваша!")
                            continue
                        
                        start = time.time()
                        print("\n!!!Битва началась!!!")
                        time.sleep(5)
                        
                        if hero_1.units < tower_4.units:
                            print("Сожалею Милорд, но эту битву Вы проиграли")
                            print(f'Ваши потери сотавили {hero_1.units} солдат')
                            tower_4.units -= hero_1.units
                            hero_1.units = 0
                            break 
                        else:
                            print(f"\nУ Вас {hero_1.units} солдат .vs. {tower_4.units} солдат противника")
                            print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_4.name} в Ваших владениях.")
                            print(f"Потери в битве составили {hero_1.units-(hero_1.units-tower_4.units)} солдат")
                            hero_1.units -= tower_4.units
                            tower_4.units = 0
                            tower_4.id = hero_1.id_
                            break

                elif vibor == 2:
                    start = time.time()
                    hero_1.use_superpower()    
                    time.sleep(3)
                    continue

                elif vibor == 3:
                    start = time.time()
                    print(hero_1)
                    print(castle_1)
                    if tower_1.id == hero_1.id_:
                        print(tower_1)
                    if tower_2.id == hero_1.id_:
                        print(tower_2)
                    if tower_3.id == hero_1.id_:
                        print(tower_3)
                    if tower_4.id == hero_1.id_:
                        print(tower_4)
                    time.sleep(3)
                    continue
                
                elif vibor == 4:
                    while 1:
                        if tower_1.id != hero_1.id_:
                            print("Эта Башня непренадлежит Вам")
                            break
                        print(f"Вы прибыли на {tower_1.name}, гарнизон {tower_1.units} солдат, уровень: {tower_1.level}, набирает солдат до {tower_1.power}")
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон на башне\
                            \n3.Повысить уровень Башни\
                            \n4.Покинуть Башню\
                            \n5.Информация о Башне")
                        vibor = int(input("Что будем делать Милорд?:"))
                        
                        if vibor == 1:
                            if tower_1.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Башни, Вам доступно {tower_1.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > tower_1.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        tower_1.units -= num_solder
                                        hero_1.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_1.units} солдат")
                                        break
                            else:
                                print(f"На {tower_1} нет солдат")         
                            
                        if vibor == 2:
                            if hero_1.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_1.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_1.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        tower_1.units += num_solder
                                        hero_1.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {tower_1.units} солдат")  
                                        break
                            else:
                                print("У Вас нет солдат Милорд\n")
                        
                        if vibor == 3:
                            print("Для улучшения Башни Вам необходимо 100 солдат в гарнизоне башни")
                            if tower_1.units == 100:
                                tower_1.level_up_tower()  
                                tower_1.units = 0
                            else:
                                print("Недостаточно солдат\n")
                        
                        if vibor == 4:
                            print(f"Вы покидаете {tower_1.name}\n")
                            break
                        if vibor == 5:
                            print(f"\n{tower_1}")

                elif vibor == 5:
                    while 1:
                        if tower_2.id != hero_1.id_:
                            print("Эта Башня непренадлежит Вам")
                            break

                        print(f"Вы прибыли на {tower_2.name}, гарнизон {tower_2.units} солдат, уровень: {tower_2.level}, набирает солдат до {tower_2.power}")
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон на башне\
                            \n3.Повысить уровень Башни\
                            \n4.Покинуть Башню\
                            \n5.Информация о Башне")
                        vibor = int(input("Что будем делать Милорд?:"))
                        
                        if vibor == 1:
                            if tower_2.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Башни, Вам доступно {tower_2.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > tower_2.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        tower_2.units -= num_solder
                                        hero_1.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_1.units} солдат")
                                        break
                            else:
                                print(f"На {tower_2} нет солдат")         
                            
                        if vibor == 2:
                            if hero_1.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_1.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_1.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        tower_2.units += num_solder
                                        hero_1.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {tower_2.units} солдат")  
                                        break
                            else:
                                print("У Вас нет солдат Милорд\n")
                        
                        if vibor == 3:
                            print("Для улучшения Башни Вам необходимо 100 солдат в гарнизоне башни")
                            if tower_2.units == 100:
                                tower_2.level_up_tower() 
                                tower_2.units = 0 
                            else:
                                print("Недостаточно солдат\n")
                        
                        if vibor == 4:
                            print(f"Вы покидаете {tower_2.name}\n")
                            break
                        if vibor == 5:
                            print(f"\n{tower_2}")

                elif vibor == 6:
                    while 1:
                        if tower_3.id != hero_1.id_:
                            print("Эта Башня непренадлежит Вам")
                            break

                        print(f"Вы прибыли на {tower_3.name}, гарнизон {tower_3.units} солдат, уровень: {tower_3.level}, набирает солдат до {tower_3.power}")
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон на башне\
                            \n3.Повысить уровень Башни\
                            \n4.Покинуть Башню\
                            \n5.Информация о Башне")
                        vibor = int(input("Что будем делать Милорд?:"))
                        
                        if vibor == 1:
                            if tower_3.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Башни, Вам доступно {tower_3.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > tower_3.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        tower_3.units -= num_solder
                                        hero_1.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_1.units} солдат")
                                        break
                            else:
                                print(f"На {tower_3} нет солдат")         
                            
                        if vibor == 2:
                            if hero_1.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_1.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_1.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        tower_3.units += num_solder
                                        hero_1.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {tower_3.units} солдат")  
                                        break
                            else:
                                print("У Вас нет солдат Милорд\n")
                        
                        if vibor == 3:
                            print("Для улучшения Башни Вам необходимо 100 солдат в гарнизоне башни")
                            if tower_3.units == 100:
                                tower_3.level_up_tower() 
                                tower_3.units = 0 
                            else:
                                print("Недостаточно солдат\n")
                        
                        if vibor == 4:
                            print(f"Вы покидаете {tower_3.name}\n")
                            break
                        if vibor == 5:
                            print(f"\n{tower_3}")

            
                elif vibor == 7:
                    while 1:
                        if tower_4.id != hero_1.id_:
                            print("Эта Башня непренадлежит Вам")
                            break

                        print(f"Вы прибыли на {tower_4.name}, гарнизон {tower_4.units} солдат, уровень: {tower_4.level}, набирает солдат до {tower_4.power}")
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон на башне\
                            \n3.Повысить уровень Башни\
                            \n4.Покинуть Башню\
                            \n5.Информация о Башне")
                        vibor = int(input("Что будем делать Милорд?:"))
                        
                        if vibor == 1:
                            if tower_4.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Башни, Вам доступно {tower_4.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > tower_4.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        tower_4.units -= num_solder
                                        hero_1.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_1.units} солдат")
                                        break
                            else:
                                print(f"На {tower_4} нет солдат")         
                            
                        if vibor == 2:
                            if hero_1.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_1.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_1.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        tower_4.units += num_solder
                                        hero_1.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {tower_4.units} солдат")  
                                        break
                            else:
                                print("У Вас нет солдат Милорд\n")
                        
                        if vibor == 3:
                            print("Для улучшения Башни Вам необходимо 100 солдат в гарнизоне башни")
                            if tower_4.units == 100:
                                tower_4.level_up_tower() 
                                tower_4.units = 0 
                            else:
                                print("Недостаточно солдат\n")
                        
                        if vibor == 4:
                            print(f"Вы покидаете {tower_4.name}\n")
                            break
                        if vibor == 5:
                            print(f"\n{tower_4}")

                if vibor == 8:
                    while 1:
                        print("!!!Да здравствует Милорд!!!\
                            \nМы рады видеть Вас дома")
                        print(castle_1)
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон в Замке\
                            \n3.Повысить уровень Лорда\
                            \n4.Информация о Замке\
                            \n5.Изготовить Катапульту\
                            \n6.Покинуть Замок")
                        vibor = int(input("Что будем делать Милорд?:"))

                        if vibor == 1:
                            if castle_1.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Замка, Вам доступно {castle_1.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > castle_1.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        castle_1.units -= num_solder
                                        hero_1.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_1.units} солдат")
                                        break
                            else:
                                print(f"В {castle_1.name} нет солдат")

                        if vibor == 2:
                            if hero_1.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_1.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_1.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        castle_1.units += num_solder
                                        hero_1.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {castle_1.units} солдат")  
                                        break
                            else:
                                print("\nУ Вас нет солдат Милорд\n")

                        if vibor == 3:
                            print("\nДля улучшения Героя, Вам необходимо 200 солдат в составе армии героя")
                            hero_1.change_level()
                        
                        if vibor == 4:
                            print(f"\ncastle_1")
                            
                        if vibor == 5:
                           
                            if castle_1.units >= 1000:
                                print('\nДля изготовления катапульты необходимо 1000 солдат и время, ожидайте...')
                                castle_1.katapulta_build()
                                castle_1.units -= 1000
                                for i in progress.bar(range(100)):
                                    time.sleep(0.08)
                            else:
                                print("У вас недостаточно солдат")
                        
                        if vibor == 6:
                            print(f"\nВы покидаете {castle_1.name}\n")
                            break
                
                if vibor == 9:
                    while 1:
                        print("Перед нападением на Замок, убедитесь что у Вас есть Катапульта и достаточно большая армия у Лорда\
                            \n1.Атаковать Замок\
                            \n2.Я ещё подумаю")
                        vibor = int(input("Ваше решение:"))
                        if vibor == 2:
                            print('Разумное решение')
                            break
                        if vibor == 1:
                            if castle_1.katapulta == 'Нет':
                                castle_2.units = castle_2.units * 2
                                print(f"Это было очень глупо с Вашей стороны Милорд, атаковать Замок без катапульты это самоубийство\
                                    \nТеперь гарнизон вражеского Замка удвоен")
                                print("=========БИТВА НАЧИНАЕТСЯ=========")
                                print(f"Ваши солдаты полезли на стены, их обстреливают стрелами, они обреченны...\
                                    \nВаших солдат: {hero_1.units} ---против --- {castle_2.units} солдат гарнизона Замка")
                                for i in progress.bar(range(100)):
                                    time.sleep(0.1)
                                if hero_1.units < castle_2.units:
                                    print(f"========БИТВА ЗАВЕРШЕНА======= ")
                                    print(f"Сторона {hero_2.id_} победила")
                                    print("\n================================================")
                                    print(f"Поздравляем Лорда {hero_2.name} с победой")
                                    print("================================================")
                                    pobeda = True
                                    break
                                elif hero_1 > castle_2.units:
                                    print("Ваши солдаты проявили крайнюю степень отчаяния и мужества, они разгромили солдат противника и снесли этот Замок...\
                                        \n...а вообще, вы просто задавили их количеством...")
                                    print(f"========БИТВА ЗАВЕРШЕНА======= ")
                                    print(f"Сторона {hero_1.id_} победила")
                                    print("\n================================================")
                                    print(f"Поздравляем Лорда {hero_1.name} с победой")
                                    print("================================================")
                                    pobeda = True
                                    break
                            elif castle_1.katapulta == 'Да':
                                print(f"Вы очень мудрый стратег Милорд, атаковать Замок с катапультой это одно удовольствие\
                                    \n Гарнизон вражеского Замка остался преждним")
                                print("=========БИТВА НАЧИНАЕТСЯ=========")
                                print(f"Ваши солдаты гуляют по полю, они поют, пьют Эль, и смотрят как катапульта разносит этот Замок в пыль\
                                    \nВ итоге обстрела, 20% гарнизона Замка было уничтожено")
                                castle_2.units = castle_2.units * 0.8
                                print(f"\nВаших солдат: {hero_1.units} ---против --- оставшихся {castle_2.units} солдат гарнизона Замка")
                                for i in progress.bar(range(100)):
                                    time.sleep(0.1)
                                if hero_1.units < castle_2.units:
                                    print("Удивительно, но Ваши солдаты не смогли захватить Замок, видимо они были сильно пьяны...")
                                    print(f"========БИТВА ЗАВЕРШЕНА======= ")
                                    print(f"Сторона {hero_2.id_} победила")
                                    print("\n================================================")
                                    print(f"Поздравляем Лорда {hero_2.name} с победой")
                                    print("================================================")
                                    pobeda = True
                                    break
                                elif hero_1.units > castle_2.units:
                                    print("Несмотря на Ваш численный перевес и предварительный обстрел, солдаты противника дали сильный отпор,\
                                        \nнеся тяжелые потери, мы Захватили Замок, поздравляю Вас Милорд!!!")
                                    print(f"========БИТВА ЗАВЕРШЕНА======= ")
                                    print(f"Сторона {hero_1.id_} победила")
                                    print("\n================================================")
                                    print(f"Поздравляем Лорда {hero_1.name} с победой")
                                    print("================================================")
                                    pobeda = True
                                    break

                                                        


            print(f'\n------------День {day}------------')
            
            
            print('\nСписок Башень')
            if tower_1.id != hero_1.id_:
                print(tower_1)
                print("--------------------------")
            if tower_2.id != hero_1.id_:
                print(tower_2)
                print("--------------------------")
            if tower_3.id != hero_1.id_:
                print(tower_3)
                print("--------------------------")
            if tower_4.id != hero_1.id_:
                print(tower_4)
                print("--------------------------")

            print(f"\nХод игрока {hero_2.name}")
            print(hero_2)
            print(castle_2)
            print(f"Башни в имении Лорда, сторона '{hero_2.id_}':")
            print('-------------------------------')
            if tower_1.id == hero_2.id_:
                print(tower_1)
                print("--------------------------")
            if tower_2.id == hero_2.id_:
                print(tower_2)
                print("--------------------------")
            if tower_3.id == hero_2.id_:
                print(tower_3)
                print("--------------------------")
            if tower_4.id == hero_2.id_:
                print(tower_4)
                print("--------------------------")
            
            
            if tower_1.id == hero_2.id_:
                print(f"\n4.{tower_1.name} это башня в Ваших владениях, Выберите чтобы посетить её")
            if tower_2.id == hero_2.id_:
                print(f"\n5.{tower_2.name} это башня в Ваших владениях, Выберите чтобы посетить её")
            if tower_3.id == hero_2.id_:
                print(f"\n6.{tower_3.name} это башня в Ваших владениях, Выберите чтобы посетить её")
            if tower_4.id == hero_2.id_:
                print(f"\n7.{tower_4.name} это башня в Ваших владениях, Выберите чтобы посетить её")
            
            while 1:
                if pobeda == True:
                    break
                print(f"\nЧто Вы будете делать Милорд?:\
                    \n0.Передать ход противнику\
                    \n1.Захватить Башню\
                    \n2.Использовать Сверхсилу\
                    \n3.Показать информацию о Лорде, Замке и башнях\
                    \n4,5,6,7 действия с Башнями в ваших владениях\
                    \n8.Отправиться в Замок Лорда\
                    \n9.Атаковать вражеский замок (если Вы не сможете захватить Замок, Вам засчитается поражение)")
                vibor = int(input('\nВаш выбор Милорд:'))

                if vibor == 0:
                    start = time.time()
                    print(f"Ход передан Лорду {hero_1.name}")
                    time.sleep(3)
                    break

                if vibor == 1:
                    print(f"На какую Башню Вы хотите напасть Милорд?:\n")
                    if tower_1.id == "Нейтральная" and tower_1.id != hero_2.id_:
                        print(f"1. {tower_1}")
                        print("--------------------------")
                    if tower_2.id == "Нейтральная" and tower_2.id != hero_2.id_:
                        print(f"2. {tower_2}")
                        print("--------------------------")
                    if tower_3.id == "Нейтральная" and tower_3.id != hero_2.id_:
                        print(f"3. {tower_3}")
                        print("--------------------------")
                    if tower_4.id == "Нейтральная" and tower_4.id != hero_2.id_:
                        print(f"4. {tower_4}")
                        print("--------------------------")

                    vibor_ = int(input("Решайтесь Милорд:"))

                    if vibor_ == 1:
                        if tower_1.id == hero_2.id_:
                            print("Это Башня уже Ваша!")
                            continue
                        
                        start = time.time()
                        print("\n!!!Битва началась!!!")
                        time.sleep(5)
                        
                        if hero_2.units < tower_1.units:
                            print("Сожалею Милорд, но эту битву Вы проиграли")
                            print(f'Ваши потери сотавили {hero_2.units} солдат')
                            tower_1.units -= hero_2.units
                            hero_2.units = 0
                            break 
                        else:
                            print(f"\nУ Вас {hero_2.units} солдат .vs. {tower_1.units} солдат противника")
                            print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_1.name} в Ваших владениях.")
                            print(f"Потери в битве составили {hero_2.units-(hero_2.units-tower_1.units)} солдат")
                            hero_2.units -= tower_1.units
                            tower_1.units = 0
                            tower_1.id = hero_2.id_
                            break
                        # zahvat_tower(tower_1.name, tower_1.units, tower_1.id, hero_1.units, hero_1.id_)

                    if vibor_ == 2:
                        if tower_2.id == hero_2.id_:
                            print("Это Башня уже Ваша!")
                            continue
                        
                        start = time.time()
                        print("\n!!!Битва началась!!!")
                        time.sleep(5)
                        
                        if hero_2.units < tower_2.units:
                            print("Сожалею Милорд, но эту битву Вы проиграли")
                            print(f'Ваши потери составили {hero_2.units} солдат')
                            tower_2.units -= hero_2.units
                            hero_2.units = 0
                            break 
                        else:
                            print(f"\nУ Вас {hero_2.units} солдат .vs. {tower_2.units} солдат противника")
                            print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_2.name} в Ваших владениях.")
                            print(f"Потери в битве составили {hero_2.units-(hero_2.units-tower_2.units)} солдат")
                            hero_2.units -= tower_2.units
                            tower_2.units = 0
                            tower_2.id = hero_2.id_
                            break
                    
                    if vibor_ == 3:
                        if tower_3.id == hero_2.id_:
                            print("Это Башня уже Ваша!")
                            continue
                        
                        start = time.time()
                        print("\n!!!Битва началась!!!")
                        time.sleep(5)
                        
                        if hero_2.units < tower_3.units:
                            print("Сожалею Милорд, но эту битву Вы проиграли")
                            print(f'Ваши потери сотавили {hero_2.units} солдат')
                            tower_3.units -= hero_2.units
                            hero_2.units = 0
                            break 
                        else:
                            print(f"\nУ Вас {hero_2.units} солдат .vs. {tower_3.units} солдат противника")
                            print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_3.name} в Ваших владениях.")
                            print(f"Потери в битве составили {hero_2.units-(hero_2.units-tower_3.units)} солдат")
                            hero_2.units -= tower_3.units
                            tower_3.units = 0
                            tower_3.id = hero_2.id_
                            break

                    if vibor_ == 4:
                        if tower_4.id == hero_2.id_:
                            print("Это Башня уже Ваша!")
                            continue
                        
                        start = time.time()
                        print("\n!!!Битва началась!!!")
                        time.sleep(5)
                        
                        if hero_2.units < tower_4.units:
                            print("Сожалею Милорд, но эту битву Вы проиграли")
                            print(f'Ваши потери сотавили {hero_2.units} солдат')
                            tower_4.units -= hero_2.units
                            hero_2.units = 0
                            break 
                        else:
                            print(f"\nУ Вас {hero_2.units} солдат .vs. {tower_4.units} солдат противника")
                            print(f"Поздравляю!!! Милорд! Вы Победили в этом сражении, теперь {tower_4.name} в Ваших владениях.")
                            print(f"Потери в битве составили {hero_2.units-(hero_2.units-tower_4.units)} солдат")
                            hero_2.units -= tower_4.units
                            tower_4.units = 0
                            tower_4.id = hero_2.id_
                            break

                elif vibor == 2:
                    start = time.time()
                    hero_2.use_superpower()    
                    time.sleep(3)
                    continue

                elif vibor == 3:
                    start = time.time()
                    print(hero_2)
                    print(castle_2)
                    if tower_1.id == hero_2.id_:
                        print(tower_1)
                    if tower_2.id == hero_2.id_:
                        print(tower_2)
                    if tower_3.id == hero_2.id_:
                        print(tower_3)
                    if tower_4.id == hero_2.id_:
                        print(tower_4)
                    time.sleep(3)
                    continue
                
                elif vibor == 4:
                    while 1:
                        if tower_1.id != hero_2.id_:
                            print("Эта Башня непренадлежит Вам")
                            break
                        print(f"Вы прибыли на {tower_1.name}, гарнизон {tower_1.units} солдат, уровень: {tower_1.level}, набирает солдат до {tower_1.power}")
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон на башне\
                            \n3.Повысить уровень Башни\
                            \n4.Покинуть Башню\
                            \n5.Информация о Башне")
                        vibor = int(input("Что будем делать Милорд?:"))
                        
                        if vibor == 1:
                            if tower_1.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Башни, Вам доступно {tower_1.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > tower_1.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        tower_1.units -= num_solder
                                        hero_2.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_2.units} солдат")
                                        break
                            else:
                                print(f"На {tower_1} нет солдат")         
                            
                        if vibor == 2:
                            if hero_2.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_2.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_2.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        tower_1.units += num_solder
                                        hero_2.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {tower_1.units} солдат")  
                                        break
                            else:
                                print("У Вас нет солдат Милорд\n")
                        
                        if vibor == 3:
                            print("Для улучшения Башни Вам необходимо 100 солдат в гарнизоне башни")
                            if tower_1.units >= 100:
                                tower_1.level_up_tower()  
                                tower_1.units -= 100
                            else:
                                print("Недостаточно солдат\n")
                        
                        if vibor == 4:
                            print(f"Вы покидаете {tower_1.name}\n")
                            break
                        if vibor == 5:
                            print(f"\n{tower_1}")

                elif vibor == 5:
                    while 1:
                        if tower_2.id != hero_2.id_:
                            print("Эта Башня непренадлежит Вам")
                            break

                        print(f"Вы прибыли на {tower_2.name}, гарнизон {tower_2.units} солдат, уровень: {tower_2.level}, набирает солдат до {tower_2.power}")
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон на башне\
                            \n3.Повысить уровень Башни\
                            \n4.Покинуть Башню\
                            \n5.Информация о Башне")
                        vibor = int(input("Что будем делать Милорд?:"))
                        
                        if vibor == 1:
                            if tower_2.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Башни, Вам доступно {tower_2.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > tower_2.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        tower_2.units -= num_solder
                                        hero_2.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_2.units} солдат")
                                        break
                            else:
                                print(f"На {tower_2} нет солдат")         
                            
                        if vibor == 2:
                            if hero_2.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_2.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_2.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        tower_2.units += num_solder
                                        hero_2.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {tower_2.units} солдат")  
                                        break
                            else:
                                print("У Вас нет солдат Милорд\n")
                        
                        if vibor == 3:
                            print("Для улучшения Башни Вам необходимо 100 солдат в гарнизоне башни")
                            if tower_2.units >= 100:
                                tower_2.level_up_tower()  
                                tower_2.units -= 100
                            else:
                                print("Недостаточно солдат\n")
                        
                        if vibor == 4:
                            print(f"Вы покидаете {tower_2.name}\n")
                            break
                        if vibor == 5:
                            print(f"\n{tower_2}")

                elif vibor == 6:
                    while 1:
                        if tower_3.id != hero_2.id_:
                            print("Эта Башня непренадлежит Вам")
                            break

                        print(f"Вы прибыли на {tower_3.name}, гарнизон {tower_3.units} солдат, уровень: {tower_3.level}, набирает солдат до {tower_3.power}")
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон на башне\
                            \n3.Повысить уровень Башни\
                            \n4.Покинуть Башню\
                            \n5.Информация о Башне")
                        vibor = int(input("Что будем делать Милорд?:"))
                        
                        if vibor == 1:
                            if tower_3.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Башни, Вам доступно {tower_3.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > tower_3.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        tower_3.units -= num_solder
                                        hero_2.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_2.units} солдат")
                                        break
                            else:
                                print(f"На {tower_3} нет солдат")         
                            
                        if vibor == 2:
                            if hero_2.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_2.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_2.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        tower_3.units += num_solder
                                        hero_2.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {tower_3.units} солдат")  
                                        break
                            else:
                                print("У Вас нет солдат Милорд\n")
                        
                        if vibor == 3:
                            print("Для улучшения Башни Вам необходимо 100 солдат в гарнизоне башни")
                            if tower_3.units >= 100:
                                tower_3.level_up_tower()  
                                tower_3.units -= 100
                            else:
                                print("Недостаточно солдат\n")
                        
                        if vibor == 4:
                            print(f"Вы покидаете {tower_3.name}\n")
                            break
                        if vibor == 5:
                            print(f"\n{tower_3}")

            
                elif vibor == 7:
                    while 1:
                        if tower_4.id != hero_2.id_:
                            print("Эта Башня непренадлежит Вам")
                            break

                        print(f"Вы прибыли на {tower_4.name}, гарнизон {tower_4.units} солдат, уровень: {tower_4.level}, набирает солдат до {tower_4.power}")
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон на башне\
                            \n3.Повысить уровень Башни\
                            \n4.Покинуть Башню\
                            \n5.Информация о Башне")
                        vibor = int(input("Что будем делать Милорд?:"))
                        
                        if vibor == 1:
                            if tower_4.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Башни, Вам доступно {tower_4.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > tower_4.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        tower_4.units -= num_solder
                                        hero_2.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_2.units} солдат")
                                        break
                            else:
                                print(f"На {tower_4} нет солдат")         
                            
                        if vibor == 2:
                            if hero_2.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_2.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_2.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        tower_4.units += num_solder
                                        hero_2.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {tower_4.units} солдат")  
                                        break
                            else:
                                print("У Вас нет солдат Милорд\n")
                        
                        if vibor == 3:
                            print("Для улучшения Башни Вам необходимо 100 солдат в гарнизоне башни")
                            if tower_4.units >= 100:
                                tower_4.level_up_tower()  
                                tower_4.units -= 100
                            else:
                                print("Недостаточно солдат\n")
                        
                        if vibor == 4:
                            print(f"Вы покидаете {tower_4.name}\n")
                            break
                        if vibor == 5:
                            print(f"\n{tower_4}")

                if vibor == 8:
                    while 1:
                        print("!!!Да здравствует Милорд!!!\
                            \nМы рады видеть Вас дома")
                        print(castle_2)
                        print("Здесь Вы можете:\
                            \n1.Забрать гарнизон с собой\
                            \n2.Оставить гарнизон в Замке\
                            \n3.Повысить уровень Лорда\
                            \n4.Информация о Замке\
                            \n5.Изготовить Катапульту\
                            \n6.Покинуть Замок")
                        vibor = int(input("Что будем делать Милорд?:"))

                        if vibor == 1:
                            if castle_2.units != 0:
                                print(f"Сколько солдат Вы хотите забрать с Замка, Вам доступно {castle_2.units} солдат")
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > castle_2.units:
                                        print("Здесь нет столько солдат Милорд")
                                    else:
                                        castle_2.units -= num_solder
                                        hero_2.units += num_solder
                                        print(f"Вы забрали с собой {num_solder} солдат, теперь с Вами {hero_2.units} солдат")
                                        break
                            else:
                                print(f"В {castle_2.name} нет солдат")

                        if vibor == 2:
                            if hero_2.units != 0:
                                print(f"Сколько солдат Вы хотите оставить в гарнизоне Башни, вам доступно {hero_2.units} солдат") 
                                while 1:
                                    num_solder = int(input("Укажите количество солдат:"))
                                    if num_solder > hero_2.units:
                                        print("У Вас нет столько солдат")
                                    else:
                                        castle_2.units += num_solder
                                        hero_2.units -= num_solder
                                        print(f"Вы оставили {num_solder} солдат, теперь в гарнизоне Башни {castle_2.units} солдат")  
                                        break
                            else:
                                print("\nУ Вас нет солдат Милорд\n")

                        if vibor == 3:
                            print("\nДля улучшения Героя, Вам необходимо 200 солдат в составе армии героя")
                            hero_2.change_level()
                        
                        if vibor == 4:
                            print(f"\ncastle_1")
                            
                        if vibor == 5:
                           
                            if castle_2.units >= 1000:
                                print('\nДля изготовления катапульты необходимо 1000 солдат и время, ожидайте...')
                                castle_2.katapulta_build()
                                castle_2.units -= 1000
                                for i in progress.bar(range(100)):
                                    time.sleep(0.08)
                            else:
                                print("У вас недостаточно солдат")
                        
                        if vibor == 6:
                            print(f"\nВы покидаете {castle_2.name}\n")
                            break
                
                if vibor == 9:
                    while 1:
                        print("Перед нападением на Замок, убедитесь что у Вас есть Катапульта и достаточно большая армия у Лорда\
                            \n1.Атаковать Замок\
                            \n2.Я ещё подумаю")
                        vibor = int(input("Ваше решение:"))
                        if vibor == 2:
                            print('Разумное решение')
                            break
                        if vibor == 1:
                            if castle_2.katapulta == 'Нет':
                                castle_1.units = castle_2.units * 2
                                print(f"Это было очень глупо с Вашей стороны Милорд, атаковать Замок без катапульты это самоубийство\
                                    \nТеперь гарнизон вражеского Замка удвоен")
                                print("=========БИТВА НАЧИНАЕТСЯ=========")
                                print(f"Ваши солдаты полезли на стены, их обстреливают стрелами, они обреченны...\
                                    \nВаших солдат: {hero_2.units} ---против --- {castle_1.units} солдат гарнизона Замка")
                                for i in progress.bar(range(100)):
                                    time.sleep(0.1)
                                if hero_2.units < castle_1.units:
                                    print(f"========БИТВА ЗАВЕРШЕНА======= ")
                                    print(f"Сторона {hero_1.id_} победила")
                                    print("\n================================================")
                                    print(f"Поздравляем Лорда {hero_1.name} с победой")
                                    print("================================================")
                                    pobeda = True
                                    break
                                elif hero_2.units > castle_2.units:
                                    print("Ваши солдаты проявили крайнюю степень отчаяния и мужества, они разгромили солдат противника и снесли этот Замок...\
                                        \n...а вообще, вы просто задавили их количеством...")
                                    print(f"========БИТВА ЗАВЕРШЕНА======= ")
                                    print(f"Сторона {hero_2.id_} победила")
                                    print("\n================================================")
                                    print(f"Поздравляем Лорда {hero_2.name} с победой")
                                    print("================================================")
                                    pobeda = True
                                    break
                            elif castle_2.katapulta == 'Да':
                                print(f"Вы очень мудрый стратег Милорд, атаковать Замок с катапультой это одно удовольствие\
                                    \n Гарнизон вражеского Замка остался преждним")
                                print("=========БИТВА НАЧИНАЕТСЯ=========")
                                print(f"Ваши солдаты гуляют по полю, они поют, пьют Эль, и смотрят как катапульта разносит этот Замок в пыль\
                                    \nВ итоге обстрела, 20% гарнизона Замка было уничтожено")
                                castle_1.units = castle_1.units * 0.8
                                print(f"\nВаших солдат: {hero_2.units} ---против --- оставшихся {castle_1.units} солдат гарнизона Замка")
                                for i in progress.bar(range(100)):
                                    time.sleep(0.1)
                                if hero_2.units < castle_1.units:
                                    print("Удивительно, но Ваши солдаты не смогли захватить Замок, видимо они были сильно пьяны...")
                                    print(f"========БИТВА ЗАВЕРШЕНА======= ")
                                    print(f"Сторона {hero_1.id_} победила")
                                    print("\n================================================")
                                    print(f"Поздравляем Лорда {hero_1.name} с победой")
                                    print("================================================")
                                    pobeda = True
                                    break
                                elif hero_2 > castle_1.units:
                                    print("Несмотря на Ваш численный перевес и предварительный обстрел, солдаты противника дали сильный отпор,\
                                        \nнеся тяжелые потери, мы Захватили Замок, поздравляю Вас Милорд!!!")
                                    print(f"========БИТВА ЗАВЕРШЕНА======= ")
                                    print(f"Сторона {hero_2.id_} победила")
                                    print("\n================================================")
                                    print(f"Поздравляем Лорда {hero_2.name} с победой")
                                    print("================================================")
                                    pobeda = True
                                    break
if __name__ == "__main__":
    main()