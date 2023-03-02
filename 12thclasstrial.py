import numpy as np
import pandas as pd

shop_list = pd.Series(index=["eggs","bread","milk","cornflakes","Cashewnut"], data=[2500,500,1200,1000,200])
print(shop_list + 500)
#You can as well do substract,division,multiplication as seen above
print(np.sqrt(shop_list))
print(np.power(shop_list,1/4))