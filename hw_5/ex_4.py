with open("text_data.txt", "r", encoding="utf-8") as f:
  text = f.read()

def zip_text(text):
  zipped = ""
  temp_dict = {}
  for i in range(0, len(text)):
    if i == 0:
      temp_dict[text[i]] = 1
    elif i == len(text) - 1:
      temp_dict[text[i]] += 1
      zipped += f"{temp_dict[text[i]]}{text[i]}"
    elif text[i] == text[i - 1]:
      temp_dict[text[i]] += 1
    elif text[i] != text[i - 1]:
      zipped += f"{temp_dict[text[i - 1]]}{text[i - 1]}"
      temp_dict = {}
      temp_dict[text[i]] = 1
  return zipped

def unzip_text(text):
  factor = ""
  res = ""
  for el in text:
    if el.isdigit():
      factor += el
    else:
      res += int(factor) * el
      factor = ""
  return res

zipped_text = zip_text(text)

with open("text_res.txt", "w", encoding="utf-8") as f:
  f.write(zipped_text)

print(unzip_text(zipped_text))
