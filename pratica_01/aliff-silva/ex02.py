# Exercício 2: Calculadora de Freelancer
valor_hora = float(input("Valor cobrado por hora: "))
horas_estimadas = float(input("Horas estimadas para conclusão: "))

valor_bruto = valor_hora * horas_estimadas
impostos = valor_bruto * 0.15
valor_liquido = valor_bruto - impostos

print(f"Valor Bruto: R$ {valor_bruto:.2f}")
print(f"Impostos (15%): R$ {impostos:.2f}")
print(f"Valor Líquido: R$ {valor_liquido:.2f}")

