import pandas as pd

def formatar_brasil(numero):
    numero_americano = f'{numero:,}'
    numero_brasileiro = numero_americano.replace(',', '.')
    return numero_brasileiro


def linha(tam):
    print('-' * tam)


vendas_df = pd.read_excel('C:\\Users\\carro_akq51l3\\Downloads\\Cópia de Vendas.xlsx')
transacoes_loja = vendas_df['ID Loja'].value_counts()

total_iguatemi = None
vendas_iguatemi = 0
faturamento_diario_medio = 0
dias = 0
dia = None
lojas = {
    'Iguatemi Esplanada': 0
}

for c in range(0, len(vendas_df)):
    if vendas_df['ID Loja'][c] == 'Iguatemi Esplanada':
        vendas_iguatemi += 1
        faturamento_diario_medio += vendas_df['Valor Final'][c]
        if vendas_df['Data'][c] != dia:
            dias += 1
        dia = vendas_df['Data'][c]
    try:
        lojas[vendas_df['ID Loja'][c]] += vendas_df['Valor Final'][c]
    except:
        lojas[vendas_df['ID Loja'][c]] = 0
        lojas[vendas_df['ID Loja'][c]] += vendas_df['Valor Final'][c]

print(f'O shooping Iguatemi Esplanada realizou um total de {vendas_iguatemi} vendas.')
faturamento_diario_medio = faturamento_diario_medio / dias
print(f'Média de faturamento diário: R${faturamento_diario_medio:.2f}')

pri_id, seg_id, ter_id = None, None, None
pri_fatu, seg_fatu, ter_fatu = 0, 0, 0

for id, faturamento in lojas.items():
    if faturamento > pri_fatu:
        pri_fatu = faturamento
        pri_id = id
    if faturamento < pri_fatu and faturamento > seg_fatu:
        seg_fatu = faturamento
        seg_id = id
    if faturamento < seg_fatu and faturamento > ter_fatu:
        ter_fatu = faturamento
        ter_id = id

linha(42)
print(f'RANKING DE FATURAMENTO')
linha(42)
print(f'1°{pri_id} -> R${formatar_brasil(pri_fatu)}')
print(f'2°{seg_id} -> R${formatar_brasil(seg_fatu)}')
print(f'3°{ter_id} -> R${formatar_brasil(ter_fatu)}')
