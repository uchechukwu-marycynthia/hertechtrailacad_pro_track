import numpy as np
import pandas as pd

shop_list = pd.Series(index=["eggs","bread","milk","cornflakes","Cashewnut"], data=[2500,500,1200,1000,200])
print(shop_list + 500)
print("\nsubtraction")
print(shop_list- 250)
print("\nmulitplication")
print(shop_list*4)
print("\nDivision")
print(shop_list/1.5)

print("All the above change is temporary\n")
#note:inplace makes any change a permanent one 
#You can as well do substract,division,multiplication as seen above
print("\n Square")
print(np.sqrt(shop_list))
#square ofthedata
print("\nraise to power")
print(np.power(shop_list,1/4))
#raised to the power
print("\nExponential")
print(np.exp(shop_list))
#np makes it easier to execute mathematical expression in one line
#without not having to write multiple lines of code
#adding arithemitic expression to only a key
shop_list["eggs"]=shop_list["eggs"]-500
print(shop_list)
#creating your own dataframe makes it easier for you to understand although most times you import a file
print("\ndict of series")
Shop_dict={"Dorothy":pd.Series(data=[56,34,10],index=["cheese","burger","meat"]),
           "Faridat":pd.Series(data=[100,80,60],index=["cocoyam","chicken","potatoes"]),
           "Amara":pd.Series(data=[300,200,250],index=["Garri","rice","beans"])}
Shop_list=pd.DataFrame(Shop_dict)
print(Shop_list)
#dataframes can automatically add its own index when not specified
print("\nAccessing values in a dataframe")
print(Shop_list["Amara"]["Garri"])
print(Shop_list.iloc[0,2])
#adding a new column with unequal length
Shop_list["Nkechi"]=np.full(9,0)
print(Shop_list)
#instead of typing the length you can useloength function or using any other method that will be dynamic
Shop_list["Ebuka"]=np.full(len(Shop_list),1000)
print(Shop_list)