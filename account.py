#Uns importo loko ai



print("Aqui está sua conta bancaria")

__name__ = input(print("Digite seu nome para continuar"))

if __name__ == None:
    print("Você não digitou seu nome, abra o programa novamente.")
    
else:
    print("Olá {} .\nVamos prosseguir com o atendimento".format(__name__['Olá']))


def Abrir(abrir):
    print("Olá, bem vindo ao seu aplicativo do banco")
    
    j = input(print("Voce já tem uma conta?? Digite 1 para entrar na sua conta e 2 para Criar uma nova conta."))
    
    if j == 1:
        print("Entrando na sua conta")
    else:
        print("Criando sua nova Conta")
        
Abrir()

