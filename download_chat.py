import subprocess
import os

# Caminho absoluto para a localização da aplicação TwitchDownloaderCLI
app_directory = r'C:\Users\mamar\Documents\GitHub\TwitchDown\TwitchDownloaderCLI\bin\Release\net6.0\publish\Windows'

# Função para baixar o chat completo em formato TXT
def baixar_chat_completo(id_da_live, pasta_destino, nome_arquivo):
    # Construa o caminho completo para o arquivo de saída
    caminho_saida = os.path.join(pasta_destino, nome_arquivo + ".txt")
    
    comando = [
        os.path.join(app_directory, "TwitchDownloaderCLI.exe"),
        "chatdownload",
        "--id", id_da_live,
        "-o", caminho_saida
    ]
    subprocess.run(comando)

# ID da live do Twitch que você deseja baixar o chat
id_da_live = "1914545362"

# Pasta de destino para salvar o arquivo TXT do chat
pasta_destino = r'C:\Users\mamar\Documents\Tealz\01.09.2023'

# Nome do arquivo de saída (sem extensão)
nome_arquivo = "chat_da_live"

# Certifique-se de que a pasta de destino exista; crie-a se não existir
if not os.path.exists(pasta_destino):
    os.makedirs(pasta_destino)

# Baixa o chat completo em formato TXT
baixar_chat_completo(id_da_live, pasta_destino, nome_arquivo)

print("\nDownload do chat em formato TXT concluído.")
