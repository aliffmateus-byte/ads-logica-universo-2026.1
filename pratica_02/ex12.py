# Exercício 12: Registro de Compras
total_gasto = 0
continuar = "S"

while continuar.upper() == "S":
    valor = float(input("Digite o valor da compra: R$ "))
    total_gasto += valor
    continuar = input("Deseja continuar cadastrando? (S/N): ")

print(f"Total acumulado das compras: R$ {total_gasto:.2f}")

