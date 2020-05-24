
#Software para calculo do custo de produção de laje pré moldada 13/07/2018

print('='* 100)
print()
print('           Software para calculo do custo de produção de laje pré moldada.')
print('                       XIMENES MATERIAIS PARA CONSTRUÇÃO')
print()
cimento = float(input('Informe o valor de cada saco de cimento estrutural CPV 40kg R$ '))
treliça = float(input('Informe o valor de cada treliça com 12m R$ '))
areia = float(input('Informe o valor do metro cubico de Areia R$ '))
pedra = float(input('Informe o valor do metro cubico de Pedra R$ '))
isopor = float(input('Informe o valor de cada placa de Isopor R$ '))
venda = float(input('Informe o valor de venda da laje pré R$ '))
cimento = (cimento / 40) * 52
treliça = ((treliça / 12) * 2.75) * 25
areia = (areia / 36) * 8
pedra = (pedra / 36) * 7
isopor = (isopor * 2.5) * 25
valor_bruto = (cimento + treliça + areia + pedra + isopor) / 25
print('='* 100)
print('De acordo com os valores informados, cada metro quadrado tem o custo de R${:.2f} para sua fabricação.'.format(valor_bruto))
print('Vendendo cada metro quadrado a R${:.2f}'.format(venda))
print('Você terá um lucro de R${:.2f}'.format(venda - valor_bruto))