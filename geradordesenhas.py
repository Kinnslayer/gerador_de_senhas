import random, string

tamanho = int(input("Digite o tamanho de senha que deseja ser gerado: "))

chars = string.ascii_letters + string.digits + "!@#$%&*()-=+,.:/?"

rnd = random.SystemRandom()

print("".join(rnd.choice(chars) for i in range(tamanho)))