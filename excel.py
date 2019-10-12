import config
import os
from typing import List, Tuple, Dict
import pandas as pd

def all_path(dirname:str)->List[str]:
    result :List[str] = []

    for maindir, subdir, file_name_list in os.walk(dirname):
        for filename in file_name_list:
            apath:str = os.path.join(maindir, filename)
            result.append(apath)

    return result

if __name__ == "__main__":
    pathlist:List[str] = all_path(r"C:\Users\jjojjo\Desktop\201907")
    for apath in range(len(pathlist)):
        df :pd.core.frame.DataFrame = pd.read_excel(pathlist[apath], header=0) 
        column :pd.core.frame.Series = df.columns

