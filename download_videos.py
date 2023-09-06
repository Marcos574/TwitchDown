import subprocess
import os

# Caminho absoluto para a localização da aplicação TwitchDownloaderCLI
app_directory = r'C:\Users\mamar\Documents\GitHub\TwitchDown\TwitchDownloaderCLI\bin\Release\net6.0\publish\Windows'

# Função para converter um tempo no formato Hora:Minuto:Segundo para segundos totais
def tempo_para_segundos(tempo_str):
    partes = tempo_str.split(":")
    if len(partes) == 3:
        horas, minutos, segundos = map(int, partes)
        return horas * 3600 + minutos * 60 + segundos
    elif len(partes) == 2:
        minutos, segundos = map(int, partes)
        return minutos * 60 + segundos
    else:
        return None

# Função para baixar um trecho do vídeo com base no tempo de início e fim
def baixar_trecho_video(id_da_live, tempo_inicio, tempo_fim, pasta_destino, nome_arquivo):
    # Construa o caminho completo para o arquivo de saída
    caminho_saida = os.path.join(pasta_destino, nome_arquivo)
    
    comando = [
        os.path.join(app_directory, "TwitchDownloaderCLI.exe"),
        "videodownload",
        "--id", id_da_live,
        "-o", caminho_saida,
        "-b", str(tempo_inicio),
        "-e", str(tempo_fim)
    ]
    subprocess.run(comando)

# ID da live do Twitch que você deseja baixar
id_da_live = "1914545362"

# Lista de trechos a serem baixados (tempo de início e fim em formato Hora:Minuto:Segundo)
trechos = [
    {"inicio": "03:04:29", "fim": "03:05:16", "output": "Clip21.mp4"},
    {"inicio": "03:08:07", "fim": "03:09:02", "output": "Clip22.mp4"},
    {"inicio": "03:20:00", "fim": "03:20:55", "output": "Clip23.mp4"},
    {"inicio": "03:48:16", "fim": "03:50:04", "output": "Clip24.mp4"},
    {"inicio": "04:01:15", "fim": "04:02:15", "output": "Clip25.mp4"},
    {"inicio": "04:29:14", "fim": "04:30:28", "output": "Clip26.mp4"},
    {"inicio": "04:38:24", "fim": "04:39:11", "output": "Clip27.mp4"},
    {"inicio": "04:39:18", "fim": "04:40:49", "output": "Clip28.mp4"},
    {"inicio": "04:39:48", "fim": "04:40:36", "output": "Clip29.mp4"},
    {"inicio": "04:39:53", "fim": "04:41:41", "output": "Clip30.mp4"},
    {"inicio": "04:42:13", "fim": "04:44:02", "output": "Clip31.mp4"},
    {"inicio": "04:58:28", "fim": "04:59:42", "output": "Clip32.mp4"},
    {"inicio": "05:07:30", "fim": "05:09:03", "output": "Clip33.mp4"},
    {"inicio": "05:29:24", "fim": "05:30:34", "output": "Clip34.mp4"},
    {"inicio": "05:30:10", "fim": "05:32:06", "output": "Clip35.mp4"},
    {"inicio": "07:01:30", "fim": "07:02:17", "output": "Clip36.mp4"},
    {"inicio": "09:59:53", "fim": "10:00:48", "output": "Clip37.mp4"},
    {"inicio": "10:09:20", "fim": "10:10:21", "output": "Clip38.mp4"},
    # Adicione mais trechos conforme necessário
]

# Pasta de destino para salvar os vídeos baixados
pasta_destino = r'C:\Users\mamar\Documents\Tealz\01.09.2023'

# Certifique-se de que a pasta de destino exista; crie-a se não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Itera sobre a lista de trechos e baixa cada um
for trecho in trechos:
    inicio_segundos = tempo_para_segundos(trecho["inicio"])
    fim_segundos = tempo_para_segundos(trecho["fim"])
    nome_arquivo = trecho["output"]
    
    # Baixa o trecho do vídeo e especifica a pasta de destino
    baixar_trecho_video(id_da_live, inicio_segundos, fim_segundos, pasta_destino, nome_arquivo)

print("Download dos trechos concluído.")



