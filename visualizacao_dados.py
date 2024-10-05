import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('ecommerce_preparados.csv')
print(df.head().to_string())

# Remover linhas com valores nulos em 'Marca', 'Qtd_Vendidos' e 'Preço'
df_dropna = df[['Marca', 'Qtd_Vendidos', 'Preço']].dropna()

# Converte 'Qtd_Vendidos' para numérico
df_dropna['Qtd_Vendidos'] = pd.to_numeric(df_dropna['Qtd_Vendidos'], errors='coerce')

# Remove as linhas que não puderam ser convertidas para numérico
df_dropna = df_dropna.dropna(subset=['Qtd_Vendidos'])

# Agrupa por marca e soma a quantidade de vendidos
df_agrupado = df_dropna.groupby('Marca')['Qtd_Vendidos'].sum()

# Seleciona as 5 marcas com maior quantidade de vendas
top5_marcas = df_agrupado.nlargest(5).index

# Filtra os dados para incluir apenas as linhas das 5 maiores marcas
df_top5 = df_dropna[df_dropna['Marca'].isin(top5_marcas)]

# Gráfico de Dispersão - Preço vs Quantidade de Vendidos (Top 5 Marcas)
plt.figure(figsize=(10, 6))
plt.scatter(df_top5['Preço'], df_top5['Qtd_Vendidos'])
plt.title('Dispersão - Preço vs Quantidade de Vendidos (Top 5 Marcas)')
plt.xlabel('Preço')
plt.ylabel('Qtd_Vendidos')
plt.show()

# Gráfico de Barras - Quantidade de Vendidos (Top 5 Marcas)
plt.figure(figsize=(10, 6))
x = df_agrupado.nlargest(5).index  # Marcas
y = df_agrupado.nlargest(5).values  # Quantidade de vendidos
plt.bar(x, y, color='#60aa65')
plt.title('Top 5 Marcas - Quantidade de Vendidos')
plt.xlabel('Marca')
plt.ylabel('Quantidade de Vendidos')
plt.xticks(rotation=45)
plt.show()

# Gráfico de Pizza - Distribuição Percentual das 5 Maiores Marcas por Vendas
plt.figure(figsize=(8, 6))
plt.pie(y, labels=x, autopct='%.1f%%', startangle=90)
plt.title('Distribuição Percentual das 5 Maiores Marcas por Vendas')
plt.show()

# Gráfico de Densidade - Vendas das Top 5 Marcas
plt.figure(figsize=(10, 8))
sns.kdeplot(df_top5['Qtd_Vendidos'], fill=True, color='#863e9c')
plt.title('Densidade de Vendas - Top 5 Marcas')
plt.xlabel('Quantidade de Vendidos')
plt.ylabel('Densidade')
plt.show()

# Mapa de Calor
plt.figure(figsize=(6, 4))
colunas_minmax = ['Nota_MinMax', 'N_Avaliações_MinMax', 'Desconto_MinMax', 'Preço_MinMax', 'Qtd_Vendidos_Cod']

matriz_correlacao_minmax = df[colunas_minmax].corr()
sns.heatmap(matriz_correlacao_minmax, annot=True, cmap='coolwarm')
plt.title('Mapa de Calor - Correlação de Variáveis Normalizadas')
plt.tight_layout()
plt.show()








