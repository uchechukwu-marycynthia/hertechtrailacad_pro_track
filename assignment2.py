import pandas as pd
import numpy as np
from tabulate import tabulate

gp=pd.read_csv("googleplaystore.csv")
print("Row,column")
print(gp.shape)
print("\n",tabulate(gp.head(),headers="keys",tablefmt="psql"))