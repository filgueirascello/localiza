#Exemplo de escrita direto

#Pacotes

import pandas as pd
from sqlalchemy import create_engine


#Paths
output_raw = "/Users/samuelfilgueiras/Library/CloudStorage/GoogleDrive-filgueirascello@gmail.com/Meu Drive/localiza/lake_localiza/raw"

output_silver = "/Users/samuelfilgueiras/Library/CloudStorage/GoogleDrive-filgueirascello@gmail.com/Meu Drive/localiza/lake_localiza/silver"

#output_gold_p1 = "/Users/samuelfilgueiras/Library/CloudStorage/GoogleDrive-filgueirascello@gmail.com/Meu Drive/localiza/lake_localiza/gold"

#output_gold_p2 = "/Users/samuelfilgueiras/Library/CloudStorage/GoogleDrive-filgueirascello@gmail.com/Meu Drive/localiza/lake_localiza/gold"

#Read on DataLake
df_raw = pd.read_parquet(output_raw)

df_silver = pd.read_parquet(output_silver)

#df_gold_p1 = pd.read_parquet(output_gold_p1)

#df_gold_p2 = pd.read_parquet(output_gold_p2)


#Engine para escrita no banco
engine = create_engine('postgresql+psycopg2://englocaliza:1234@localhost:5432/localiza')


#Escrita no banco
df_raw.to_sql('pessoas_raw', engine, if_exists='replace', index=False, schema='teste_engenheiro')

df_silver.to_sql('pessoas_silver', engine, if_exists='replace', index=False, schema='teste_engenheiro')

print("Dados inseridos com sucesso!")