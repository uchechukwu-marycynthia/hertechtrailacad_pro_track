
def main():
    get_name()
    menu()
    order_from()


def get_name():
    name = input('Name: ').title()
    print (f"{name}, welcome to Nigeria")


def menu():
    """
    Tells user what kind of Local food to eat based on  time and region.
 
    get_name function gets the users name, order_from function provides user 
    with the link to order the food from and also order any food of their choice,menu function 
    contains time function and get_location which gets the current time and also asks user to pick their region;
    it also contain the menu_west,menu_east and menu_south which is a combination of dict and list and tuples.
 
    Parameters:
    menu_west (list,tuple and dict): Different foods available in western region of Nigeria
                                     in the morning, afternoon and evening
    menu_east (list,tuple and dict): Different foods available in eastern regions of Nigeria
                                     in the morning, afternoon and evening
    menu_south (list,tuple and dict): Different foods available in southern region of Nigeria
                                     in the morning, afternoon and evening
    name(str): name of the user
    Location(str):location of user
 
    Returns:
    location and food to eat and where to get it
 
    """
    def get_location():
        Location = input(
                'which part of Nigeria are you in: 1) South-east | 2) South-south | 3) South-west  [1/2/3]? ')
        return(Location)
        

    
    def time():
        #how to get time of the day
        import datetime
        from datetime import date

        t = date.today()

        dt=t.strftime("%X")
        if "11:59:59am" >= dt :
            return ("Morning")
        elif  "4:59:59pm" <= dt:
            return ("Afternoon")
        elif "11:59:59pm" >= dt:
            return ("Evening")

    print ("Type a number 1-3")
    #dict of course meals in the  west
    Menu_west ={
            "Morning":["fried plantain with hot akamu, Ogi with akara, beans and akara,ghetto beans and bread"],
            "Afternoon":["beans and bread, kwunu mixed with milk and groundnut",
            "Jellof rice with fried plantain and egg", "Jellof spaghetti with fish and moimoi",
            "Jellof rice with moimoi and fish, Jellof rice with chicken and salad", "Amara and ewedu", 
            "Rice and stew with egg and beef", "beans and garri","yam and egg sauce","boole and groundut"],
            "Evening":("boiled plantain with sauce","fruit salad" )}

    #dict of course meals in the east
    Menu_east ={
            "Morning":["okpa and akamu, bread and akara, beverages,rice and ofe akwu"],
            "Afternoon":["pounded yam and nsala soup, akpu and bitterleaf soup, eba and okpono soup",
            "semovita and egusi soup, oha and eba, groundnut soup and akpu, achalla soup and eba","abacha, vegetable soup, ",
            "Jellof rice with fried plantain and egg", "Jellof spaghetti with fish and moimoi",
            "Jellof rice with moimoi and fish, Jellof rice with chicken and salad",  
            "Rice and stew with egg and beef", "beans and roasted plantain","yam and egg sauce","yam with vegetable"],
            "Evening":("ngwongwo with ngwo","fruit salad, isiewu with nkwu, garden egg leaf with ukpaka, oseoji and garden egg" )}


    #dict of course meals in the  south
    Menu_south ={
            "Morning":["beverages, beans and akara,beans and bread"],
            "Afternoon":["beans and bread, banga and starch,owo and starch, black soup and eba, leaf rice",
            "Jellof rice with fried plantain and egg", "Jellof spaghetti with fish and moimoi","marcorni and stew"
            "Jellof rice with moimoi and fish, Jellof rice with chicken and salad", "vegetable soup and eba", 
            "Rice and stew with egg and beef", "beans and garri","yam and egg sauce","yam and garden egg sauce"],
            "Evening":("roasted yam","fruit salad", "boiled plantain with garden egg sauce")}
         
    while time() == "Morning":
        if get_location()=="1":
            print(Menu_east["Morning"])
            break
        elif get_location()=="2":
            print(Menu_south["Morning"])
            break
        elif get_location()=="3":
            print(Menu_west["Morning"])
            break
        
        
    while time() == "Afternoon":
        if get_location()=="1":
            print(Menu_east["Afternoon"])
            break
        elif get_location()=="2":
            print(Menu_south["Afternoon"])
            break
        elif get_location()=="3":
            print(Menu_west["Afternoon"])
            break
        

    while time() == "Evening":
        if get_location()=="1":
            print(Menu_east["Evening"])
            break
        elif get_location()=="2":
            print(Menu_south["Evening"])
            break
        elif get_location()=="3":
            print(Menu_west["Evening"])
            break
        
def order_from():
    Order = ("For this and other much more delicacies,check out this link")
    print(f"{Order}, https://food.jumia.com.ng/")      

main()
#CODE REPETITION IS BAD