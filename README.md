# 🏅 Medallion Architecture Pipeline

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![Docker](https://img.shields.io/badge/docker-compose-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Sobre o Projeto

Este projeto implementa um pipeline de engenharia de dados seguindo os conceitos da **Arquitetura Medalhão**, focado na ingestão, normalização e persistência de dados.

O objetivo é demonstrar a manipulação de dados brutos (JSON/CSV) através de camadas de refinamento utilizando **Python e Pandas**, convertendo-os para formatos performáticos (**Parquet**) e, finalmente, disponibilizando-os em um Banco de Dados Relacional (**PostgreSQL**) para consumo.

---

## 🏗️ Arquitetura e Fluxo de Dados

O pipeline é executado através de scripts modulares que movem os dados entre as seguintes camadas lógicas:



### 1. 🥉 Bronze Layer (Raw)
* **Fonte:** APIs externas e arquivos locais (`users.csv`, `products.json`).
* **Processo:** Script `get_data.py`.
* **Armazenamento:** Arquivos crus armazenados no diretório `01-bronze-raw`.

### 2. 🥈 Silver Layer (Normalized)
* **Processo:** Script `normalize_data.py`.
* **Transformações:**
    * Limpeza de dados com **Pandas**.
    * Remoção de duplicatas.
    * Tratamento de tipagem (listas para strings).
    * Conversão para formato colunar comprimido (**Parquet**).
* **Armazenamento:** Arquivos `.parquet` no diretório `02-silver-normalized` (otimizados para leitura via PyArrow).

### 3. 🥇 Gold/Serving Layer (Database)
* **Processo:** Scripts `app.py` e `db.py`.
* **Ação:** Leitura da camada Silver e ingestão no banco de dados.
* **Armazenamento:** Tabela estruturada no **PostgreSQL** (via Docker), pronta para consultas SQL e conexão com ferramentas de BI.

---

## 🛠️ Tech Stack

### Linguagem & Processamento
* **Python 3.x**: Linguagem principal.
* **Pandas**: Manipulação e limpeza de dataframes.
* **NumPy**: Operações numéricas.

### Armazenamento & Formatos
* **Parquet (PyArrow)**: Formato de arquivo otimizado para a camada Silver.
* **PostgreSQL**: Banco de dados destino (Serving Layer).
* **CSV / JSON**: Formatos de entrada.

### Infraestrutura & Bibliotecas
* **Docker Compose**: Orquestração do container do banco de dados.
* **Psycopg2**: Conector Python-PostgreSQL.
* **Requests**: Consumo de APIs.

---

## 📂 Estrutura do Projeto

```bash
Medallion-Architecture/
├── 01-bronze-raw/       # Landing zone dos dados brutos
├── 02-silver-normalized/ # Dados tratados em Parquet
├── src/                 # (Ou raiz)
│   ├── get_data.py      # Ingestão (API -> Bronze)
│   ├── normalize_data.py # Processamento (Bronze -> Silver)
│   ├── app.py           # Carga (Silver -> Postgres)
│   └── db.py            # Classe de conexão com o Banco
├── docker-compose.yml   # Definição do serviço PostgreSQL
├── requirements.txt     # Dependências do projeto
└── README.md
