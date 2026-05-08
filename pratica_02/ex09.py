salario = float(input("Digite o salário atual: "))

if salario <= 1500:
    novo_salario = salario * 1.15
elif salario <= 3000:
    novo_salario = salario * 1.10
else:
    novo_salario = salario * 1.05

print(f"Seu novo salário com reajuste é: R$ {novo_salario:.2f}")

