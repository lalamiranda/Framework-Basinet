import seaborn as sns
import matplotlib.pyplot as plt
from contar_bases import criar_dataframe_bases

df_bases = criar_dataframe_bases()

plt.figure(figsize=(10,6))

sns.barplot(
    x="Base",
    y="Quantidade",
    hue="DENV",
    data=df_bases
)

plt.title("Frequência de Nucleotídeos por Tipo de DENV")
plt.savefig("grafico_denv.png", dpi=300, bbox_inches='tight')
plt.show()