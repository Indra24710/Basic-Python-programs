print("welcome to Rock Paper Scissors")
print("R:ROCK")
print("S:SCISSORS")
print("P:PAPER")
print("X=EXIT")
print("lets begin")
i=''
while i!='X':
 from random import randint
 n=randint(1,4)
 if n==1:
     i=input()
     print("R")
     if i=='S':
      print("you lose")
     elif i=='P':
      print("you win")
     elif i=='R':
      print("draw") 
 elif n==2:
      i=input()
      print("S")
      if i=='P':
       print("you lose")
      elif i=='R':
       print("you win")
      elif i=='R':
       print("draw") 
 elif n==3:
      i=input()
      print("P")
      if i=='R':
       print("you lose")
      elif i=='S':
       print("you win")
      elif i=='R':
       print("draw") 
