# Elabore um algoritmo que receba dois números, calcule a multiplicação entre eles e apresente o resultado.

numero1 = int(input("Digite o primeiro numero"))
numero2 = int(input("Digite o segundo numero"))

print("O valor da multiplicação é", numero1 * numero2)

# Desenvolva um algoritmo que receba cinco números, calcule a média aritmética e apresente o resultado final.


num1 = float(input("Digite a primeira nota"))
num2 = float(input("Digite a segunda nota"))
num3 = float(input("Digitie a terceira nota"))
num4 = float(input("Digitia a quarta nota"))
num5 = float(input("Digite a quinta nota"))

media = (num1 + num2 + num3 + num4 + num5) /5

print("O valor da media aritmetica é", media)

# Construa um algoritmo que receba o valor de um produto e calcule o preço final considerando um acréscimo de 8% de imposto.

produto = float(input("Valor do produto"))
imposto = (produto * 0.08) + produto
print("O valor do produto com acrescimo de imposto é", imposto)

# Elabore um algoritmo que receba dois números e apresente o resultado da subtração entre eles.

num01 = int(input("Digite o primeiro numero"))
num02 = int(input("Digite o segundo numero"))

print("O valor da subtraçao é", num01 - num02)

# Construa um algoritmo que receba a altura e o peso de uma pessoa e calcule o Índice de Massa corporal (imc)

altura = float(input("Digite o valor da altura"))
peso = float(input("Digite o valor do peso"))
imc = altura / (peso * peso) 

print("O valor do indice de massa corporal é", imc)

#Elabore um algoritmo que receba a temperatura em graus Celsius e apresente o valor convertido para garus em fahrenheit

temperatura = float(input("Digite a temperatura"))
fahrenheit = (temperatura * 9/5) + 32
print("A temperatura convertida em fahrenheit é", fahrenheit)

#Construa um algoritmo que receba a quantidade de horas trabalhadas por um funcionário e o valor da hora trabalhada, calculando o salário total

horas_trabalho = float(input("Digite a quantidade de horas trabalhada"))
valor_trabalho = float(input("Digite o valor da hora trabalhada"))
print("O seu salario total baseado nas horas trabalhadas é", (horas_trabalho * valor_trabalho))