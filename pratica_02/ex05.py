# Exercício 5: Contar Positivos
contador_positivos = 0

for i in range(1, 11):
    num = float(input(f"Digite o {i}º número: "))
    if num > 0:
        contador_positivos += 1

print(f"Total de números positivos: {contador_positivos}")

