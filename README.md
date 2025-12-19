# 🏅 Medallion Architecture Pipeline

![Status](https://img.shields.io/badge/status-active-success)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green)

## 📋 Sobre o Projeto

Este repositório contém a implementação de um pipeline de Engenharia de Dados baseado na **Arquitetura Medalhão (Medallion Architecture)**. O objetivo é demonstrar o fluxo de processamento de dados desde a ingestão bruta até a disponibilização de insights de negócios, garantindo qualidade, governança e rastreabilidade.

O projeto simula um cenário real de ETL/ELT, onde os dados são progressivamente refinados através de camadas lógicas.

---

## 🏗️ A Arquitetura (Bronze, Silver, Gold)

O fluxo de dados segue o padrão de design de lakehouse/data warehouse dividido em três camadas principais:



### 1. 🥉 Bronze Layer (Raw)
* **Objetivo:** Armazenar os dados em seu formato original, imutável.
* **Características:** Dados "as-is" (como vieram da fonte), histórico completo, permitindo reprocessamento.
* **Formatos:** [Ex: JSON, Parquet, CSV].

### 2. 🥈 Silver Layer (Cleansed/Enriched)
* **Objetivo:** Dados limpos, filtrados e estruturados.
* **Transformações:** Remoção de duplicatas, tratamento de nulos, tipagem de dados (schema enforcement) e normalização.
* **Uso:** Fonte da verdade para cientistas de dados e análises ad-hoc.

### 3. 🥇 Gold Layer (Curated/Business)
* **Objetivo:** Dados agregados e prontos para consumo de negócios (BI/Reporting).
* **Características:** Modelagem dimensional (Star Schema), agregações, KPIs calculados.
* **Uso:** Dashboards, relatórios executivos.

---

## 🛠️ Tech Stack

As principais tecnologias e bibliotecas utilizadas neste projeto:

* **Linguagem:** Python
* **Processamento:** [Ex: PySpark, Pandas, Polars]
* **Armazenamento/Formato:** [Ex: Delta Lake, Parquet, Postgres, DuckDB]
* **Orquestração:** [Ex: Airflow, Prefect, Script Manual]
* **Qualidade de Dados:** [Ex: Great Expectations, Pydantic]

---

## 📂 Estrutura do Projeto

```bash
Medallion-Architecture/
├── data/
│   ├── bronze/       # Dados brutos
│   ├── silver/       # Dados tratados
│   └── gold/         # Dados de negócio
├── src/
│   ├── ingestion/    # Scripts de ingestão (Source -> Bronze)
│   ├── transformation/ # Scripts de limpeza (Bronze -> Silver)
│   └── aggregation/  # Regras de negócio (Silver -> Gold)
├── notebooks/        # Jupyter Notebooks para exploração
├── requirements.txt  # Dependências do projeto
└── README.md
