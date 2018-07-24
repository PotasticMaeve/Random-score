
import random
import os

scorekakak = 0
scoreadik = 0

def main():
  global scorekakak, scoreadik
  os.system("clear")
  print("=====")
  print("Score Kakak : " + str(scorekakak))
  print("Score Adik : " + str(scoreadik))
  print("=====")
  kakak = random.randint(1,10)
  adik = random.randint(1,10)
  if (kakak > adik): 
    print("Kakak menang!")
    scorekakak += 1
  else:
    print("Adik menang!")
    scoreadik += 1
  print("")
  dummy = raw_input("tekan tombol enter untuk mencoba lagi")
  main()

main()
