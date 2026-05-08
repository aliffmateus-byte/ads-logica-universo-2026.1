# Exercício 15: Desafio – Maior Nota
maior_nota = -1 # Começa com um valor impossível para ser substituído

for i in range(1, 6):
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    if nota > maior_nota:
        maior_nota = nota

print(f"A maior nota encontrada no grupo foi: {maior_nota}")

