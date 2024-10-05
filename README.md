# Ecommerce
Análise de Dados de Vendas de um e-commerce fictício - Top 5 Marcas

Este projeto Python faz uma análise dos dados de vendas de um e-commerce, focando nas 5 marcas com maior quantidade de vendas. Várias visualizações são geradas para ilustrar as tendências dos dados, incluindo gráficos de dispersão, barras, pizza, densidade e um mapa de calor. O objetivo é fornecer insights visuais sobre os principais produtos vendidos, com base em seus preços e quantidade de vendas.

Requisitos
Antes de executar o código, certifique-se de que você tem as seguintes bibliotecas instaladas:
- Pandas: Para manipulação de dados.
- Matplotlib: Para criação de gráficos.
- Seaborn: Para visualizações de gráficos de alta qualidade.

Você pode instalar as bibliotecas necessárias com o seguinte comando:
pip install pandas 
pip install matplotlib 
pip install seaborn

 Estrutura do Código

1. Carregamento e Limpeza dos Dados

O código começa carregando um arquivo CSV (`ecommerce_preparados.csv`) contendo os dados de vendas de um  e-commerce fictício. Ele remove valores nulos em colunas específicas (`Marca`, `Qtd_Vendidos`, `Preço`) e garante que a coluna `Qtd_Vendidos` seja convertida para formato numérico.

2. Agrupamento e Seleção das 5 Maiores Marcas

Os dados são agrupados por marca e a soma das vendas é calculada. Em seguida, as 5 marcas com a maior quantidade de vendas são selecionadas, e os dados são filtrados para incluir apenas essas marcas.

 3. Visualizações Geradas

Gráfico de Dispersão - Preço vs Quantidade de Vendidos (Top 5 Marcas)
Mostra a relação entre o preço e a quantidade de vendidos, focando nas 5 principais marcas.

Gráfico de Barras - Quantidade de Vendidos (Top 5 Marcas)
Representa as 5 marcas com maior quantidade de vendas em um gráfico de barras, facilitando a visualização das diferenças entre elas.

Gráfico de Pizza - Distribuição Percentual das 5 Maiores Marcas por Vendas
Exibe a distribuição percentual das 5 principais marcas no total de vendas.

Gráfico de Densidade - Vendas das Top 5 Marcas
Mostra a densidade das vendas das 5 principais marcas, evidenciando a distribuição dos dados de vendas.

Mapa de Calor - Correlação entre Variáveis Normalizadas
Apresenta as correlações entre diferentes variáveis normalizadas (`Nota_MinMax`, `N_Avaliações_MinMax`, etc.) em um gráfico de calor.

4. Exibição dos Gráficos
Cada gráfico é exibido separadamente usando `plt.show()`, o que abre uma nova janela para cada visualização.

## Como Executar o Código

1. **Passo 1**: Certifique-se de que o arquivo `ecommerce_preparados.csv` esteja no mesmo diretório que o arquivo Python.
   
2. **Passo 2**: Execute o script Python.

```bash
python nome_do_arquivo.py
```

O script exibirá os gráficos conforme o processamento dos dados.

Possíveis Extensões

- Aprimorar os filtros de seleção: O código pode ser facilmente ajustado para exibir as 10 maiores marcas, ou outras métricas, além de quantidade de vendas.
- Adicionar interatividade: Utilizar bibliotecas como Plotly ou Dash para criar visualizações interativas.

Contribuição

Sinta-se à vontade para contribuir com este projeto! Sugestões e melhorias são sempre bem-vindas. Para qualquer dúvida, entre em contato.
