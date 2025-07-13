from game import JogoDaVelha
from ai import IA
from interface import mostrar_tabuleiro, obter_jogada_humano, mostrar_resultado

def main():
    jogo = JogoDaVelha()
    ia = IA()
    
    print("Bem-vindo ao Jogo da Velha contra IA!")
    print("Você é o jogador X\n")
    
    while not jogo.estado_jogo():
        mostrar_tabuleiro(jogo.tabuleiro)
        
        if jogo.jogador_atual == 'X':
            jogada = obter_jogada_humano(jogo)
        else:
            print("\nIA pensando...")
            jogada = ia.melhor_jogada(jogo)
            print(f"IA jogou na posição {jogada}")
        
        jogo.fazer_jogada(jogada)
    
    mostrar_tabuleiro(jogo.tabuleiro)
    mostrar_resultado(jogo.vencedor)
    
    if input("\nJogar novamente? (s/n): ").lower() == 's':
        main()
    else:
        print("Obrigado por jogar!")

if __name__ == "__main__":
    main()