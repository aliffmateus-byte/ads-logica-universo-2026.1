# Importando as ferramentas do arquivo funcoes.py do seu grupo
from funcoes import (Cores, FatorEstrategico, ProblemaGUT, PlanoAcao, 
                     limpar_tela, cabecalho, obter_nota)

# --- FUNÇÕES DE FASE (Mantendo a estrutura original do seu grupo) ---

def fase_swot():
    cabecalho("FASE 1: IDENTIFICAÇÃO DE CENÁRIOS (SWOT)")
    fatores = []
    tipos = {"1": "Força", "2": "Fraqueza", "3": "Oportunidade", "4": "Ameaça"}
    
    while True:
        desc = input(f"\n{Cores.BOLD}Descreva o Problema ou Situação:{Cores.RESET} ")
        print(f"Como você classifica isso?")
        for k, v in tipos.items(): print(f"  {k}. {v}")
        
        t_idx = input("Opção (1-4): ")
        tipo = tipos.get(t_idx, "Outro")
        impacto = obter_nota("Nota de Impacto")
        
        fatores.append(FatorEstrategico(desc, tipo, impacto))
        
        continuar = input(f"\n{Cores.AMARELO}Deseja registrar mais algum ponto? (s/n): {Cores.RESET}").lower()
        if continuar != 's': break
    return fatores

def fase_gut():
    cabecalho("FASE 2: ANÁLISE DE PRIORIDADE (GUT)")
    problemas = []
    print(f"{Cores.AMARELO}Dica: Foque nos problemas que trazem mais risco imediato.{Cores.RESET}")
    
    while True:
        desc = input(f"\nQual problema/gargalo vamos priorizar agora? ")
        g = obter_nota("Gravidade (O quão sério é?)")
        u = obter_nota("Urgência (Isso pode esperar?)")
        t = obter_nota("Tendência (Piorará se nada for feito?)")
        
        problemas.append(ProblemaGUT(desc, g, u, t))
        if input(f"\n{Cores.AMARELO}Analisar outro problema? (s/n): {Cores.RESET}").lower() != 's': break
    
    problemas.sort(key=lambda x: x.score, reverse=True)
    return problemas

def main():
    limpar_tela()
    print(f"{Cores.BOLD}{Cores.AZUL}GERENCIADOR DE SOLUÇÕES ESTRATÉGICAS v3.1{Cores.RESET}")
    
    swot = fase_swot()
    limpar_tela()
    print(f"\n{Cores.BOLD}MAPA DE DIAGNÓSTICO:{Cores.RESET}")
    for f in swot: print(f)

    problemas = fase_gut()
    limpar_tela()
    print(f"\n{Cores.BOLD}RANKING DE PRIORIDADES (ORDEM DE ATUAÇÃO):{Cores.RESET}")
    for p in problemas: print(p)

    if problemas:
        cabecalho("FASE 3: ELABORAÇÃO DO PLANO DE RESPOSTA")
        # Foca nos 2 maiores problemas do ranking original
        planos = [PlanoAcao(p.descricao) for p in problemas[:2]]
        
        limpar_tela()
        cabecalho("RELATÓRIO FINAL PARA EXECUÇÃO")
        for plano in planos:
            plano.exibir()
            
    print(f"\n{Cores.VERDE}✔ Processo concluído. Bom trabalho na execução!{Cores.RESET}\n")

if __name__ == "__main__":
    main()
  
