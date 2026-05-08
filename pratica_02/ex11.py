# Exercício 11: Classificação de Turma
qtd_alunos = int(input("Quantos alunos tem na turma? "))
aprovados = 0
recuperacao = 0
reprovados = 0

for i in range(qtd_alunos):
    media = float(input(f"Digite a média do aluno {i+1}: "))
    if media >= 7:
        aprovados += 1
    elif 4 <= media < 7:
        recuperacao += 1
    else:
        reprovados += 1

print(f"\nTotal Aprovados: {aprovados}")
print(f"Total em Recuperação: {recuperacao}")
print(f"Total Reprovados: {reprovados}")

