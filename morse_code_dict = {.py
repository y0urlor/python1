def is_valid_card(card_number):
  if len(card_number) not in [13, 15, 16, 19]:
    return False
  for char in card_number:
    if not char.isdigit():
      return False
  sum = 0
  for i in range(len(card_number) - 1, -1, -2):
    sum += int(card_number[i])
  for i in range(len(card_number) - 2, -1, -2):
    digit = int(card_number[i]) * 2
    sum += digit // 10 + digit % 10

  if sum % 10 != 0:
    return False

  prefixes = {
    "4": ["Visa"],
    "5": ["MasterCard"],
    "6": ["Discover"],
    "37": ["American Express"],
  }
  prefix = card_number[0]
  if prefix not in prefixes:
    return False
  return True
card_number = input("Введіть номер картки: ")
if is_valid_card(card_number):
  print("Номер дійсний.")
else:
  print("Номер недійсний.")
