soma_pares = 0
for i in range(1, 9):
    num = int(input(f"Digite o {i}º número inteiro: "))
    if num % 2 == 0:
        soma_pares += num

print(f"A soma dos números pares digitados é: {soma_pares}")

