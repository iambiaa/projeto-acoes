# 💭 Projeto - Dados de Ações

Pipeline automatizado de coleta, processamento e análise de dados de ações da B3, combinando cotações históricas via yfinance com indicadores fundamentalistas via fundamentus. O objetivo é fornecer um panorama completo da saúde financeira das empresas, permitindo que investidores estruturem e acompanhem a evolução de suas carteiras.

## 🖥 Tecnologias utilizadas

- Python
- Pandas
- yfinance
- Fundamentus
- GitHub Actions

## 📈 Funcionalidades

- Coleta de cotações históricas — Preços de abertura, fechamento, máxima, mínima e volume para um período definido
- Dados fundamentalistas — Setor, cotação atual, valor de mercado, patrimônio líquido, receita líquida e lucro líquido (12 e 3 meses)
- Indicadores de valuation — P/L, P/VP, Dividend Yield e ROE diretamente do Fundamentus
- Cálculo de LPA e VPA — Lucro por Ação e Valor Patrimonial por Ação calculados automaticamente
- Exportação para Excel — Dois arquivos gerados: cotacoes.xlsx e indicadores.xlsx

## 📑 Pipeline de dados

1. Coleta de dados de mercado (yfinance)
2. Coleta de dados fundamentalistas (fundamentus)
3. Tratamento e padronização dos dados
4. Geração de arquivos Excel
5. Atualização automática via GitHub Actions
6. Consumo dos dados no Power BI

## 📍 Objetivo

Demonstrar habilidades em:
- Analise de dados
- ETL (Extract, Transform, Load)
- Automação de pipelines
- Integração com ferramentas de BI

## 🤝 Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request com melhorias, novos indicadores ou suporte a outras bolsas.
