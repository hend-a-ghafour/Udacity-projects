import time
import calendar
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ["chicago","new york city","washington"]
selected_months = ["all", "january", "february", "march", "april", "may", "june"]
days = ["all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thursday", "friday"]
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Please, Insert the name of the city\n(Chicago, New York City, or Washington)\n > ").lower()
    while city not in cities:
        print('Sorry, The name you entered is not in our city data')
        city = input("Please, Insert the name of the city\n(Chicago, New York City, or Washington)\n > ").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Please, Insert the month\n (Months from January to June, or all)\n > ").lower()
    while month not in selected_months:
        print('Sorry, we do not have data for this input')
        month = input("Please, Insert the month\n (Months from January to June, or all)\n > ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Please, Insert the day\n (Days from Monday to Sunday, or all)\n > ").lower()
    while day not in days:
        print('Sorry, we do not have data for this input')
        day = input ("Please, Insert the day\n (Days from Monday to Sunday, or all)\n > ").lower()
    print ("You requested a data about Bikeshare in {} for {} month(s) on {} days ".format(city, month,day).title())

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekdays'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june"]
        month = months.index(month)+1
        df = df[df['month'] == month]
    if day != "all":
        df = df[df['weekdays'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    filtered_months = df['month'].nunique()
    common_month = df['month'].mode()[0]
    month_name = calendar.month_name[common_month]
    if filtered_months == 6:
        print("The most common month is: {}".format(month_name))
    else:
        print("{} is the only month you requested data about".format(month_name))
    """ 
    Here, I calculate the number of months in "df['month']" using ".nunique()" method , in order to use it in the conditional statement. Also the months numbers are converted into names using "calender.month_name()"
    """ 
    # TO DO: display the most common day of week
    filtered_days = df['weekdays'].nunique()
    common_day_of_week = df['weekdays'].mode()[0]
    if filtered_days == 7:
        print ("The most common day of the week is: {}".format(common_day_of_week))
    else:
        print("{} is the only day you requested data about".format(common_day_of_week))
        """ 
        Here, I calculate the number of months in "df['weekdays']" using ".nunique()" method , in order to use it in the conditional statement
        """ 
    # TO DO: display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour is: {}".format(common_start_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    commonly_used_S = df['Start Station'].mode()[0]
    print("The most commonly used start station is: {}".format(commonly_used_S))
    # TO DO: display most commonly used end station
    commonly_used_E = df['End Station'].mode()[0]
    print("The most commonly used end station is: {}".format(commonly_used_E))
    # TO DO: display most frequent combination of start station and end station trip
    S_E_combined = df['Start Station'] + " to " + df['End Station']
    commonly_used_S_E = S_E_combined.mode()[0]
    print("The most frequent combination of start station & end station trip is: from {}".format(commonly_used_S_E))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("The total travel time = ", total_travel_time)

    # TO DO: display mean travel time.
    travel_time_mean = df['Trip Duration'].mean()
    print("The average travel time = ", travel_time_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print ("The total number of each user type is :\n", user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print ("The total Number of each gender is:\n",gender)
    except KeyError as k:
        print ("The data regarding gender is not available")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        print ("The earliest birth year is: ", earliest)
    except KeyError as k:
        print ("The data regarding the earlist birth year is not available")    
    try:
        most_recent = int(df['Birth Year'].max())
        print("The most recent birth year is: ", most_recent)
    except KeyError as k:
        print ("The data regarding the most recent birth year is not available")        
    try:
        common_year = int(df['Birth Year'].mode())
        print ("The most common birth year is: ", common_year)
    except KeyError as k:
        print ("The data regarding the most common birth year is not available")          
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def row_data (df):
    row_data = input ("Would you like to see 5 rows of data?\n (Enter yes or no)\n> ").lower()
    start_loc = 0
    while row_data == "yes":
        print (df.iloc[start_loc:start_loc + 5])
        start_loc += 5
        row_data = input ("Do you wish to continue?\n(Enter yes or no)\n> ").lower()
        if row_data != "yes":
            break
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        row_data (df)
        
        
                   
        restart = input('\nWould you like to restart? \n(Enter yes or no)\n>')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
