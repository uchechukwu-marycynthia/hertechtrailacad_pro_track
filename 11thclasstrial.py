import pandas as pd
import numpy as np

#although different wordings can be 
#used as aliases to this import pandas
#and numpy respectively but its advisable 
#to use the above conventional method

#Note that pandas is like an excel sheet 
#with both rows and columns
#the series below must be in capital letter

Shop_list = pd.Series(data=[500,200,300,500,1000],index=["tomatoes","pepper","spices","meat","crayfish"])
#the above list is position sensitive
print(Shop_list)