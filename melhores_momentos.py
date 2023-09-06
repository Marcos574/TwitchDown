import pandas as pd
from textblob import TextBlob
from collections import Counter
from datetime import datetime, timedelta

# Etapa 1: Leitura do arquivo de histórico de chat
def ler_historico_chat(arquivo):
    with open(arquivo, 'r', encoding='utf-8') as file:
        linhas = file.readlines()
    return linhas

# Etapa 2: Pré-processamento de dados
def preprocessar_dados(linhas):
    mensagens = []
    for linha in linhas:
        partes = linha.split('] ')
        if len(partes) >= 2:
            tempo, mensagem = partes[0][1:], partes[1].strip()
            mensagens.append({'tempo': tempo, 'mensagem': mensagem})
    df = pd.DataFrame(mensagens)
    return df

# Etapa 3: Análise de sentimento
def analisar_sentimento(texto):
    analysis = TextBlob(texto)
    return analysis.sentiment.polarity

# Etapa 4: Detecção de mensagens semelhantes
def detectar_mensagens_semelhantes(df):
    df['sentimento'] = df['mensagem'].apply(analisar_sentimento)
    
    # Detectar mensagens semelhantes com base na contagem de mensagens idênticas
    contador_mensagens = Counter(df['mensagem'])
    momentos_semelhantes = []
    limite_contagem = 5  # Ajuste o limite conforme necessário
    
    for mensagem, contagem in contador_mensagens.items():
        if contagem >= limite_contagem:
            indices = df[df['mensagem'] == mensagem].index
            tempo_inicial = df.at[indices[0], 'tempo']
            tempo_final = df.at[indices[-1], 'tempo']
            momentos_semelhantes.append({'tempo_inicial': tempo_inicial, 'tempo_final': tempo_final})
    
    return momentos_semelhantes

# Etapa 5: Filtrar momentos com mais de 2 minutos
def filtrar_momentos_longo(momentos, limite_minutos=2):
    momentos_filtrados = []
    for momento in momentos:
        tempo_inicial = datetime.strptime(momento['tempo_inicial'], '%H:%M:%S')
        tempo_final = datetime.strptime(momento['tempo_final'], '%H:%M:%S')
        duracao = tempo_final - tempo_inicial
        if duracao <= timedelta(minutes=limite_minutos):
            momentos_filtrados.append(momento)
    return momentos_filtrados


# Etapa 6: Exibir os momentos semelhantes
def exibir_momentos_semelhantes(momentos_semelhantes):
    clip = 0
    for momento in momentos_semelhantes:
        tempo_inicial = datetime.strptime(momento['tempo_inicial'], '%H:%M:%S')
        tempo_inicial -= timedelta(seconds=30)  # Subtrair 20 segundos do tempo inicial
        tempo_inicial_str = tempo_inicial.strftime('%H:%M:%S')

        tempo_final = datetime.strptime(momento['tempo_final'], '%H:%M:%S')
        tempo_final += timedelta(seconds=15)
        tempo_final_str = tempo_final.strftime('%H:%M:%S')
        #print(f"inicio: {tempo_inicial_str} - Tempo Final: {tempo_final}")

        #{"inicio": "00:38:08", "fim": "00:39:20", "output": "Clip1.mp4"},
        clip += 1
        print(f'{{"inicio": "{tempo_inicial_str}", "fim": "{tempo_final_str}", "output": "Clip{clip}.mp4"}}')

if __name__ == '__main__':
    arquivo_chat = 'seu_arquivo_de_chat.txt'  # Substitua pelo nome do seu arquivo de chat
    linhas_chat = ler_historico_chat(arquivo_chat)
    df_chat = preprocessar_dados(linhas_chat)
    momentos_semelhantes = detectar_mensagens_semelhantes(df_chat)
    momentos_filtrados = filtrar_momentos_longo(momentos_semelhantes, limite_minutos=2)
    exibir_momentos_semelhantes(momentos_filtrados)




