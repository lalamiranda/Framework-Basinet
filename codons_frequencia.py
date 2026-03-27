import seaborn as sns
import matplotlib.pyplot as plt
from contar_codons import criar_dataframe_codons

df_top = criar_dataframe_codons()
plt.figure(figsize=(12,6))

sns.barplot(
    x="Codon",
    y="Frequencia",
    hue="DENV",
    data=df_top
)

plt.title("Top 10 Códons Mais Frequentes por DENV")
plt.xlabel("Códon")
plt.ylabel("Frequência")

plt.show()