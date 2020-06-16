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
    "You flipped a %s and you called %s! You %s and now have $%.2f"
    %(coin_toss, call, result, total_amount)
  )
  
coin_flip("Heads", 10)

