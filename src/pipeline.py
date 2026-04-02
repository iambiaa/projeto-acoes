import pandas as pd
import os
import yfinance as yf
import fundamentus

def run_pipeline():

    # ======================
    # DADOS DE MERCADO
    # ======================
    carteira_yf = ['ABEV3.SA', 'B3SA3.SA', 'GGBR4.SA', 'ITSA4.SA',
                   'PETR4.SA', 'RENT3.SA', 'SUZB3.SA', 'VALE3.SA', 'WEGE3.SA']

    df = yf.download(carteira_yf, start="2022-08-01", end="2023-08-01")

    cotacoes = df.stack(level=1).reset_index().rename(columns={"Ticker": "Ativo"})
    cotacoes.columns.name = None

    # ======================
    # DADOS FUNDAMENTALISTAS
    # ======================
    carteira_fund = ["ABEV3", "B3SA3", "GGBR4", "ITSA4",
                     "PETR4", "RENT3", "SUZB3", "VALE3", "WEGE3"]

    try:
        ind = fundamentus.get_papel(carteira_fund)[[
            'Setor', 'Cotacao', 'Min_52_sem', 'Max_52_sem',
            'Valor_de_mercado', 'Nro_Acoes', 'Patrim_Liq',
            'Receita_Liquida_12m', 'Receita_Liquida_3m',
            'Lucro_Liquido_12m', 'Lucro_Liquido_3m'
        ]]

        ind = ind.reset_index().rename(columns={'index': 'Ativo'})

        colunas = ['Cotacao', 'Min_52_sem', 'Max_52_sem', 'Valor_de_mercado',
                   'Nro_Acoes', 'Patrim_Liq', 'Receita_Liquida_12m',
                   'Receita_Liquida_3m', 'Lucro_Liquido_12m', 'Lucro_Liquido_3m']

        ind[colunas] = ind[colunas].apply(pd.to_numeric, errors='coerce')

        ind2 = fundamentus.get_resultado_raw().reset_index()
        ind2 = ind2.query('papel in @carteira_fund')
        ind2 = ind2[['papel', 'P/L', 'Div.Yield', 'P/VP', 'ROE']]

        ind2.rename(columns={'papel': 'Ativo', 'Div.Yield': 'DY'}, inplace=True)

        indicadores = pd.merge(ind, ind2, on='Ativo')

        indicadores['LPA'] = (indicadores['Lucro_Liquido_12m'] / indicadores['Nro_Acoes']).round(2)
        indicadores['VPA'] = (indicadores['Patrim_Liq'] / indicadores['Nro_Acoes']).round(2)

    except Exception as e:
        print("Erro no fundamentus:", e)
        indicadores = pd.DataFrame()

    # ======================
    # SALVAR ARQUIVOS
    # ======================
    os.makedirs("data", exist_ok=True)

    cotacoes.to_excel("data/cotacoes.xlsx", index=False)
    indicadores.to_excel("data/indicadores.xlsx", index=False)

# ======================
# EXECUÇÃO
# ======================
if __name__ == "__main__":
    run_pipeline()
