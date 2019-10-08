import pandas as pd
import numpy as np
# 导入数据集，定义index_col='user_id'  
users=pd.read_csv("https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user", sep='|', index_col='user_id')
print(users.tail(10))
print(len(users))