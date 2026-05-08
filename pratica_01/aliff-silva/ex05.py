# Exercício 5: Desafio do Download
tamanho_mb = float(input("Tamanho do arquivo (MB): "))
velocidade_mbps = float(input("Velocidade da internet (Mbps): "))

# 1. Calcular tempo total em segundos
# Fórmula: Tamanho / (Velocidade / 8)
tempo_segundos = tamanho_mb / (velocidade_mbps / 8)

# 2. Converter para minutos inteiros e segundos restantes
minutos = int(tempo_segundos // 60)
segundos_restantes = int(tempo_segundos % 60)

print(f"{minutos} minutos e {segundos_restantes} segundos")

