
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Carregue o arquivo CSV usando o pandas
data = pd.read_csv("gasolina.csv")

# Crie um gráfico de linha com o Seaborn
sns.set(style="whitegrid")  
sns.lineplot(x='dia', y='venda', data=data, label='Vendas de Gasolina')

# Adicione um título ao gráfico
plt.title('Vendas de Gasolina ao Longo do Tempo')

# Adicione uma legenda
plt.legend(loc='upper right')

# Adicione rótulos aos eixos (opcional)
plt.xlabel('Dia')
plt.ylabel('Volume de Vendas')

# Salve o gráfico como gasolina.png usando o Matplotlib
plt.savefig('gasolina.png')

# Exiba o gráfico
plt.show()
