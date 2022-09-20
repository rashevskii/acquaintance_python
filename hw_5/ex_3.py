def print_field(field):
  count = 1
  for i in range(0, len(field)):
    if count % 3 != 0:
      print(f" {field[i][1]} ", end="")
    else:
      print(f" {field[i][1]} ")
    count += 1

def set_sign(field, position, sign):
  field[position - 1][1] = sign

def check_win(field):
  if (field[0][1] == field[1][1] == field[2][1] == "0" or field[0][1] == field[1][1] == field[2][1] == "x") or \
  (field[3][1] == field[4][1] == field[5][1] == "0" or field[3][1] == field[4][1] == field[5][1] == "x") or \
  (field[6][1] == field[7][1] == field[8][1] == "0" or field[6][1] == field[7][1] == field[8][1] == "x") or \
  (field[0][1] == field[3][1] == field[6][1] == "0" or field[0][1] == field[3][1] == field[6][1] == "x") or \
  (field[1][1] == field[4][1] == field[7][1] == "0" or field[1][1] == field[4][1] == field[7][1] == "x") or \
  (field[2][1] == field[5][1] == field[8][1] == "0" or field[2][1] == field[5][1] == field[8][1] == "x") or \
  (field[0][1] == field[4][1] == field[8][1] == "0" or field[0][1] == field[4][1] == field[8][1] == "x") or \
  (field[2][1] == field[4][1] == field[6][1] == "0" or field[2][1] == field[4][1] == field[6][1] == "x"):
    return True

def check_empty_position(field, position):
  return field[position - 1][1] == "*"

def make_step(position, field, gamers, current_gamer):
  if position < 1 or position > 9:
    print(f"Ход {gamers[current_gamer]} повторяется, т.к. вы ввели некорректную позицию: {position}")
    return False
  elif not(check_empty_position(field, position)):
    print("Ячейка уже занята!")
    return False
  else:
    set_sign(field, position, gamers[current_gamer])
    print_field(field)
    return True

def game():
  game_field = [
    [1, "*"], [2, "*"], [3, "*"], 
    [4, "*"], [5, "*"], [6, "*"], 
    [7, "*"], [8, "*"], [9, "*"]
  ]
  gamers = {
    1: "0",
    2: "x"
  }
  current_gamer = None
  steps = 1
  has_win = False
  print("Игра началась!")
  print("Игровое поле:")
  print_field(game_field)
  while not(has_win):
    if steps % 2 != 0:
      current_gamer = 1
      position = int(input("Ходят нолики. Введите номер позиции в поле от 1 до 9: "))
      if make_step(position, game_field, gamers, current_gamer):
        has_win = check_win(game_field)
        steps += 1
    else:
      current_gamer = 2
      position = int(input("Ходят крестики. Введите номер позиции в поле от 1 до 9: "))
      if make_step(position, game_field, gamers, current_gamer):
        has_win = check_win(game_field)
        steps += 1
  else:
    print(f"Победил игрок, играющий за {gamers[current_gamer]}!")


game()
