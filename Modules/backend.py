import pandas as pd
import numpy as np


def market_prices(start_date: str, end_date: str, tickers: list[str]) -> pd.DataFrame:
    fechas = pd.date_range(start=start_date, end=end_date, freq="B")
    data = []

    for ticker in tickers:
        precio = 100.0
        retornos = np.random.normal(loc=0.0002, scale=0.01, size=len(fechas))
        precios = [precio]

        for r in retornos[1:]:
            precios.append(precios[-1] * (1 + r))

        for f, p in zip(fechas, precios):
            data.append({
                "FECHA": f,
                "TICKER": ticker,
                "EMISOR": "iShares",
                "PRECIO_CIERRE": p
            })

    return pd.DataFrame(data)
