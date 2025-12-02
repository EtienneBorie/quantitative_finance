import numpy as np
import pandas as pd
from scipy import stats


def var_normal_series(returns: pd.Series, alpha: float = 0.05,
                      annualize: bool = True, trading_days: int = 252) -> float:
    # volatilidad diaria
    sigma = returns.std()

    # percentil de la normal estándar (negativo)
    z_alpha = stats.norm.ppf(alpha)

    # VaR diario (en valor absoluto)
    var_diario = abs(z_alpha) * sigma

    if annualize:
        var_anual = var_diario * np.sqrt(trading_days)
        return var_anual
    else:
        return var_diario
