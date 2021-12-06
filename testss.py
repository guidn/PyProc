#The Last One


class Controle_Remoto:
    def __init__(self, cor, altura, profundidade, largura):
        self.cor = cor
        self.altura = altura
        self.profundidade = profundidade
        self.largura = largura
        
        
controle = Controle_Remoto ("preto", "180", "50", "10")
print(controle.cor)