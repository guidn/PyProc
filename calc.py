###Aprendendo Python

##        print("Bem-vindo a calculadora de Python")
##        name = str(input(print("Digite seu nome para continuar {}".format(name))))
##        print("Bem-vindo {}".format(name))




class Calc():
    def __init__ (self, Soma: int, Sub: int, name: str):
        self.Soma = Soma
        self.Sub = Sub
        self.name = name
        
    
    def inicio (self):
        i = str(input(print(f"Olá, Sou uma calculadora em Python"
                            f"Me diga seu nome {self.name}")))
    

    def Soma (self):
        print(f"Então vamos a fazer a Soma Sr. {self.name}")
    
    def Sub (self):
        print(f"Então vamos começar a fazer Subtração Sr. {self.name}")
        
print("Tudo certo")

calculadora = Calc (Soma=(1)(4), Sub=(2)(6), name='rodrigo')





