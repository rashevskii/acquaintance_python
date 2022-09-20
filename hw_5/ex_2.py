from random import randint


type_of_game = int((input("Введите режим игры, где 0 - играют люди, 1 - игра с ботом: ")))

candies = 2021
count_steps = 1
lot = randint(1, 2)
if type_of_game == 0:
  # игра людей
  print(f"Старт игры. Начинает игрок № {lot}")
  while candies > 0:
    gamer = "второго" if count_steps % 2 == 0 else "первого"
    count_candies = int(input(f"Ход {gamer} игрока. Осталось {candies} конфет. Введите количество конфет, которые хотите забрать (1 - 28): "))
    if candies >= count_candies:
      candies -= count_candies
      count_steps += 1
    else:
      print(f"Вы не можете взять {count_candies}, так как осталось {candies}")
  else:
    print("Поздравляем! Вы выиграли!")
else:
  # игра с ботом
  # считаем, что игрок под №1 - бот
  bot_or_gamer = "бот" if lot == 1 else "игрок"
  print(f"Старт игры. Начинает {bot_or_gamer}")
  count_steps = lot
  last_step = 0
  while candies > 0:
    if count_steps % 2 != 0:
      if count_steps == 1:
        bot_step = 20
      else:
        if candies > 28:
          bot_step = 29 - last_step
        else:
          bot_step = candies
      candies -= bot_step
      print(f"Ход бота - {bot_step}. Осталось {candies} конфет.")
      if candies == 0:
        print("Выиграл бот!")
      count_steps += 1
    else:
      gamer_step = int(input(f"Ваш ход. Введите количество конфет, которые хотите забрать (1 - 28): "))
      if gamer_step <= 28:
        last_step = gamer_step
        if candies >= gamer_step:
          candies -= gamer_step
          if candies == 0:
            print("Вы победили!")
          count_steps += 1
        else:
          print(f"Вы не можете взять {gamer_step}, так как осталось {candies}")
      else:
        print("Введите число от 1 до 28! ")



