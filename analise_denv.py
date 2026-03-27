import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import os
from Bio import SeqIO

# 1. CONFIGURAÇÃO DE CAMINHOS
# Se o comando !ls mostrou que os arquivos estão em uma pasta específica, mude aqui:
caminho_base = "Framework-Basinet/"

# Mapeamento dos arquivos conforme os nomes no repositório
arquivos = {
    "DENV-1": "DENV-1.fasta",
    "DENV-2": "DENV-2.fasta",
    "DENV-3": "DENV-3.fasta",
    "DENV-4": "DENV-4.fasta"
}

def processar_denv(nome_sorotipo, nome_arquivo):
    caminho_completo = os.path.join(caminho_base, nome_arquivo)

    # Leitura do arquivo
    record = SeqIO.read(caminho_completo, "fasta")
    seq = str(record.seq)

    # Segmentação em Códons (WS=3, ST=3)
    limite = (len(seq) // 3) * 3
    codons = [seq[i:i+3] for i in range(0, limite, 3)]

    # Construção da Rede Direcionada
    G = nx.DiGraph()
    for i in range(len(codons) - 1):
        c1, c2 = codons[i], codons[i+1]
        if G.has_edge(c1, c2):
            G[c1][c2]['weight'] += 1
        else:
            G.add_edge(c1, c2, weight=1)

    return G, codons

# 2. PROCESSAMENTO
resultados = {}
for soro, arq in arquivos.items():
    try:
        print(f"Processando {soro}...")
        g, c = processar_denv(soro, arq)
        resultados[soro] = {"grafo": g, "codons": c}
    except Exception as e:
        print(f"Erro ao processar {soro}: {e}")

# 3. EXTRAÇÃO DAS MÉTRICAS (Hubs de Convergência e Divergência)
print("\n--- RESULTADOS TOPOLÓGICOS ---")
for soro, dados in resultados.items():
    G = dados["grafo"]
    in_deg = sorted(G.in_degree(), key=lambda x: x[1], reverse=True)[:3]
    out_deg = sorted(G.out_degree(), key=lambda x: x[1], reverse=True)[:3]

    print(f"\n{soro}:")
    print(f"  Hubs de Convergência (In): {in_deg}")
    print(f"  Hubs de Divergência (Out): {out_deg}")

# 4. VISUALIZAÇÃO (Exemplo DENV-1)
if "DENV-1" in resultados:
    plt.figure(figsize=(10,7))
    G_plot = resultados["DENV-1"]["grafo"]
    # Pegar os 30 nós mais frequentes para o gráfico não travar
    nodes = pd.Series(resultados["DENV-1"]["codons"]).value_counts().head(30).index
    sub = G_plot.subgraph(nodes)

    pos = nx.spring_layout(sub, k=0.5)
    nx.draw(sub, pos, with_labels=True, node_color='lightblue',
            node_size=800, font_size=8, edge_color='gray',
            width=[d['weight']*0.2 for u,v,d in sub.edges(data=True)])
    plt.title("Rede de Transições de Códons - DENV-1 (Top 30)")
    plt.show()