import numpy as np
import pandas as pd
data = np.arange(0, 20).reshape(5, 4)

df = pd.DataFrame(
    data,
    index=['row1', 'row2', 'row3', 'row4', 'row5'],
    columns=['col1', 'col2', 'col3', 'col4']
)
print(df)
print()
var = df.loc['row1']
print(type(var))
var3 = df.loc['row1', 'col1']
print(type(var3))