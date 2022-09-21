def count_char(string):
  target = "Р"
  res_list = []
  count = 0
  for i in range(0, len(string)):
    if i == (len(string) - 1):
      if string[i] == target:
        count += 1
      res_list.append(count)
    elif string[i] == target:
      count += 1
    elif string[i] != target:
      res_list.append(count)
      count = 0
  print(max(res_list))

count_char("ООООРРРРОРОРРРРРРРРООРОРОРРРРРРРРРРРРРРРРРРРРРРРРРРРРРРР")
