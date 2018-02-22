from AlgoritmoGenetico import AlgoritmoGenetico

tam_barra, pedidos = map(int, input().split())

demanda = []

i = 0
while i < pedidos:

    tam_pedido, qtd = map(int, input().split())

    demanda.append({'item': i, 'tamanho': tam_pedido, 'quantidade': qtd})

    i+=1


algoritmoGenetico = AlgoritmoGenetico(20, tam_barra, demanda)
algoritmoGenetico.execute()
