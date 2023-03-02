import pandas as pd
import numpy as np

#although different wordings can be 
#used as aliases to this import pandas
#and numpy respectively but its advisable 
#to use the above conventional method

#Note that pandas is like an excel sheet 
#with both rows and columns
#the series below must be in capital letter

Shop_list = pd.Series(data=[500,200,300,1000],index=["tomatoes","pepper",("spices","meat"),"crayfish"])
#the above list is position sensitive
print(Shop_list)
#index above can either be strings or numbers and  dataframes are made 
#from blocks of this series and the above index and data are not positional
print(Shop_list.values)
#this just prints whats in the data
print(Shop_list.index)
#how to check if a particular string is in an array in a series
print("meat" in Shop_list.index)
print(1000 in Shop_list.values)
print(np.average([6,9,4,9,2]))
#iterating and or
#used when you are sure that a variable is there but you dont know if its an index or not
print("meat" in Shop_list.index or "meat" in Shop_list.values)
#always readup your error message since it helps to correct the code 
# 
#and for the code below the tuple must have the same variable arrangement
print(Shop_list["spices","meat"])
house_dues=pd.Series(index=["water","electricity","security","house_cleaning","Lawma"], data=[700,5000,100,530,1000])
#using the .loc to access values and not the double [] there the code wont run without it
print(house_dues.loc[["water","electricity"]])
print(np.mean(house_dues.loc[["water","electricity"]]))
print(house_dues[[0,-1]])
#also note the 2 [] above, its necessary
print(house_dues.iloc[[0,1]])
#iloc is majorly useful when the index and data are numbers 
foodstuffs=pd.Series(index=[1,2,3,4,5,6],data=[3500,1500,3000,4000,3000,5000])
print(foodstuffs.iloc[[0,1]])
print(foodstuffs[[1,2]])
#how to modify a value in a series 
house_dues["Lawma"]=860
print(house_dues)
#for multiple modification.Recall .loc can only be used for string
house_dues.loc[["security","water"]]=[200,500] 
print(house_dues)
#Deleting of a variable
house_dues.drop("house_cleaning",inplace=True)
print(house_dues)
#Another Deleting of a variable
house_dues=house_dues.drop("security")
print(house_dues)