from Backend.data_loader import get_ishares_tickers, load_prices
from Modules.DataProcessing import pivot_prices, compute_returns
from Backend.risk_calculator import compute_var_per_ticker
from Backend.utils import sort_var_desc, print_var_table


def main():
    # 1) Definir portafolio 
    tickers = get_ishares_tickers()

    # 2) Definir rango de fechas
    start_date = "2023-01-01"
    end_date = "2024-12-31"

    # 3) Cargar precios desde el backend
    df_prices = load_prices(
        tickers=tickers,
        start=start_date,
        end=end_date)

    # 4) Calcular retornos diarios
    df_prices_pivot = pivot_prices(df_prices)
    df_returns = compute_returns(df_prices_pivot)

    # 5) Calcular VaR individual
    df_var = compute_var_per_ticker(
        df_returns=df_returns,
        alpha=0.05  )

    # 6) Ordenar ETFs de mayor a menor riesgo
    df_var_sorted = sort_var_desc(df_var)

    # 7) Imprimir resultado
    print_var_table(df_var_sorted, confidence=0.95)


if __name__ == "__main__":
    main()

