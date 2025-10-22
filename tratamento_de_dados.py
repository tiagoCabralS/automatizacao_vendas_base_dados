import pandas as pd
from time import sleep


def formatar_brasil(numero):
    numero_americano = f'{numero:,}'
    numero_brasileiro = numero_americano.replace(',', '.')
    return numero_brasileiro


def linha(tam=42):
    print('-' * tam)


def cabecalho(texto=str):
    texto = str.upper(texto)
    linha(42)
    print(f'{texto:^42}')
    linha(42)


def contagem_vendas(nome):
    todas = vendas_df['ID Loja'].value_counts()
    contagem = todas[nome]
    return contagem


def faturamento_total(nome):
    faturamento = vendas_df.groupby('ID Loja')['Valor Final'].sum()
    faturamento = faturamento[nome]
    return faturamento


def media_diaria(nome):
    lojas_datas = vendas_df.groupby('ID Loja')['Data'].unique()
    quant_datas = len(lojas_datas[nome])
    media = faturamento_total(nome) / quant_datas
    return media


def ranking():
    todos = vendas_df.groupby('ID Loja')['Valor Final'].sum()
    top3 = todos.sort_values(ascending=False).head(3)
    rank = {'pri' : {}, 'seg': {}, 'ter': {}}
    rank['pri'] = [top3.index[0], top3.iloc[0]]
    rank['seg'] = [top3.index[1], top3.iloc[1]] 
    rank['ter'] = [top3.index[2], top3.iloc[2]]
    """for shop, faturamento in todos.items():
        if rank['pri'] == {}:
            rank['pri'] = [shop, faturamento]
        elif rank['pri'][1] < faturamento:
            rank['pri'] = [shop, faturamento]
        if rank['seg'] == {}:
            rank['seg'] = [shop, faturamento]
        elif rank['seg'][1] < faturamento and rank['pri'][1] > faturamento:
            rank['seg'] = [shop, faturamento]
        if rank['ter'] == {}:
            rank['ter'] = [shop, faturamento]
        elif rank['ter'][1] < faturamento and rank['seg'][1] > faturamento:
            rank['ter'] = [shop, faturamento]"""
    return rank


def leiaInt(msg):
    ok = False
    num = input(msg)
    while not ok:
        try:
            result = int(num)
        except:
            num = input(msg)
        else:
            return result


def checarSeExiste(texto, base):
    ok = False
    while not ok:
        leitura = input(texto)
        for shop in base:
            if leitura == shop:
                ok = True
    return leitura    


def produtos_mais_vendidos_por_shop():
    todos = vendas_df.groupby(['ID Loja', 'Produto'])['Quantidade'].sum().reset_index() 
    # Reset index para transformar o groupby em DataFrame
    mais_vendidos = todos.loc[todos.groupby('ID Loja')['Quantidade'].idxmax()]
    
    return mais_vendidos 


def parar(opc):
    if opc == 0:
        return True
    else:
        return False


vendas_df = pd.read_excel('C:\\Users\\carro_akq51l3\\Downloads\\Cópia de Vendas.xlsx')

while True:
    print()
    cabecalho('Sistema de análise')
    sleep(1)
    for loja in vendas_df.groupby('ID Loja'):
        print(loja[0])
        sleep(0.3)
    sleep(1)
    linha()
    print('0: Fechar sistema')
    sleep(1)
    print('1: Número de vendas de um shopping')
    sleep(1)
    print('2: Média diária de um shopping')
    sleep(1)
    print('3: Ranking TOP 3 maiores faturamentos')
    sleep(1)
    print('4: Buscar produtos mais vendidos por shopping')
    sleep(1)
    opc = leiaInt('Qual ação deseja realizar? ')
    if opc == 0:
        print('Fechando sistema...')
        sleep(2)
        break
    elif opc == 1:
        nomes = vendas_df['ID Loja']
        nome = checarSeExiste('Qual shopping? ', nomes)
        print(f'O shopping {nome} realizou {contagem_vendas(nome)} vendas.')
        sleep(1)
        linha()
        print('0: Fechar o sistema')
        print('1: Voltar para o menu principal')
        opc = leiaInt('Qual ação deseja realizar? ')
        if parar(opc):
            print('Fechando sistema...')
            sleep(1)
            break
    elif opc == 2:
        nomes = vendas_df['ID Loja']
        nome = checarSeExiste('Qual shopping? ', nomes)
        print(f'O shopping {nome} tem uma média de R${media_diaria(nome):.2f} de faturamento diário.')
        sleep(1)
        linha()
        print('0: Fechar o sistema')
        print('1: Voltar para o menu principal')
        opc = leiaInt('Qual ação deseja realizar? ')
        if parar(opc):
            print('Fechando sistema...')
            sleep(1)
            break
    elif opc == 3:
        top3 = ranking()
        cabecalho('Ranking de Faturamento')
        print()
        sleep(1)
        print('Em TERCEIRO LUGAR ficou...')
        sleep(2)
        print(f'{top3["ter"][0]} com R${formatar_brasil(top3["ter"][1])}')
        sleep(2)
        print('Em SEGUNDO LUGAR')
        sleep(2)
        print('ficou...')
        sleep(2)
        print(f'{top3["seg"][0]} com R${formatar_brasil(top3["seg"][1])}')
        sleep(1)
        print('E finalmente.')
        sleep(2)
        print('Em PRIMEIRO LUGAR ESTÁ...')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(1)
        print('.')
        sleep(2)
        print(f'{top3["pri"][0]} com R${formatar_brasil(top3["pri"][1])}!!!')
        sleep(1)
        linha()
        print('0: Fechar o sistema')
        print('1: Voltar para o menu principal')
        opc = leiaInt('Qual ação deseja realizar? ')
        if parar(opc):
            print('Fechando sistema...')
            sleep(1)
            break
    elif opc == 4:
        shop = checarSeExiste('Qual shopping? ', vendas_df['ID Loja'])
        result = produtos_mais_vendidos_por_shop().loc[produtos_mais_vendidos_por_shop()['ID Loja'] == shop]
        print(f'O produto mais vendido no shopping {shop} foi {result["Produto"].values[0]} com {result["Quantidade"].values[0]} unidades vendidas.')
        sleep(1)
        linha()
        print('0: Fechar o sistema')
        print('1: Voltar para o menu principal')
        opc = leiaInt('Qual ação deseja realizar? ')
        if parar(opc):
            print('Fechando sistema...')
            sleep(1)
            break
