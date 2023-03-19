
#1
try:
    def gcd_fun(x, y):
        if(y == 0):  
            return x  
        else: 
            return gcd_fun(y, x % y)
    def Input():
        x =int(input("Enter the first number: "))   
        y =int(input("Enter the second number: "))
        num = gcd_fun(x, y)
        print("GCD of two number is: ") 
        print(num)
except:
    print("Error")
finally:
    Input()


 #2

from random import randint


def game():
  rand = randint(1000, 9999)

  listNumR = []
  xr = rand // 1000
  yr = (rand // 100) % 10
  zr = (rand // 10) % 10
  cr = rand % 10
  listNumR.append(xr)
  listNumR.append(yr)
  listNumR.append(zr)
  listNumR.append(cr)
  print(listNumR)

  while True:
    number = int(input("Enter number 4x: "))
    listNum = []
    x = number // 1000
    y = (number // 100) % 10
    z = (number // 10) % 10
    c = number % 10
    listNum.append(x)
    listNum.append(y)
    listNum.append(z)
    listNum.append(c)
    print(listNum)

    a = 0
    while a <= 3:
        if listNum[a] == listNumR[a]:
            print(a + 1, "цифра совпала и на своем месте")
            a += 1

    for i in listNumR:
      for j in listNum:
        if i == j:
          print(i, "такая цифра есть")
    if listNum == listNumR:
      print("WIN")
      print("ещё разок ?")
      start = int(input("1= да, 2 = нет"))
      print()

      if start == 1:
        game()
      else:
        break


print("Угадай число:")
game()



