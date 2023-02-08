def my_function(nthclass):
    print("Welcome to todays class which is the {}th".format(nthclass))

my_function(8)
#power of positional argument
def nname(fname,lname):
    print("my firstname is {} and my surname is {}".format(fname,lname))

nname("Gozie", "Ikebudu")
#the position only matters at the def and fuction calling
def nname(fname,age):
    print("I am {} yrs old and my name is {}".format(age,fname))

nname("Gozie", 24)
#since I might forget their positions its advisable i follow through with the manual asignment soitwillrun
def nname(fname,age,yr):
    print("I am {} yrs old and my name is {}. Its year {}".format(age,fname,yr))

nname(age=24,fname="Gozie",yr=2023)
# you can specify the parameter when definig the function and can still overide it 
# by specifiying a new parameter when callingthe function

def nname(fname,age,yr=2023):
    print("I am {} yrs old and my name is {}. Its year {}".format(age,fname,yr))

nname(age=24,fname="Gozie", yr=2024)
#how to pass a function without deleting it
def nname(fname,age,yr):
    pass
#    print("I am {} yrs old and my name is {}. Its year {}".format(age,fname,yr))

#nname(age=24,fname="Gozie",yr=2023)
#return statement hands out the result from a function
def nname(fname,age,yr):
    return("I am {} yrs old and my name is {}. Its year {}".format(age,fname,yr))

nname(age=24,fname="Gozie",yr=2023)
#see how this code is called
def nname(fname,age,yr):
    return("I am {} yrs old and my name is {}. Its year {}".format(age,fname,yr))

result=nname(age=24,fname="Gozie",yr=2023)
print(result)


WFO = ["Monday", "Wednesday", "Friday"]
WFH = ["Tuesday", "Thursday"]
WKD = ["Saturday", "Sunday"]


def my_alarm(wrk_office_days, wrk_home_days, weekends):
    """
    summary 

 
    Extended description of function.
 
    Parameters:
    wrk_office_days (list): Days of the week the person needs to work from the office
    wrk_home_days (list): Days of the week the person needs to work from home
    weekends(list): Days of the week that are weekend days
    nickname(str): nickname of the user
 
    Returns:
    An alarm note of action for what the person should do
 
    """
    DOW = (input("What day is it?: ")).title()
    nickname = (input("What do your friends call you?: ")).lower()
#while loop alone ensures codecontinues running until we are satisfied
    
    if DOW in WFO:
        return("Hi {}! Get off from your bed and prepare for work, its {}".format(nickname, DOW))
    elif DOW in WFH:
        return("Hi {}! You get to work from home today, it's {}".format(nickname, DOW))
    elif DOW in WKD:
        return("Hi {}! Have some rest and get on with your social life, its {}".format(nickname, DOW))
    else:
        return("This is not a recognized day of the week")

permission = "Start"
while permission == "Start":
    my_alarm_message = my_alarm(wrk_office_days=WFO, wrk_home_days=WFH, weekends=WKD)
    print("\n{}....Thank you for using Chukwudi Global Limited Alarms\n".format(my_alarm_message))


    while True:
        check=input("\nDo you want to go again? (Y:Yes, N:No): ").upper()
        if check == "Y":
            break
        elif check == "N":
            print("Have some fun.... see you later")
            permission = "Stop"
            break

        else:
            print("wrong input")
            