nota = -1
while nota < 0 or nota > 10:
    nota = float(input("Digite uma nota entre 0 e 10: "))
    if nota < 0 or nota > 10:
        print("Valor inválido! Tente novamente.")

print(f"Nota {nota} registrada com sucesso!")

