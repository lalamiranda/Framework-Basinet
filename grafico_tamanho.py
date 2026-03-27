import seaborn as sns
import matplotlib.pyplot as plt
from extrair_tamanho import criar_dataframe

# cria o dataframe vindo do outro arquivo
df = criar_dataframe()

plt.figure(figsize=(10,6))
sns.set_style("whitegrid")

sns.boxplot(x='DENV', y='Tamanho', data=df, palette='Set2')

sns.stripplot(
    x='DENV',
    y='Tamanho',
    data=df,
    color='black',
    size=3,
    alpha=0.5
)

plt.title('Distribuição do Tamanho das Sequências por Tipo de DENV')
plt.xlabel('Tipo de DENV')
plt.ylabel('Tamanho (nucleotídeos)')

plt.show()