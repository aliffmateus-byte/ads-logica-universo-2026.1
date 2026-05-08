# Exercício 2: Faixa Etária Essencial
idade = int(input("Digite a idade: "))

if idade < 18:
    print("Classificação: Menor de idade.")
elif 18 <= idade <= 59:
    print("Classificação: Maior de idade.")
else:
    print("Classificação: Idoso.")

