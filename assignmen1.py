import pandas as pd
#dict of of list
Paye =pd.DataFrame({
    "Designation":["GENERAL MANAGER","CLEANER","PRODUCTION SUPERVISOR","PROCUREMENT OFFICER","FINANCE MANAGER",
    "IT MANAGER","QUALITY CONTROL MGR","OPERATOR"],
    "Basic_sal":[900,200,300,400,1000,600,550,430],
    "Tax_payable":[51,25,36,13,60,24,21,15],
    "Tax_ID":["N-3511063","N-5599638","N-1682407","N-5463085","N-4372194","N-5463077","N-4104278","N-3716994"]
},index=["ABAYOMI KUJORE","ADAMS DELE","AYODELE CHRISTIANA","BOBBY VICTOR","AZUBUIKE EBERE" ,
    "NWAIWU Emeka","AMINU Abosede","MULERO Joseph"])

#list of dict
Fact_sal = pd.DataFrame([
    {"Gross_sal":203,"Housing_allow":301,"Loan_repay":15,"THT_dedu":20},
    {"Gross_sal":300,"Housing_allow":401,"Loan_repay":10,"THT_dedu":20}
],index=["Abiade Ganiyat","Oyewole Sukurat"])
print(Paye)
print(Fact_sal)
#add a new row
print("\nadding new rows using loc\n")
Paye.loc["Odubuiyi Kehji"]= {
    "Designation":"Front Desk","Basic_sal":100,
    "Tax_payable":12,"Tax_ID":"N-4373889"
    }
print(Paye)
#add new rows
print("\nadding of new rows using concat\n")
Paye2=pd.DataFrame({
    "Designation":["Marketing","Production"],"Basic_sal":[500,300],"Tax_payable":[18,35],
    "Tax_ID":["N-4377682","N-4372175"]},index=["Oke Olayemi", "Okoye Chioma"])
paye=pd.concat([Paye,Paye2])
print(paye)  
#loc cannot be used to add multiple rows but concat or Paye.append(Paye2) does a good job
# add new columns
print("\n adding using loc and bracket\n")
paye.loc[:, ["Dev_levy"]]=[10,10,10,10,10,10,10,10,10,10,10]
print(paye)
#Note forthe above to work the len must correspond
#new column with bracket
paye["Nationality"]=["NIG","GHN","NIG","USA","CND","NIG","NGN","SNG","NGN","NIG","IRQ"]
print(paye)
#adding new columns using insert
print("\n inserts column in desired position\n")
paye.insert(0,"Exits_in_Etax",["Y","N","Y","Y","Y","Y","Y","N","Y","N","Y"])
print(paye)
#The above inserts the column in the desired position
print("\nRename a row\n")
paye.rename(index={"NWAIWU Emeka":"Emeka Hudson"},inplace=True)
print(paye)
print("\nRename multiple rows\n")

paye.rename(index={"AMINU Abosede":"Aminu Precious","Okoye Chioma":"Obidike Chioma"},
columns={"Tax_ID":"Tax_id","Basic_sal":"Gross_sal"},inplace=True)
print(paye)

print("\nChange index position of a column\n")
Pa=paye.set_index(["Tax_id"])
print(Pa)
print("\nThe change of the index col is temporary and what happens to the previous index column\n")
new_order=[2,4,3,1,-1,0,5]
print(paye[paye.columns[new_order]])
print("\nThe order of arrangement is temporary too\n")
#Delete rows
paye.drop(index={"AZUBUIKE EBERE","ABAYOMI KUJORE"},inplace=True)
print(paye)
print("\nDeleting of rows\n")
#Delete columns
paye.drop(columns="Dev_levy",inplace=True)
print(paye)
