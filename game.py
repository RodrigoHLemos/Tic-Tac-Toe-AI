class JogoDaVelha:
    def __init__(self):
        self.resetar()
    
    def resetar(self):
        self.tabuleiro = [' '] * 9
        self.jogador_atual = 'X'  
        self.vencedor = None
        self.jogadas = 0
    
    def fazer_jogada(self, posicao):
        if self.tabuleiro[posicao] == ' ' and not self.vencedor:
            self.tabuleiro[posicao] = self.jogador_atual
            self.jogadas += 1
            self.verificar_vencedor()
            self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'
            return True
        return False
    
    def verificar_vencedor(self):
        linhas_vencedoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]             
        ]
        
        for linha in linhas_vencedoras:
            a, b, c = linha
            if self.tabuleiro[a] != ' ' and self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c]:
                self.vencedor = self.tabuleiro[a]
                return
        
        if self.jogadas == 9:
            self.vencedor = 'E'  
    
    def jogadas_disponiveis(self):
        return [i for i, celula in enumerate(self.tabuleiro) if celula == ' ']
    
    def estado_jogo(self):
        return self.vencedor is not None

    def verificar_vencedor(self):
        linhas_vencedoras = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], 
            [0, 3, 6], [1, 4, 7], [2, 5, 8], 
            [0, 4, 8], [2, 4, 6]             
        ]
        
        for linha in linhas_vencedoras:
            a, b, c = linha
            if self.tabuleiro[a] != ' ' and self.tabuleiro[a] == self.tabuleiro[b] == self.tabuleiro[c]:
                self.vencedor = self.tabuleiro[a]
                return
        
        if ' ' not in self.tabuleiro:
            self.vencedor = 'E'  