class IA:
    def __init__(self, jogador='O'):
        self.jogador = jogador
    
    def melhor_jogada(self, jogo):
        _, melhor_movimento = self.minimax(jogo, self.jogador, 0, float('-inf'), float('inf'))
        return melhor_movimento
    
    def minimax(self, estado, jogador, profundidade, alpha, beta):
        estado.verificar_vencedor()
        
        if estado.vencedor == self.jogador:
            return 10 - profundidade, None
        elif estado.vencedor == 'X':  
            return profundidade - 10, None
        elif estado.vencedor == 'E':  
            return 0, None
        
        if jogador == self.jogador:
            melhor_valor = float('-inf')
            melhor_mov = None
        else:
            melhor_valor = float('inf')
            melhor_mov = None
        
        for movimento in estado.jogadas_disponiveis():
            estado.tabuleiro[movimento] = jogador
            estado.jogadas += 1
            
            valor, _ = self.minimax(
                estado, 
                'X' if jogador == 'O' else 'O', 
                profundidade + 1, 
                alpha, 
                beta
            )
            
            estado.tabuleiro[movimento] = ' '
            estado.jogadas -= 1
            estado.vencedor = None
            
            if jogador == self.jogador:  # MAX
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_mov = movimento
                alpha = max(alpha, melhor_valor)
            else:  # MIN
                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_mov = movimento
                beta = min(beta, melhor_valor)
            
            if alpha >= beta:
                break
        
        return melhor_valor, melhor_mov