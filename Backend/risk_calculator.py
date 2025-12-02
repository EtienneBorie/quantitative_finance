import pandas as pd
from Modules.RiskMetrics import var_normal_series

def compute_var_per_ticker(df_returns: pd.DataFrame, alpha: float = 0.05) -> pd.DataFrame:
    resultados = []

    for ticker in df_returns.columns:
        serie = df_returns[ticker].dropna()
        var_anual = var_normal_series(serie, alpha=alpha, annualize=True)
        resultados.append({
            "TICKER": ticker,
            "VAR_ANUAL": var_anual
        })

    df_var = pd.DataFrame(resultados)
    return df_var