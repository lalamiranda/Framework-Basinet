from Bio import SeqIO
from collections import Counter
import pandas as pd

def contar_codons(arquivo):
    contagem = Counter()

    for record in SeqIO.parse(arquivo, "fasta"):
        seq = str(record.seq)

        limite = (len(seq) // 3) * 3
        codons = [seq[i:i+3] for i in range(0, limite, 3)]

        contagem.update(codons)

    return contagem


def criar_dataframe_codons():
    arquivos = {
        "DENV-1": "Framework-Basinet/DENV-1.fasta",
        "DENV-2": "Framework-Basinet/DENV-2.fasta",
        "DENV-3": "Framework-Basinet/DENV-3.fasta",
        "DENV-4": "Framework-Basinet/DENV-4.fasta"
    }

    dados = []

    for denv, arq in arquivos.items():
        cont = contar_codons(arq)

        for codon, freq in cont.items():
            dados.append([denv, codon, freq])

    df_codons = pd.DataFrame(dados, columns=["DENV", "Codon", "Frequencia"])

    # pega top 10 mais frequentes no geral
    top_codons = (
        df_codons.groupby("Codon")["Frequencia"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .index
    )

    df_top = df_codons[df_codons["Codon"].isin(top_codons)]

    return df_top