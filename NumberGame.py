import random
number = random.randint(1, 10)
for i in range(0, 3):
    user = int(input("Advinhe o número: "))
    if user == number:
        print("Parabéns!")
        print(f'Você acertou o número. O número era {number}!')
        break
    if user != number:
        print(f'Que pena! O número correto era {number}!')
    break