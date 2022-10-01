import random
randomint = random.randint(1,100)

user = int(input('pick a number from 0 - 100 :'))

if user < 0:
  print('your answer is too low')

elif user>100:
  print('your answer is too high')

else:
  print('your answer is correct')

