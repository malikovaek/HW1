import numpy as np
import pandas as pd
from scipy.stats import ttest_ind


def estimate_first_type_error(df_pilot_group, df_control_group, metric_name, alpha=0.05, n_iter=10000, seed=None):
    """Оцениваем ошибку первого рода.

    Бутстрепим выборки из пилотной и контрольной групп тех же размеров, считаем долю случаев с значимыми отличиями.

    df_pilot_group - pd.DataFrame, датафрейм с данными пилотной группы
    df_control_group - pd.DataFrame, датафрейм с данными контрольной группы
    metric_name - str, названия столбца с метрикой
    alpha - float, уровень значимости для статтеста
    n_iter - int, кол-во итераций бутстрапа
    seed - int or None, состояние генератора случайных чисел.

    return - float, ошибка первого рода
    """
    # YOUR_CODE_HERE
    np.random.seed(seed)

    rejected = 0
    for i in range(n_iter):
        pilot = np.random.choice(df_pilot_group[metric_name], size=len(df_pilot_group[metric_name]), replace=True)
        control = np.random.choice(df_control_group[metric_name], size=len(df_control_group[metric_name]), replace=True)
        if ttest_ind(pilot, control)[1] < alpha:
            rejected += 1
    return rejected / n_iter
