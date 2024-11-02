# Dicionário de faturamento por estado
faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

def calc_percentual(faturamento):
    total_fatu = sum(faturamento.values()) 

    percentual = {}

    for estado, valor in faturamento.items():
        percentual[estado] = (valor / total_fatu) * 100  

    return total_fatu, percentual 


total_fatu, percentual = calc_percentual(faturamento_estados)


print(f'Faturamento total: R${total_fatu:.2f}')
print('Percentuais de faturamento por estado:')

for estado, perc in percentual.items():
    print(f'{estado}: {perc:.2f}%')
