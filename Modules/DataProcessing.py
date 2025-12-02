import pandas as pd


def pivot_prices(df_prices: pd.DataFrame) -> pd.DataFrame:
    df_pivot = pd.pivot_table(
        data=df_prices,
        index="FECHA",
        columns="TICKER",
        values="PRECIO_CIERRE",
        aggfunc="max"
    )
    return df_pivot


def compute_returns(df_prices: pd.DataFrame) -> pd.DataFrame:
    df_ret = df_prices.pct_change().dropna()
    return df_ret
