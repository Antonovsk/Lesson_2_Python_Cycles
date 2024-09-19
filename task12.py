def guess_numbers():

  S = int(input("Введите сумму чисел S: "))
  P = int(input("Введите произведение чисел P: "))


  for x in range(1, 1000):
    for y in range(1, 1000):
      if x + y == S and x * y == P:
        return x, y

  # Если числа не найдены
  return None, None

# Запуск функции и вывод результата
x, y = guess_numbers()
if x is not None and y is not None:
  print(f"Задуманные числа: {x} и {y}")
else:
  print("Числа не найдены.")