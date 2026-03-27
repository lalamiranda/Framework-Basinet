from Bio import SeqIO
import pandas as pd

def contar_bases(arquivo):
    contagem = {'A':0, 'T':0, 'C':0, 'G':0}

    for record in SeqIO.parse(arquivo, "fasta"):
        seq = str(record.seq)
        for base in seq:
            if base in contagem:
                contagem[base] += 1

    return contagem


def criar_dataframe_bases():
    dados = []

    arquivos = {
        "DENV-1": "Framework-Basinet/DENV-1.fasta",
        "DENV-2": "Framework-Basinet/DENV-2.fasta",
        "DENV-3": "Framework-Basinet/DENV-3.fasta",
        "DENV-4": "Framework-Basinet/DENV-4.fasta"
    }

    for denv, arq in arquivos.items():
        cont = contar_bases(arq)
        for base, valor in cont.items():
            dados.append([denv, base, valor])

    df_bases = pd.DataFrame(dados, columns=["DENV", "Base", "Quantidade"])

    return df_bases