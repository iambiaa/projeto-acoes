# 📈 Pipeline de Dados de Ações — B3
 
> Pipeline automatizado de coleta, processamento e análise de ações da B3, combinando cotações históricas e indicadores fundamentalistas para acompanhamento de carteiras de investimento.
 
---
 
## 🎯 Objetivo
 
Demonstrar habilidades em engenharia e análise de dados construindo um pipeline completo do zero — da coleta à visualização no Power BI.
 
- **ETL** — coleta, transformação e carga de dados financeiros reais
- **Automação** — pipeline agendado via GitHub Actions sem intervenção manual
- **Análise** — indicadores de valuation e saúde financeira das empresas
- **Visualização** — consumo dos dados no Power BI para acompanhamento de carteira
---
 
## 🛠️ Tecnologias
 
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat&logo=github-actions&logoColor=white)
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat&logo=power-bi&logoColor=black)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white)
 
---
 
## 🗂️ Estrutura do repositório
 
```
projeto-acoes/
│
├── README.md
├── .github/
│   └── workflows/
│       └── pipeline.yml       # Agendamento automático via GitHub Actions
│
├── src/
│   ├── cotacoes.py            # Coleta de preços históricos via yfinance
│   ├── fundamentalistas.py    # Coleta de indicadores via fundamentus
│   └── pipeline.py            # Orquestração do pipeline completo
│
└── data/
    ├── cotacoes.xlsx          # Preços históricos exportados
    └── indicadores.xlsx       # Indicadores fundamentalistas exportados
```
 
---
 
## ⚙️ Pipeline de dados
 
```
1. Coleta de cotações históricas     →   yfinance
         ↓
2. Coleta de dados fundamentalistas  →   fundamentus
         ↓
3. Tratamento e padronização         →   pandas
         ↓
4. Exportação para Excel             →   cotacoes.xlsx + indicadores.xlsx
         ↓
5. Atualização automática            →   GitHub Actions (agendado)
         ↓
6. Visualização                      →   Power BI
```
 
---
 
## 📊 Dados coletados
 
### Cotações históricas (`cotacoes.xlsx`)
Preços de abertura, fechamento, máxima, mínima e volume para um período definido — coletados via **yfinance**.
 
### Indicadores fundamentalistas (`indicadores.xlsx`)
 
| Indicador | Descrição |
|---|---|
| Setor | Setor de atuação da empresa |
| Cotação atual | Preço de mercado no momento da coleta |
| Valor de mercado | Capitalização total da empresa |
| Patrimônio líquido | Valor contábil dos ativos menos passivos |
| Receita líquida | Receita dos últimos 12 e 3 meses |
| Lucro líquido | Lucro dos últimos 12 e 3 meses |
| P/L | Preço sobre Lucro — indicador de valuation |
| P/VP | Preço sobre Valor Patrimonial |
| Dividend Yield | Retorno em dividendos |
| ROE | Retorno sobre o Patrimônio Líquido |
| LPA | Lucro por Ação — calculado automaticamente |
| VPA | Valor Patrimonial por Ação — calculado automaticamente |
 
---
 
## 🚀 Como reproduzir
 
**1. Clone o repositório**
```bash
git clone https://github.com/seu-usuario/projeto-acoes.git
cd projeto-acoes
```
 
**2. Instale as dependências**
```bash
pip install pandas yfinance fundamentus openpyxl
```
 
**3. Execute o pipeline**
```bash
python src/pipeline.py
```
 
Os arquivos `cotacoes.xlsx` e `indicadores.xlsx` serão gerados na pasta `data/`.
 
---
 
## 🤖 Automação com GitHub Actions
 
O pipeline é executado automaticamente via GitHub Actions em um agendamento definido. A cada execução os arquivos Excel são atualizados com os dados mais recentes e commitados de volta ao repositório — prontos para consumo no Power BI.
 
---
Projeto desenvolvido como parte do portfólio de entrada na área de dados.
