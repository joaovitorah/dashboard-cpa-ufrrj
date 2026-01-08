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
![Tela Geral](caminho_para_sua_imagem_geral.png)

### 2. Filtros Dinâmicos
Capacidade de segmentar os dados por **Campus (Seropédica, Nova Iguaçu, Três Rios)** e **Instituto**.
![Filtros](caminho_para_sua_imagem_filtros.png)

### 3. Análise Temporal
Gráfico de linha comparando a evolução das notas nos últimos 3 anos.
![Evolução Temporal](caminho_para_sua_imagem_temporal.png)

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

* **Python (Pandas):** Scripts de automação para extração e tratamento (ETL) dos dados brutos da COTIC.
* **Power BI:** Renderização dos gráficos interativos e publicação do dashboard.
* **UX Design:** Interface focada em usabilidade para gestores públicos.

---

## Autor

Desenvolvido por **João Vitor Azevedo**
*Projeto desenvolvido para fins de apoio à gestão da CPA/UFRRJ.*
