import pandas as pd
from time import sleep

vendas_df = pd.read_excel('C:\\Users\\carro_akq51l3\\Downloads\\Cópia de Vendas.xlsx')

"""
def faturamento_total(nome):
    todos = vendas_df.groupby('ID Loja')['Valor Final'].sum()
    faturamento = todos[nome]
    return faturamento


def ranking():
    todos = vendas_df.groupby('ID Loja')['Valor Final'].sum()
    todos = todos.to_dict()
    rank = {'pri' : {}, 'seg': {}, 'ter': {}}
    for shop, faturamento in todos.items():
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
            rank['ter'] = [shop, faturamento]
        
    return rank"""

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



print(produtos_mais_vendidos_por_shop())

"""vendas_df = pd.read_excel('C:\\Users\\carro_akq51l3\\Downloads\\Cópia de Vendas.xlsx')
"""
"""print()
print('Em TERCEIRO LUGAR ficou...')
sleep(2)
print('Shopping Palladium')
sleep(2)
print('Em SEGUNDO LUGAR')
sleep(2)
print('ficou...')
sleep(2)
print('Shopping FDP')
sleep(1)
print('E finalmente.')
sleep(2)
print('Em PRIMEIRO LUGAR ESTÁ...')
sleep(2)
print('.')
sleep(1)
print('.')
sleep(1)
print('.')
sleep(2)
print('Shopping Ibirapuera!!!')"""

"""
        print(f'3° {top3["ter"][0]} -> R${top3["ter"][1]}')
        sleep(2)
        print(f'2° {top3["seg"][0]} -> R${top3["seg"][1]}')
        sleep(2)
        print(f'1° {top3["pri"][0]} -> R${top3["pri"][1]}')
        sleep(2)
"""
