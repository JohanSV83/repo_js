import numpy as np
import pandas as pd

dt=pd.to_datetime(['2024-07-03','2024-07-04','2021-01-01'])

df=pd.DataFrame({
    'year':[2024,2025,2026],
    'month':[1,2,3],
    'day':[1,3,4]
}, index=dt)

print(type(df))






