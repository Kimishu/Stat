from graphics import create_bar_chart
import matplotlib.pyplot as plt
from scipy.stats import expon
from points import *
from interval_estimation import *
import numpy as np
import seaborn as sb


def complex_explore(data: list) -> None:

    create_bar_chart(data)

    # point estimators
    print('/' * 50)
    
    print(f'Среднее значение                : {get_mean(data)}')
    print(f'Медиана                         : {get_median(data)}')
    print(f'Дискретная мода                 : {get_discrete_moda(data)}')
    print(f'Интервальная мода               : {get_interval_moda(data)}')
    print(f'Квадратный корень из отклонения : {get_square_root_deviation(data)}')
    print(f'Дисперсия                       : {get_square_root_deviation(data) ** 2}')
    
    print('/' * 50)

    # interval estimators
    print('/' * 50)

    print(f'Доверительный интервал: ')
    print(f'       {get_mean_intervals(data)}')
    print(f'       {get_sq_dev_intervals(data)}')

    print('/' * 50)

    # special values
    print('/' * 50)

    print(f't-value               : {t_test(data)}')
    print(f'z-value               : {z_test(data)}')
    print(f'f-value               : {f_test(data)}')

    print('/' * 50)


    normal_check(data)
