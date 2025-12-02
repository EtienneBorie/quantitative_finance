import pandas as pd

def sort_var_desc(df_var: pd.DataFrame) -> pd.DataFrame:
    df_sorted = df_var.sort_values(by="VAR_ANUAL", ascending=False)
    df_sorted = df_sorted.reset_index(drop=True)
    return df_sorted


def print_var_table(df_var: pd.DataFrame, confidence: float):
    nivel = int(confidence * 100)
    print(f"\nVaR anualizado (nivel de confianza {nivel}%)")
    print("-" * 60)
    for _, row in df_var.iterrows():
        print(f"{row['TICKER']:10s}  VaR anual: {row['VAR_ANUAL']:.6f}")