# Dashboard de Avaliação Institucional - CPA UFRRJ

![Status](https://img.shields.io/badge/Status-Finalizando_Repositório-orange) ![Tipo](https://img.shields.io/badge/Arquivo-Demonstrativo-orange)

## Sobre o Projeto

Este projeto apresenta uma solução de **Business Intelligence (BI)** desenvolvida para auxiliar a **Comissão Própria de Avaliação (CPA)** da **Universidade Federal Rural do Rio de Janeiro (UFRRJ)**.

O objetivo foi transformar os dados brutos das avaliações institucionais em painéis interativos visuais, permitindo identificar gargalos e pontos fortes nos cursos e departamentos da universidade.

---

Por motivos de **segurança da informação ez proteção de dados (LGPD)**, o arquivo fonte (`.pbix`) não está disponível neste repositório público, pois contém dados sensíveis da comunidade acadêmica da UFRRJ.

No entanto, a versão pública e interativa (com dados anonimizados ou agregados) pode ser acessada através do link abaixo:

### 🔗 [CLIQUE AQUI PARA ACESSAR O DASHBOARD ONLINE](https://app.powerbi.com/view?r=eyJrIjoiMjI0MzVlNDEtZWJkZS00MjhkLTg1OWEtZTJhOTMyZjY5OTlhIiwidCI6IjcwZGM2ZWM0LTc0YjEtNGMyNy04MWY5LWQwMmVlMmU1NzM5NiJ9)

---
*Este link leva para a versão publicada via Power BI Service.

## ⚙️ Engenharia de Dados e Automação (ETL)

Um dos maiores desafios deste projeto foi a integração e tratamento dos dados brutos fornecidos pela **COTIC (Coordenadoria de Tecnologia da Informação e Comunicação)**. Para garantir a integridade das análises, foi desenvolvido um pipeline de **ETL (Extract, Transform, Load)** robusto.

* **Desafio:** Os dados originais apresentavam inconsistências de formatação e fragmentação entre diferentes sistemas, departamentos, cardinalidades da universidade e falta de anonimizaçao dos dados.
* **Solução:** Foram desenvolvidos **scripts em Python (Pandas)** para automatizar a limpeza, padronização e unificação dessas bases.
* **Legado:** O script foi estruturado para ser reutilizável, permitindo que a automação do tratamento de dados seja aplicada em **ciclos avaliativos futuros**, reduzindo drasticamente o tempo de preparação de relatórios nos próximos anos.

---

## Visualização e Funcionalidades

Abaixo estão demonstradas as principais telas e capacidades analíticas da ferramenta.

### 1. Visão Geral (Overview)
Painel principal que resume os índices gerais de satisfação da universidade.
<img width="1014" height="593" alt="image" src="https://github.com/user-attachments/assets/34ed95a1-1ced-4365-a8cd-6887534bace8" />)


### 2. Filtros Dinâmicos
Capacidade de segmentar os dados por **Campus (Seropédica, Nova Iguaçu, Três Rios)** e **Instituto**.
<img width="1041" height="610" alt="image" src="https://github.com/user-attachments/assets/2e9fc29f-2237-42db-9198-81ee50ef7441" />


### 3. Análise Temporal
Gráfico de linha comparando a evolução das notas nos últimos semestres.
<img width="1028" height="605" alt="image" src="https://github.com/user-attachments/assets/be0a3602-d620-44f2-9df1-db56d3471897" />

---

## Modelo de Relatório Padronizado

Junto ao desenvolvimento técnico do dashboard, foi elaborada uma metodologia para a descrição textual dos gráficos nos relatórios oficiais da CPA. O padrão estabelecido garante consistência na comunicação dos dados.

**Estrutura Lógica de Descrição:**

> **1. Contextualização:** Define qual eixo ou dimensão está sendo analisado (ex: Infraestrutura, Didática).
>
> **2. Evidência Quantitativa:** Cita os números exatos apresentados no dashboard (ex: *"82% de aprovação"*).
>
> **3. Análise Qualitativa:** Interpreta o dado em relação à meta institucional ou histórico (ex: *"Houve superação da meta estipulada em 2022..."*).

*O modelo completo de relatório utilizado como base para estas descrições pode ser visualizado na pasta `/docs` deste repositório.*

---

## Arquitetura e Tecnologias

A construção do projeto utilizou a seguinte stack tecnológica:

* **Python (Pandas):** O script (`etl_limpeza_cpa.py`) implementa técnicas de Hashed-based Anonymization (SHA-256) para assegurar que nenhum dado pessoal identificável (PII) seja carregado para o ambiente de visualização, em estrita conformidade com a LGPD.
* **Power BI:** Renderização dos gráficos interativos e publicação do dashboard.
* **UX Design:** Interface focada em usabilidade para gestores públicos.

---

## Roadmap e Trabalhos Futuros

O projeto atual representa a primeira fase da modernização da análise de dados da CPA. O planejamento para as próximas etapas visa a **automação total do pipeline de dados**, eliminando a necessidade de extração manual de arquivos.

### Metas de Evolução da Arquitetura:

* ** Integração via API (Endpoints):**
    * Substituição do recebimento de arquivos estáticos (.xlsx/.csv) pelo desenvolvimento de **Endpoints RESTful** seguros.
    * Objetivo: Conectar o script de ETL diretamente ao banco de dados do Sistema Acadêmico (respeitando as camadas de segurança da COTIC), permitindo a extração dos dados brutos via requisição HTTP.

* ** Orquestração de ETL (Data Pipeline):**
    * Implementação de orquestradores (como *Apache Airflow* ou *Cron Jobs*) para executar o script de limpeza automaticamente ao fim de cada ciclo avaliativo.
    * Isso garante que, assim que a avaliação fecha no sistema, os dados já sejam tratados e disponibilizados.

* ** Atualização em "Real-Time" do BI:**
    * Configuração do **Power BI Gateway** para leitura direta da base tratada (Data Warehouse).
    * O dashboard passará a refletir o cenário da avaliação institucional minutos após o processamento dos dados, sem intervenção humana manual.

### Fluxo de Evolução (Diagrama)
<img width="8192" height="470" alt="Untitled diagram-2026-01-12-064641" src="https://github.com/user-attachments/assets/82e548ed-671b-4461-8957-395decd4eaec" />



## Autoria e Colaboração

**Desenvolvedor Líder:** João Vitor Azevedo

O desenvolvimento deste dashboard ocorreu em **interação constante com os Grupos de Trabalho (GTs)** da CPA/UFRRJ.

A estrutura dos painéis reflete a segmentação da comissão, onde as regras de negócio e indicadores foram validados periodicamente com cada grupo responsável, garantindo aderência às necessidades reais da avaliação institucional.
