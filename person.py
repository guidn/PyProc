##Aprendendo POO com Python

class Person:
    def __init__(self, name, age, altura):
        self.name = name
        self.idade = age
        self.altura = altura
    
    def say_hi (self):
        print(f"Olá, meu nome é {self.name}. Tenho {self.idade}"
              f" anos e minha altura é {self.altura}m")
        
    def cozinhar(self, receita):
        print(f"Estou cozinhando um: {receita}")
    
    def andar(self, distancia):
        print(f"Sai para andar. Volto quando andar uns {distancia} metros")


pessoa = Person(name='Joao', age=25, altura=180)

pessoa.say_hi()
pessoa.cozinhar('Macarrão')
pessoa.andar(500)