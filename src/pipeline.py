import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://admin:admin@localhost:5432/iot')

df = pd.read_csv('data/temperature_readings.csv')
# renomear colunas
df = df.rename(columns={
    'id': 'device_id',
    'noted_date': 'timestamp',
    'temp': 'temperature'
})

# converter timestamp
df['timestamp'] = pd.to_datetime(df['timestamp'], dayfirst=True)

print(df.head())

df.to_sql('temperature_readings', engine, if_exists='replace', index=False)

print("✅ Dados inseridos com sucesso!")