# Sistema-de-Recomendacao-de-Filmes
Sistema de Recomendação de Filmes (Fast API, AirFLow, Streamlit, Duckdb)



Este projeto foi desenvolvido para criar um sistema de recomendação de filmes mais eficiente, atendendo às necessidades de uma empresa de streaming. Nosso objetivo é melhorar a assertividade das recomendações, aumentando a satisfação e o engajamento dos usuários finais.

Funcionalidades

Dashboard Interativo: Visualize métricas como popularidade dos filmes, avaliações médias, e tendências segmentadas por gênero e outros filtros.

Sistema de Armazenamento Escalável: Os dados são organizados e armazenados utilizando o DuckDB para consultas analíticas eficientes.

API REST: Desenvolvida com FastAPI, a API permite acesso rápido e seguro aos dados.

Automação de Fluxos de Dados: Gerenciada com Apache Airflow, garantindo a ingestão e processamento contínuos de dados.

Tecnologias Utilizadas

DuckDB: Banco de dados para análise rápida e centralizada dos dados.

FastAPI: Framework para desenvolvimento da API.

Streamlit: Ferramenta para criação do dashboard interativo.

Airflow: Automação e agendamento dos processos de ETL.

Estrutura do Projeto

Armazenamento de Dados: Os dados de avaliações são organizados em arquivos CSV processados pelo DuckDB.

API: Comunicação eficiente entre os dados armazenados e o dashboard.

Dashboard: Interface para visualização e exploração dos dados.

Automação: Airflow para gerenciar a ingestão e atualização dos dados.
