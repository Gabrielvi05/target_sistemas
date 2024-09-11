import json

cam = 'C:\\Users\\Desktop\\OneDrive\\Área de Trabalho\\resolucoes_exer\\exerc3\\dados.json'

with open(cam, 'r') as file:
    dados = json.load(file)

def anali_fat(dados):
    # Presumindo que 'dados' seja uma lista de dicionários e cada dicionário tem uma chave 'faturamento'
    fat = [d['valor'] for d in dados if 'valor' in d]

    if not fat:
        raise ValueError("A lista de faturamentos está vazia.")

    menor_valor = min(fat)
    maior_valor = max(fat)
    media = sum(fat) / len(fat)
    dias_acima_da_media = sum(1 for valor in fat if valor > media)

    return menor_valor, maior_valor, dias_acima_da_media

# A função json.load já carrega os dados como um objeto Python (lista ou dicionário).
menor_valor, maior_valor, dias_acima_da_media = anali_fat(dados)

print("Menor valor de faturamento:", menor_valor)
print("Maior valor de faturamento:", maior_valor)
print("Número de dias com faturamento acima da média:", dias_acima_da_media)
