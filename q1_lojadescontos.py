valorcompra = float(input("Digite o valor da compra: "))

if(valorcompra >=101 and valorcompra <=500):
    print(f'Valor final com desconto: R${valorcompra - (valorcompra * 0.05)}\n')
elif(valorcompra > 500):
    print(f'Valor final com desconto: R${valorcompra - (valorcompra * 0.10)}\n')
else:
    print(f'Sem desconto! Valor final: R${valorcompra}\n')