from Bio import SeqIO
import pandas as pd

def extrair_tamanhos(arquivo):
    tamanhos = []

    for record in SeqIO.parse(arquivo, "fasta"):
        tamanho = len(record.seq)
        tamanhos.append(tamanho)

    return tamanhos


def criar_dataframe():
    # lendo os arquivos
    tamanhos_denv1 = extrair_tamanhos("Framework-Basinet/DENV-1.fasta")
    tamanhos_denv2 = extrair_tamanhos("Framework-Basinet/DENV-2.fasta")
    tamanhos_denv3 = extrair_tamanhos("Framework-Basinet/DENV-3.fasta")
    tamanhos_denv4 = extrair_tamanhos("Framework-Basinet/DENV-4.fasta")

    print("DENV-1:", tamanhos_denv1[:5])
    print("DENV-2:", tamanhos_denv2[:5])
    print("DENV-3:", tamanhos_denv3[:5])
    print("DENV-4:", tamanhos_denv4[:5])

    dados = {
        'DENV': (
            ['DENV-1'] * len(tamanhos_denv1) +
            ['DENV-2'] * len(tamanhos_denv2) +
            ['DENV-3'] * len(tamanhos_denv3) +
            ['DENV-4'] * len(tamanhos_denv4)
        ),
        'Tamanho': (
            tamanhos_denv1 +
            tamanhos_denv2 +
            tamanhos_denv3 +
            tamanhos_denv4
        )
    }

    df = pd.DataFrame(dados)

    print(df.head())

    return df