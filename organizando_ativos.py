import requests
import pandas as pd

# Passo 1: Extração de dados
url = 'URL_DA_FONTE_AQUI'  # Substitua pela URL ou fonte de dados real
response = requests.get(url)

# Verifique se a solicitação foi bem-sucedida
if response.status_code == 200:
    data = response.json()  # Supondo que os dados estejam em formato JSON
else:
    print("Falha na extração de dados.")
    exit()

# Passo 2: Transformação de dados
# Realize as transformações necessárias nos dados (limpeza, manipulação, etc.)
# Vamos supor que os dados estejam em uma lista de dicionários com campos relevantes

# Exemplo de transformação: Converter para DataFrame do pandas
df = pd.DataFrame(data)

# Passo 3: Carregamento de dados
# Carregue os dados transformados em um arquivo CSV como exemplo
output_file = 'chainsaw_man_episodes.csv'
df.to_csv(output_file, index=False)

print(f'Dados carregados com sucesso para {output_file}.')
