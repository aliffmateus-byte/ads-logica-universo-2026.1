import os

# Cores para o terminal para manter a interface intuitiva
class Cores:
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'

class FatorEstrategico:
    def __init__(self, descricao, tipo, impacto):
        self.descricao = descricao
        self.tipo = tipo
        self.impacto = impacto

    def __str__(self):
        cor = Cores.VERDE if self.tipo in ["Força", "Oportunidade"] else Cores.AMARELO
        return f"{cor}• [{self.tipo.upper():^12}]{Cores.RESET} {self.descricao:<25} | Peso: {self.impacto}/5"

class ProblemaGUT:
    def __init__(self, descricao, g, u, t):
        self.descricao = descricao
        self.score = g * u * t
        self.detalhe = f"G:{g} U:{u} T:{t}"

    def __str__(self):
        aviso = Cores.VERMELHO + " [CRÍTICO]" if self.score > 60 else ""
        return f"{Cores.BOLD}Score: {self.score:>3}{Cores.RESET} | {self.descricao:<30} ({self.detalhe}){aviso}"

class PlanoAcao:
    def __init__(self, problema):
        self.problema = problema
        self.dados = {}
        
        perguntas = {
            "O QUE": ("Ação prática", "Ex: Trocar rolamentos"),
            "POR QUE": ("Justificativa", "Ex: Evitar travamento da máquina"),
            "QUEM": ("Responsável", "Ex: Técnico de Manutenção"),
            "QUANDO": ("Prazo final", "Ex: Próxima segunda-feira"),
            "ONDE": ("Local", "Ex: Linha de Produção A"),
            "COMO": ("Método", "Ex: Lubrificação e substituição"),
            "QUANTO": ("Custo", "Ex: R$ 200,00")
        }

        print(f"\n{Cores.AZUL}{Cores.BOLD}>>> PLANEJANDO SOLUÇÃO PARA: {problema.upper()}{Cores.RESET}")
        for chave, (rotulo, exemplo) in perguntas.items():
            valor = ""
            while not valor:
                valor = input(f" {Cores.BOLD}{chave}{Cores.RESET} ({rotulo}) [{Cores.AMARELO}{exemplo}{Cores.RESET}]: ")
                if not valor: print(f"{Cores.VERMELHO} Erro: Preenchimento obrigatório!{Cores.RESET}")
            self.dados[chave] = valor

    def exibir(self):
        print(f"\n{Cores.VERDE}┌──────────────────────────────────────────────────────────┐")
        print(f"│ FICHA DE AÇÃO: {self.problema[:40]:<41} │")
        print(f"├──────────────────────────────────────────────────────────┤")
        for k, v in self.dados.items():
            print(f"│ {k:<7}: {v[:47]:<48} │")
        print(f"└──────────────────────────────────────────────────────────┘{Cores.RESET}")

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def cabecalho(titulo):
    print(f"\n{Cores.AZUL}{'='*60}\n{titulo.center(60)}\n{'='*60}{Cores.RESET}")

def obter_nota(msg):
    while True:
        try:
            nota = int(input(f"  {msg} (1-5): "))
            if 1 <= nota <= 5: return nota
            print(f"{Cores.VERMELHO}  Digite uma nota válida entre 1 e 5!{Cores.RESET}")
        except ValueError:
            print(f"{Cores.VERMELHO}  Entrada inválida! Use apenas números.{Cores.RESET}")

