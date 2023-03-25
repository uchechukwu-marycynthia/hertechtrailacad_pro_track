import time
import pandas as pd
import numpy as np
import datetime as dat
import matplotlib.pyplot as plt

CITY_DATA = { 'chicago': "chicago.csv",
              'new york city': "new_york_city.csv",
              'washington': "washington.csv" }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city_ref = int(input('What city would you like to get insight on?\navailable cities are chicago, new york city and washington.\npress 1  for chicago\npress 2 for new york city\npress 3 for washington\n'))

            city_list = ('chicago', 'new york city', 'washington')

        except Exception as e:
            print('\nPlease check your input!,\n Exception Occurred: {}, \n\n we don\'t have that city on our database\n'.format(e))

        else:
            city = city_list[(city_ref - 1)]
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('What month would you be interested in(Available for Jan - June)? \n input "ALL" if you prefer to see for all months: ').lower()
            assert month in ('all', 'january', 'february', 'march', 'april', 'may', 'june')
            break

        except Exception as e:
            print('Please check your input!,\n Exception Occurred: {}, \n\n You could have misspelt something or no data for selected month\n'.format(e))

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('What day are you interested in? \n input "ALL" if you prefer to see for all days: ').title()
            assert day in ('All', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday')
            break

        except Exception as e:
            print('Please check your input!,\n Exception Occurred: {}, \n\n You could have misspelt something\n'.format(e))

    print('-'*40 + '\n')
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('\n' + '.'*20 + 'retrieving data\n')
    df = pd.read_csv(CITY_DATA[str(city)],index_col=[0])
    narray=df.to_numpy()
    df.rename(columns={0:"id"},inplace =True)
    st=df["Start Station"].astype(str)+" to "+df["End Station"].astype(str)
    df.insert(6,column="Trip",value=st)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(str(month)) + 1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'All':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == str(day)]

    print('\nData Retrieved!!!\n')
    # Ask if user would like to preview data
    while True:
        try:
            preview = input('\nWould you like to preview the raw data? Enter yes or no.\n').lower()
            break
        except:
            print('oops!!!, check your input and try again\n')

    if preview == 'yes':
        print('\n','.'*10 + "loading city data\n")
        print('\n\n', df.head(), '\n')

        # Ask if user would like to view more raw data and in how many steps
        while True:
            try:
                preview_more = input('\nWould you like to preview more raw data? Enter yes or no.\n').lower()
                start_index = 5
                break
            except:
                print('\noops!!!, check your input and try again\n')

        if preview_more == 'yes':
            while len(df)-1 >= start_index+10:
                while True:
                    try:
                        steps = int(input('How many more rows would you like to see? (number from 1 - 10): \n'))
                        assert steps in range(11)
                        break
                    except:
                        print('\noops!!!, check your input and try again\n')

                print('\n','.'*10 + "loading {} more rows of city data\n".format(steps))
                print('\n', df.iloc[(start_index + 1):(start_index + 1 +steps)], '\n')
                start_index += steps

                #ask if user would like to view more
                while True:
                    try:
                        see_more = input('\nWould you like to preview more raw data? Enter yes or no.\n').lower()
                        break
                    except:
                        print('\noops!!!, check your input and try again\n')

                if see_more != 'yes':
                    print('\n\nAlright then, let\'s have a fun experience exploring your selected data.\n')
                    break

    else:
        print('\n\nAlright then, let\'s have a fun experience exploring your selected data.\n')


    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    if 'Start Time' and 'End Time' and 'month' and 'day_of_week' in set(df.columns):
        # TO DO: display the most common month
        if month == 'all':
            most_common_month = df['month'].mode()
            print('\nThe most common month(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
            for value in most_common_month.get_values():
                print(value)

        # TO DO: display the most common day of week
        if day == 'All':
            most_common_dow = df['day_of_week'].mode()
            print('\nThe most common day(s) of the week for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
            for value in most_common_dow.get_values():
                print(value)

        # TO DO: display the most common start hour
        df['start hour'] = df['Start Time'].dt.hour
        most_common_start_hour = df['start hour'].mode()
        print('\nThe most common start hour(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in most_common_start_hour.get_values():
            print(value, '(00)hrs')

        # TO DO: display the most common end hour
        df['end hour'] = pd.to_datetime(df['End Time']).dt.hour
        most_common_end_hour = df['end hour'].mode()
        print('\nThe most common end hour(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in most_common_end_hour.get_values():
            print(value, '(00)hrs')

        # display a count for total number of completed trips
        trip_count = df['end hour'].count()
        print('\nThe total number of trips for City: {}, Month: {}, Day: {} is:\n{} {}'.format(city,month,day,trip_count,'Trip(s)'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df, city, month, day):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    if 'Start Station' in set(df.columns):
        common_start_station = df['Start Station'].mode()
        print('\nThe most commonly used start station(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in  common_start_station.get_values():
            print(value)

    # TO DO: display most commonly used end station
    if 'End Station' in set(df.columns):
        common_end_station = df['End Station'].mode()
        print('\nThe most commonly used end station(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in common_end_station.get_values():
            print(value)

    # TO DO: display most frequent combination of start station and end station trip
    if 'Start Station' in set(df.columns) and 'End Station' in set(df.columns):
        df['Trip Combination'] = df['Start Station'] + ' ' + 'to' + ' ' + df['End Station']
        most_common_trip = df['Trip Combination'].mode()
        print('\nThe most frequent trip(s) for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in most_common_trip.get_values():
            print(value)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    if 'Trip Duration' in set(df.columns):
        total_travel_time = df['Trip Duration'].sum()
        print('\nThe total travel time for City: {}, Month: {}, Day: {} is:\n{} {}'.format(city,month,day,total_travel_time,'Seconds'))

    # TO DO: display mean travel time
        mean_travel_time = np.mean(df['Trip Duration'])
        print('\nThe mean travel time for City: {}, Month: {}, Day: {} is:\n{} {}'.format(city,month,day,mean_travel_time,'Seconds'))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city, month, day):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if 'User Type' in set(df.columns):
        user_type_count = df['User Type'].value_counts()
        print('\nThe User type Count for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),user_type_count)

    # TO DO: Display counts of gender
    if 'Gender' in set(df.columns):
        gender_count = df['Gender'].value_counts()
        print('\nThe Gender Count for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in set(df.columns):
        earliest_yob = int(df['Birth Year'].min())
        print('\nThe earliest year of birth of users for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),earliest_yob)

        most_recent_yob = int(df['Birth Year'].max())
        print('\nThe most recent year of birth of users for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),most_recent_yob)

        most_common_yob = df['Birth Year'].mode()
        print('\nThe most common year(s) of birth of users for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day))
        for value in most_common_yob.get_values():
            print(int(value))

    # Display age range distribution of users
    # The code block below was gotten from defltstack.com literature and modified to access current year
    current_DateTime = dat.datetime.now()
    current_date = current_DateTime.date()
    current_year = int(current_date.strftime("%Y"))

    # create new column to label age class distribution
    if 'Birth Year' in df.columns:
        #create a new column for age class
        df['Age Class'] = df['Birth Year'].copy()

        #create list of index where class is true
        #idx_Babies = (np.where(2019 <= df['Birth Year'].get_values() < 2022))
        #idx_Children = (np.where(2005 <= df['Birth Year'].get_values() < 2019))
        #idx_Young_Adults = (np.where(1991 <= df['Birth Year'].get_values() < 2005))
        #idx_Middle_aged_Adults = (np.where(1976 <= df['Birth Year'].get_values() < 1991))
        #idx_Old_Adults = np.where(df['Age Class'].get_values > 1976)[0]

        # create dictionary for age class. Age class as Key and list label as value
        #age_class_dict = {'Babies':idx_Babies, 'Children':idx_Children, 'Young_Adults':idx_Young_Adults, 'Middle_aged_Youths':idx_Middle_aged_Adults, 'Old_Adults':idx_Old_Adults}
        #age_class_dict = {'Old Adults':idx_Old_Adults}

        # modify age class column to labels for age class
        for row in df.itertuples():
            i = row.Index
            if (current_year-2)<=df.loc[i,'Birth Year'] and df.loc[i,'Birth Year']<(current_year + 1):
                df.loc[i, 'Age Class'] = 'Babies (0-2yrs)'
            elif (current_year - 16)<=df.loc[i,'Birth Year'] and df.loc[i,'Birth Year']<(current_year - 2):
                df.loc[i, 'Age Class'] = 'Children (3-16yrs)'
            elif (current_year - 30)<=df.loc[i,'Birth Year'] and df.loc[i,'Birth Year']<(current_year - 16):
                df.loc[i, 'Age Class'] = 'Young Adults (17-30yrs)'
            elif (current_year - 45)<=df.loc[i,'Birth Year'] and df.loc[i,'Birth Year']<(current_year - 30):
                df.loc[i, 'Age Class'] = 'Middle aged Adults (31-45yrs)'
            else:
                df.loc[i, 'Age Class'] = 'Old Adults (above 45yrs)'


        # get count of distinct values in age class column
        age_dist_count = df['Age Class'].value_counts()
        print('\nThe age demographic for City: {}, Month: {}, Day: {} is:\n'.format(city,month,day),age_dist_count)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def plot(rows=3, cols=2, dashboard_size=(30,20)):
    #Create figure and subplots for the Dasboard
    #The code below is a sample dashboard config that can take 6 plots in a 3 rows by 2 columns arrangement
    #You are to expand this function to plot all your visuals at the end in one dashboard view. 
    fig, axs = plt.subplots(rows, cols, figsize=dashboard_size)
    #line graphs
    #most common trip
    plt.plot(df["id"].value_counts(),df["Trip"])
    plt.title("Frequency of Trip")
    plt.xlabel("id count")
    plt.ylabel("Trip")
    plt.show()

    #frequency of service use
    plt.plot(df["id"].value_counts(),df["usertype"])
    plt.title("Frequency of service use")
    plt.xlabel("id count")
    plt.ylabel("Start Station")
    plt.show()

    #column Chart
    #Avg trip duration for male and female

    #gender(legend),agegroup(x-axis) and count of users(y-axis)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        while True:
            '''The next four lines of code does a quick statistical summary of the data.
                You should modify the print statements in their functions above to make the print happen inside the dashboard 
                You should also carry out your own exploratory data analysis to produce insightful charts that can be plotted in the dashboard

            '''
            
            time_stats(df, city, month, day)
            station_stats(df, city, month, day)
            trip_duration_stats(df, city, month, day)
            user_stats(df, city, month, day)

            plot()

            see_another_stat = input('\nWould you like to see another statistics? Enter yes or no.\n')
            if see_another_stat.lower() != 'yes':
                break



        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
