n = int(input("Введите количество монет: "))

coins = []

for i in range(n):
  coin = int(input(f"Введите состояниние понеты{i + 1} (0 - решка, 1 - герб): "))
  coins.append(coin)
  
  # Подсчет решек и гербов

tails_count = coins.count(0)
eagle_count = coins.count(1)

print (f"Минимальное количество переворотов: {min(tails_count, eagle_count)}")