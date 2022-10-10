# Calcula o desconto e o acréscimo no valor de um produto
p = float(input('Digite o preço do produto: R$'))
pd = p - (p * 5 / 100)
pa = p + (p * 10 / 100)
print('Para pagamento à vista, o valor do produto com o desconto de 5% é de R${:.2f}'.format(pd))
print('Para pagamento parcelado, o valor do produto com acréscimo de 10% é de R${:.2f}'.format(pa))
