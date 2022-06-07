
#enviar um email com os detalhes da compra online (utilizando 3 tentativas) para compras confirmadas.

compra_confirmada = True
dados_compra = 'Compra no valor de 50,00 aprovada.'

for enviar in range (3) :
 if compra_confirmada:
     print(dados_compra)
     print('Detalhes enviado para seu email.')
     break
else:
    print('Compra nao aprovada')

