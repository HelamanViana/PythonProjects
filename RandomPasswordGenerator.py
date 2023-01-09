import random
passlen = int(input('Digite o comprimento da senha: '))
senha = 'qwertyuiopasdfghjklçzxcvbnm1234567890@#$%&*'
password = "".join(random.sample(senha, passlen))
print(password)
