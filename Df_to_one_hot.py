import random
import pandas as pd
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()

values = data.whoAmI #записываем значения начального DataFrame
import numpy as np
classnames, indices = np.unique(values, return_inverse=True) #получаем названия уникальных переменных и их индексы в начальном фрейме
classnames = list(classnames)