def mostrar_tabuleiro(tabuleiro):
    print("\n  0 | 1 | 2")
    print(" -----------")
    for i in range(0, 9, 3):
        linha = f"{i//3} {tabuleiro[i]} | {tabuleiro[i+1]} | {tabuleiro[i+2]}"
        print(linha)
        if i < 6:
            print(" -----------")

def obter_jogada_humano(jogo):
    while True:
        try:
            jogada = int(input("\nSua jogada [0-8]: "))
            if 0 <= jogada <= 8 and jogo.tabuleiro[jogada] == ' ':
                return jogada
            print("Jogada inválida. Tente novamente.")
        except ValueError:
            print("Digite um número entre 0 e 8.")

def mostrar_resultado(vencedor):
    if vencedor == 'E':
        print("\nEmpate!")
    else:
        print(f"\nJogador {vencedor} venceu!")