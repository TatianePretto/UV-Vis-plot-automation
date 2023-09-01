
import os

pasta = r'xxxxxxx'  ### substitute by the folder you want


# Percorra todos os arquivos na pasta
for nome_arquivo in os.listdir(pasta):
    # Verifique se o arquivo é um arquivo de texto
    if nome_arquivo.endswith('.txt'):
        # Abra o arquivo
        caminho_arquivo = os.path.join(pasta, nome_arquivo)
        with open(caminho_arquivo, 'r') as f:
            linhas = f.readlines()

        # Remova as duas primeiras linhas
        linhas = linhas[2:]

        # Escreva o conteúdo de volta ao arquivo
        with open(caminho_arquivo, 'w') as f:
            f.writelines(linhas)
