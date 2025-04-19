import random
print('1) Rock')
print('2) Paper')
print('3) Scissor')
n=int(input('\nEnter your choice = '))
if n==1:
  print('You chose Rock')
elif n==2:
  print('You chose Paper')
elif n==3:
  print('You chose Scissor')
else:
  print('Invalid entry')
  exit()
pc=random.randint(1,3)
if pc==1:
  print('PC Chose rock')
elif pc==2:
  print('PC chose Paper')
else:
  print('Pc chose Scissor')

if n==pc:
  print('TIE')
elif (n==1 and pc==3) or (n==2 and pc==1) or (n==3 and pc==2):
  print('YOU WON')
else:
  print('YOU LOST')
exit()