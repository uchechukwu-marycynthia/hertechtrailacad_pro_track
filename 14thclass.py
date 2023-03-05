import  numpy as np
import pandas as pd
from tabulate import tabulate 

df=pd.read_csv("outfile.csv")
print("\nknow the num of rows and col")
#note its an attribute not a function to be called
print(df.shape)
#viewing of the first 5 rows ofthe dataset
print(df.head())
#dropping of a column
df.drop(columns=["Remarks","Value. Date","Reference","Originating Branch"],axis=1,inplace=True)

#Inthis data below we are going to drop all places that the transactional date
#  is nan (our deduction since  its a bank ststement).recall the no of rows is 13... 
# we definetly cant sscrollthrough toknow the row indexes
print(df.dtypes)
df["Debits"]=df["Debits"].str.replace(",","").astype(float)
df["Credits"]=df["Credits"].str.replace(",","").astype(float)
df["Balance"]=df["Balance"].str.replace(",","").astype(float)
print("\nnull values Removed")
nullrows=np.where(pd.isnull(df["Trans. Date"]))[0]
#note without the last 0 it will throw us an error b/c of the list is inside a tuple but we just need a list
df.drop(labels=nullrows,inplace=True)
#Situations where you need your index to be arranged in ascending order after dropping some rows then index need to be reset
df.reset_index(drop=True,inplace=True)
df.fillna(value=0,inplace=True)
#please ensure your type the below as seen keys not key
#youcan add the number of columns
print(tabulate(df.head(20),headers="keys",tablefmt="psql"))
Credits=np.sum(df.Credits)
debits=df["Debits"].sum()
avg_bal=round(np.mean(df.Balance),2)
print("\nThe total credits is {}  \nTotal debit is {} \nAvg balance is {}".format(Credits,debits,avg_bal))

#the below commented worked but it was displaying some other unneeded details
#start=df["Trans. Date"].iloc[[0]]
#end=df["Trans. Date"].iloc[[-1]]
start=df["Trans. Date"][0]
end=df["Trans. Date"][(len(df)-1)]
print("\nThis account statement starts from {} and ends  in {}".format(start,end))
#note during data cleaning relabel column name with spaces by adding _ to it since 
# some pd operations will require you to call the column like seen below




