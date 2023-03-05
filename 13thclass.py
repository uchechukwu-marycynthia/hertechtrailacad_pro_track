import pandas as pd
import numpy as np
Shop_dict={"Dorothy":pd.Series(data=[56,34,10],index=["Garri","burger","meat"]),
           "Faridat":pd.Series(data=[100,80,60],index=["Garri","chicken","potatoes"]),
           "Amara":pd.Series(data=[300,200,250],index=["Garri","rice","beans"])}
Shop_list=pd.DataFrame(Shop_dict)

print(Shop_list)
#adding a new column with unequal length
Shop_list["Nkechi"]=np.full(7,100)
print(Shop_list)
#instead of typing the length you can use length function or using any other method that will be dynamic
Shop_list["Ebuka"]=np.full(len(Shop_list),1000)
print(Shop_list)
#remove the nan valuesby filing it up with  0 toensure accraucy of the total 
#value not values
#print("\nfillup nan values with 0")
#Shop_list.fillna(value=0,inplace=True)
Shop_list["Total"]=Shop_list["Amara"]+Shop_list["Dorothy"]+Shop_list["Faridat"]+Shop_list["Nkechi"]+Shop_list["Ebuka"]
print(Shop_list)
#nulldatas above or close to 50% shouldnot be deleted nor average used rather 
#finding why they are there and maybe outsourcing for the actual valuewhich is a 
# major reason we have to determine the number of null values
print("\nSum of null values")
print(Shop_list.isnull().sum())
print("\nshows the total no of nulls")
print(Shop_list.isnull().sum().sum())
#not null
print("\nNon-Null values ina col")
print(Shop_list.count())
#.size shows the total no of elements in  a dataset
print("\nNo of elements")
print(Shop_list.size)
#.shape shows the no of rows and column
print("\nRow,Column")
print(Shop_list.shape)
#pandas method of writing length instead of using theconventional python len\
print("\nRow Length")
print(Shop_list.shape[0])
#how todrop a nan: todrop a nan use  dropna
#axis when using pandas siginifies every row
print("\ndrops a nan value")
print(Shop_list.dropna(axis=0))
#its a goodpractice in  data analyticstomake a 
#copy of the original and modify than tampering with the original
#how touse fillna to fill nan values
#As can be seen the total that  initially had nan had been chnged to 0 which is wrong so how do we rectify that
#so reassign the total column willdo justice to that but thats wrong coding principles 
#so the fillna is efected in line 16
#The below is efected but its of no use inrealsense becauseitjust copies the values up or down to fillup the nana value
print(Shop_list.fillna(method='ffill',axis=0))
print(Shop_list.fillna(method="backfill",axis=0))
#Before the above2 lines are used it musthave been thought out tobe the best approach but 
#most times interpolation is the best approach since it predicts the value by looking at the 
#surrounding values and backfill is used to fill up any remaining nan 
# interpolationis of 2 types linear and exponential
print("\nlinear interpolation")
print(Shop_list.interpolate(method="linear",axis=0))