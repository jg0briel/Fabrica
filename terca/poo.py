class Garrafa:
    def __init__(self, tamanho, cor, marca):
        self.tamanho = tamanho
        self.cor = cor
        self.marca = marca

    def __str__(self):
        return f'oi, eu sou a garrafa de tamanho {self.tamanho} da marca {self.marca}'
    
    def __eq__(self, object):
        if self.marca == object.marca:
            return True
        else:
            return False
    

garrafa = Garrafa(100, 'preto', 'shopee')
print(garrafa)

stanley = Garrafa(100, 'preto', 'shopee')
print(stanley)

print(garrafa == stanley)