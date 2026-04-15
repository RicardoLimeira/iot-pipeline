# 📡 Pipeline de Dados IoT com Docker, PostgreSQL e Streamlit

## 🚀 Visão Geral

Este projeto tem como objetivo construir um pipeline completo de dados IoT, capaz de:

- 📥 Coletar dados de temperatura de dispositivos
- ⚙️ Processar e transformar os dados com Python
- 🗄️ Armazenar em um banco PostgreSQL via Docker
- 📊 Visualizar os dados em um dashboard interativo com Streamlit

---

## 🧠 Tecnologias Utilizadas

- 🐍 Python
- 🐳 Docker
- 🐘 PostgreSQL
- 📊 Streamlit
- 📈 Plotly
- 🧮 Pandas
- 🔗 SQLAlchemy

---

## 📁 Estrutura do Projeto


iot-pipeline/
│
├── data/
│ └── temperature_readings.csv
│
├── docs/
│ └── imagens
│
├── sql/
│ └── views.sql
│
├── src/
│ └── dashboard.py
│ └── pipeline.py
|
├── README.md
└── requirements.txt


---

## ⚙️ Como Executar o Projeto

### 🔹 1. Subir o PostgreSQL com Docker

```bash
docker run --name postgres-iot -e POSTGRES_USER=admin -e POSTGRES_PASSWORD=admin -e POSTGRES_DB=iot -p 5432:5432 -d postgres

🔹 2. Instalar dependências
pip install pandas sqlalchemy psycopg2-binary streamlit plotly

🔹 3. Executar o pipeline de dados
python src/pipeline.py

👉 Esse script:

Lê o CSV
Trata os dados
Insere no PostgreSQL

🔹 4. Criar as views SQL

Execute o arquivo sql/views.sql no banco de dados.

🔹 5. Executar o dashboard
streamlit run src/dashboard.py

👉 Acesse no navegador:

http://localhost:8501
📊 Dashboard

O dashboard apresenta:

📌 Média de Temperatura por Dispositivo
Visualização em gráfico de barras
📌 Leituras por Hora
Identifica padrões de uso ao longo do dia
📌 Temperatura Máxima e Mínima por Dia
Análise de variação térmica
🗄️ Views SQL Criadas
🔹 avg_temp_por_dispositivo

Calcula a média de temperatura por dispositivo

🔹 leituras_por_hora

Mostra a quantidade de leituras por hora

🔹 temp_max_min_por_dia

Exibe a temperatura máxima e mínima por dia

📈 Insights Obtidos
🔥 Identificação de dispositivos com maior aquecimento
⏰ Horários com maior volume de leituras
🌡️ Variação de temperatura ao longo do tempo
📊 Possível aplicação em monitoramento industrial e ambiental
📸 Demonstração

(Adicione aqui prints do dashboard na pasta /docs/imagens)

🎯 Objetivo Acadêmico

Este projeto foi desenvolvido como parte da disciplina:

Disruptive Architectures: IoT, Big Data e IA

Com foco em:

Integração de tecnologias modernas
Processamento de dados em larga escala
Visualização interativa
👨‍💻 Autor

Ricardo Limeira

🏁 Conclusão

Este projeto demonstra a construção de um pipeline de dados completo, integrando ingestão, armazenamento e visualização de dados IoT, utilizando ferramentas amplamente utilizadas no mercado.
