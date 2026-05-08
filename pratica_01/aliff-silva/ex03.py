# Exercício 3: Divisão Justa
fatias = int(input("Número total de fatias de pizza: "))
programadores = int(input("Número de programadores na equipe: "))

# Cálculo usando divisão inteira (//) e resto da divisão (%)
fatias_por_pessoa = fatias // programadores
sobra = fatias % programadores

print(f"Cada programador comerá {fatias_por_pessoa} fatias inteiras.")
print(f"Sobraram {sobra} fatias na caixa.")

