#1 Crie um programa que receba o ano de nascimento do usuário e informe se ele é menor de idade (menor de 18 anos), maior de idade ou idoso (60 anos ou mais)

ano = int(2003)

idade = 2026 - ano

if idade >=60:
    print(f"idoso ({idade} anos)")

elif idade<=59 and idade>=18:
    print(f"maior de idade ({idade} anos)")

else:
    print(f"menor de idade ({idade} anos)")


#Variação 2: Categoria de Atleta (Faixas de Idade)

ano = int(2003)

idade = 2026 - ano

if idade >=60:
    print(f"Categoria Master ({idade} anos)")

elif idade<=59 and idade>=18:
    print(f"Categoria Adulto ({idade} anos)")

elif idade<=17 and idade >=12:
    print(f"Categoria Junvenil ({idade} anos)")

else:
    print(f"Cadegoria Infantil ({idade} anos)")

#Variação 3: Calculadora de Desconto e Frete (Simulação de E-commerce)

valor_compra = float(20)
frete = 20.00

if valor_compra >=300.00:
    valor_final = valor_compra * 0.85 #Aplicou 15% dedesconto
    print(
        f"valor a pagar: R${valor_final:.2f} (com 15% de desconto e Frete Gratis)" 
    )

elif valor_compra >=100.00:
    valor_final = valor_compra * 0.95 #Aplicou 5% de desconto
    frete = valor_final + frete
    print(
        f"valor a pagar: R${frete:.2f} (com 5% de desconto  + Frete R${20.00:.2f})"
    )
else:
    print(
        f"Valor a pagar: {valor_compra + frete:.2f} (Acrecimo de R${frete:.2f} do Frete)"
    )

#4 Calculadora de Conta de Luz (Simulação de Concessionária)Neste exercício, você calcula o valor total da conta com base no consumo de energia ($\text{kWh}$) e na aplicação de taxas operacionais.

consumo = float(300.00)

if consumo <= 150.00:
    preco = consumo * 0.60
    taxas =()
    print(
        f"valor da Conta: R$ {preco:.2f} (Sem taxas extras aplicadas)"
    )

elif consumo <= 300.00:
    preco = (consumo * 0.80) + 15.00 #taxa de iluminação.
    print(
        f"Valor da conta: R$ {preco:.2f} (+ Taxa fixa de Iluminação Pública de 15,00$.)"
    )

else:
    preco = (consumo * 1.00) + 55.00 #(25 + 30 das taxas)
    print(
        f"Valor da Conta: R$  {preco:.2f}( + Taxa fixa de Iluminação Pública de 15,00$ + Adicional de Bandeira Vermelha de R$30,00.)"
    )

#5 Análise de Risco de Empréstimo (Mercado Financeiro)Este cenário simula a validação de regra de negócio para concessão de crédito.
    
salario = float(1800)
parcela = float(200)
percentual = (parcela / salario) * 100

if percentual <= 20:
    print(
        f"Crédito Aprovado! Comprometimento de {percentual:.1f}% (Risco Baixo)."
    )

elif percentual <=35:
    print(
        f"Credito Aprovado com Analise Manual Comprometimento de {percentual:.1f}% (Risco Médio)."
    )

else:
    print(
        f"Credito Negado! Comprometimento de {percentual:.1f}% (Risco Alto)."
    )

#6 O Desafio: Somatório e Média de Números 
# Você deve criar um programa que peça para o usuário digitar vários números inteiros, um de cada vez.

soma = 0
contador = 0

while True:
    numero = int(input("Digite um número (ou 0 para sair):"))
    if numero == 0:
        break
    soma += numero
    contador += 1

          
if contador > 0:
    media = soma / contador
    print(f"/n--- RESUMO FINAL ---")
    print(f"Quantidade de números: {contador} ")
    print(f"Soma total: {soma}")
    print(f"Média: {media:.2f}")
else:
    print("\nNenhum número foi digitado.")

    