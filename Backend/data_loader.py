import pandas as pd
from modules.backend import market_prices

def get_ishares_tickers() -> list[str]:
    return ["IVV", "AGG", "IEMG", "IJR"]


def load_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    df = market_prices(start_date=start, end_date=end, tickers=tickers)
    df = df[["FECHA", "TICKER", "PRECIO_CIERRE"]].copy()
    return df