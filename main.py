import requests


CHAVE_API = 'sua_chave_api_aqui'

def obter_previsao_tempo(uf):
    url = f'https://api.hgbrasil.com/weather?woeid={uf}&key={CHAVE_API}'
    response = requests.get(url)

    if response.status_code != 200:
        return None
    else:
        dados = response.json()
        return dados


def exibir_previsao_tempo(dados):
    if dados:
        temperatura_celsius = dados['temp']
        data_hora_consulta = dados['time']
        descricao_tempo = dados['description']
        dia_noite = dados['condition_slug']
        umidade = dados['humidity']
        velocidade_vento = dados['wind_speedy']
        nascer_do_sol = dados['sunrise']
        por_do_sol = dados['sunset']
        condicao_atual = dados['condition']

        print(f"Previsão do tempo para {uf}:")
        print(f"Temperatura: {temperatura_celsius}°C")
        print(f"Data e Hora da Consulta: {data_hora_consulta}")
        print(f"Descrição do Tempo: {descricao_tempo}")
        print(f"Condição Atual: {condicao_atual}")
        print(f"É {dia_noite}")
        print(f"Umidade: {umidade}%")
        print(f"Velocidade do Vento: {velocidade_vento}")
        print(f"Nascer do Sol: {nascer_do_sol}")
        print(f"Pôr do Sol: {por_do_sol}")
    else:
        print("Não foi possível obter a previsão do tempo para a UF informada. Certifique-se de que sua chave de API está configurada corretamente.")

if __name__ == "__main":
    uf = input("Digite a UF (sigla do estado brasileiro): ").upper()
    dados_previsao_tempo = obter_previsao_tempo(uf)
    exibir_previsao_tempo(dados_previsao_tempo)