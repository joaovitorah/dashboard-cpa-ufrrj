# Dashboard de Avaliação Institucional - CPA UFRRJ

![Status](https://img.shields.io/badge/Status-FinalizandoRespositorio-success) ![Tipo](https://img.shields.io/badge/Arquivo-Demonstrativo-orange)

## Sobre o Projeto

Este projeto apresenta uma solução de **Business Intelligence (BI)** desenvolvida para auxiliar a **Comissão Própria de Avaliação (CPA)** da **Universidade Federal Rural do Rio de Janeiro (UFRRJ)**.

O objetivo foi transformar os dados brutos das avaliações institucionais em painéis interativos visuais, permitindo identificar gargalos e pontos fortes nos cursos e departamentos da universidade.

---

##  Visualização e Funcionalidades

Abaixo estão demonstradas as principais telas e capacidades analíticas da ferramenta.

### 1. Visão Geral (Overview)
Painel principal que resume os índices gerais de satisfação da universidade.
**
![Tela Geral](caminho_para_sua_imagem_geral.png)

### 2. Filtros Dinâmicos
Capacidade de segmentar os dados por **Campus (Seropédica, Nova Iguaçu, Três Rios)** e **Instituto**.
**
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

Embora o código fonte seja restrito, a construção do projeto utilizou a seguinte stack tecnológica:

* **Processamento de Dados:** Python (Pandas) para limpeza e estruturação da base de dados da UFRRJ.
* **Visualização:** Power BI para renderização dos gráficos interativos.
* **Design:** Interface focada em usabilidade (UX) para gestores públicos.

---

##  Autor

Desenvolvido por **João Vitor Azevedo**
*Projeto desenvolvido para fins de apoio à gestão da CPA/UFRRJ.
