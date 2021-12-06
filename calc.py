###Aprendendo Python

##        print("Bem-vindo a calculadora de Python")
##        name = str(input(print("Digite seu nome para continuar {}".format(name))))
##        print("Bem-vindo {}".format(name))


operacao = input ('''
Escolha a operação desejavel
Basta apenas escolher por operação
+ para Soma
- para Subtração
* para Multiplicação
/ para Divisão                                    
                  ''')

num1 = int(input('EScolha seu primeiro número'))
num2 = int(input('Escolha seu segundo número'))
result = int(num1 + num2)


if operacao == '+':
    print(f'{num1} + {num2} = ')
    print(result)

elif operacao == '-':
    print(f'{num1} - {num2} = ')
    print(result)
    
elif operacao == '*':
    print(f'{num1} * {num2} = ')
    print(result)
    
elif operacao == '/':
    print(f'{num1} / {num2} = ')
    print(result)

else:
    ('Você não colocou um operador valido')