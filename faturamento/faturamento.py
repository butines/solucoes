import json
import os

print("d:\emprego\faturamento", os.getcwd())

def ler_fatu(dias):
    with open(dias, 'r') as f:
        info = json.load(f)
        return info
      

def calc_faturamento(info):
    faturamentos = [dia["faturamento"] for dia in info if dia["faturamento"] > 0]

    if not faturamentos:
        return "Não houve nenhum dia com faturamento neste mês."
    
    menor_fatu = min(faturamentos)
    maior_fatu = max(faturamentos)

    media = sum(faturamentos) / len(faturamentos)

    dias_acima = sum(1 for valor in faturamentos if valor > media)

    return menor_fatu, maior_fatu, dias_acima


info = ler_fatu(r'd:\emprego\faturamento\dias.json')


resultado = calc_faturamento(info)

if isinstance(resultado, str):

    print(resultado)
else:
    menor_fatu, maior_fatu, dias_acima = resultado

    print(f"Menor faturamento no mês: R$ {menor_fatu:.2f}")
    print(f"Maior faturamento no mês: R$ {maior_fatu:.2f}")
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima}")