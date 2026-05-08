# Exercício 4: Verificador de Acesso
idade = int(input("Digite a idade do usuário: "))
experiencia = int(input("Digite os anos de experiência: "))

# A regra lógica: (Idade >= 18) E (Experiência >= 2)
# O resultado será True se ambos forem verdadeiros, ou False caso contrário.
pode_acessar = (idade >= 18) and (experiencia >= 2)

print(f"Acesso permitido: {pode_acessar}")
