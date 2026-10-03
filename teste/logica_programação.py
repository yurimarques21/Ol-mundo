#exiba os números de 1 a 10 usando um loop while

n = 1

while n <= 10:
    print(n)
    n += 1
# crie um simulador de tabuada, onde o jogador digita um número, e a tabuada desse número será exibida.

contador = int(input("Digite o numero que deseja multiplicar: "))

for i in range(int(input("Digite até onde quer multplicar: "))):
    resultado = contador * i
    print(f"{contador} x {i} ={resultado}")