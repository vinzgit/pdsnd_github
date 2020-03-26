import time
import pandas as pd
import numpy as np
import calendar

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    
    while True:
        city = input("Would you like to see data for Chicago, New York City or Washington?: ").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print ("Sorry you have typed in an incorrect name - please try again")
        else:
            break

    # TO DO: get    user input for month (all, january, february, ... , june)
    
    while True:
        userdata = input("Would you like to filter the data by Month, Day, or All?: ").lower()
        if userdata == "month":
            print ("We will make sure to filter by month")
            month = input("Which month? January, February, March, April, May, June or All? Please type out the full month name: ").lower()
            if month not in ['january', 'february', 'march', 'april', 'may', 'june', 'all']:
                print ("Sorry you have typed in an incorrect month - please try again")
            else:
                day = 'All'
                break

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        
        elif userdata == "day":
            print ("We will make sure to filter by day")
            day = input("Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?: ").title()
            if day not in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']:
                print ("Sorry you have typed in an incorrect day - please try again")
            else:
                month = 'all'
                break

        elif userdata == "all":
            month = 'all'
            day = 'All'
            break

        else:
            print ("You have typed in an incorrect entry. Please try again")


    


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

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        return df[df['Start Time'].dt.month == month]
    elif day != 'All':
        return df[df['day_of_week'] == day]
    else:
        return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].value_counts().idxmax()
    print('The most common month is: ', calendar.month_name[popular_month-1])


    # TO DO: display the most common day of week
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    popular_day = df['day_of_week'].value_counts().idxmax()
    print('The most common day of the week is: ', popular_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    print('The most frequent start hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print ("The most commonly used start station is: ", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print ("The most commonly used end station is: ", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combined_start_end = ("Start station: "+df['Start Station']+" / "+"End station: "+df['End Station']).value_counts().idxmax()
    print ("The most frequent combination of start/end station is: ", combined_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    print ("The total travel time is: {0:,.0f} minutes".format(total_duration))

    # TO DO: display mean travel time
    mean_duration = df['Trip Duration'].mean()
    print ("The total mean travel time is: {0:,.0f} minutes".format(mean_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print ("The number of people based on user type is: \n{}\n".format(user_count))

    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print ("The number of people based on gender is: \n{}\n".format(gender_count))
    except KeyError:
        print ("No data are available for the gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_year = df['Birth Year'].min()
        print ("The earliest birth year is: {:.0f}".format(earliest_year))

        recent_year = df['Birth Year'].max()
        print ("The most recent birth year is: {:.0f}".format(recent_year))

        common_year = df['Birth Year'].value_counts().idxmax()
        print ("The most common birth year is: {:.0f}".format(common_year))

    except KeyError:
        print ("No data are available for the birth year")

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """
    Asks user if they want to see 5 lines of raw data.
    Returns the 5 lines of raw data if user inputs `yes`. Iterate until user response with a `no`

    """

    count = 5

    while True:
        answer = input('Would you like to see 5 lines of raw data? Enter yes or no: ').lower()
        
        # Check if response is yes, print the raw data and increment count by 10
        
        if answer == 'yes':
            print (df[:count])
            if count == len(df):
                count +=0
            else:
                count += 10
        elif answer == 'no':
            break
        else:
            print ("Please answer 'yes' or 'no'")
        # otherwise break
        
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

