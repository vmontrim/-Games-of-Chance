import random

money = 100

def coin_flip(call, amount):
  
  if random.randint(1,2) == 1:
    coin_toss = "Heads"
  else:
    coin_toss = "Tails"
  if call == coin_toss:
    result = "won"
    total_amount = money + amount
  else:
    result = "lost"
    total_amount = money - amount
  
  print(
    f"You flipped {coin_toss} and you called {call}! You {result} and now have {total_amount}"
  )
  
coin_flip("Heads", 10)
