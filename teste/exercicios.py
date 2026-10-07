#Crie um programa que receba o ano de nascimento do usuário e informe se ele é menor de idade (menor de 18 anos), maior de idade ou idoso (60 anos ou mais)

ano = int(2003)

idade = 2026 - ano

if idade >=60:
    print(f"idoso ({idade} anos)")

elif idade<=59 and idade>=18:
    print(f"maior de idade ({idade} anos)")

else:
    print(f"menor de idade ({idade} anos)")


#Variação 1: Categoria de Atleta (Faixas de Idade)

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

#Variação 2: Calculadora de Desconto e Frete (Simulação de E-commerce)

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