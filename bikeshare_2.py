import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

city_names = {1: 'chicago', 2: 'new york city', 3: 'washington'}

month_names = {1: 'january', 2: 'february', 3: 'march',
               4: 'april', 5: 'may', 6: 'june',
               7: 'july', 8: 'august', 9: 'september',
               10: 'october', 11: 'november', 12: 'december', 13: 'all'}

days_names = {1: 'saturday', 2: 'sunday', 3: 'monday',
              4: 'tuesday', 5: 'wednesday', 6: 'thursday',
              7: 'friday', 8: 'all'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    city = ''
    month = ''
    day = ''

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('You can terminate the process at any stage\n')
    while True:
        print('First, could you specify city index : \n')
        print("1 for {} \n2 for {} \n3 for {}".format(
            'chicago', 'new york city', 'washington'))
        user_input = input()
        try:
            city_index = int(user_input)
            if(city_index in range(1, 4)):
                city = city_names.get(city_index)
                print("you select index: {} for city name : {}".format(
                    city_index, city))
                break
            else:
                raise Exception('Invalid range, choose from 1 to 3 values\n')
        except ValueError:
            print('Invalid input format, please provide a valid int\n')
        except Exception as error:
            print(error)
        except KeyboardInterrupt:
            print('Terminating Program, Goodbye :) \n')

    # get user input for month (all, january, february, ... , june)
    print('-'*40)

    while True:
        print('Secondly, could you specify month index : \n')
        print("1 for {} \n2 for {} \n3 for {}\n4 for {}\n5 for {}\n6 for {}\n7 for {}\n8 for {}\n9 for {}\n10 for {}\n11 for {}\n12 for {}\n13 for {}".format(
            'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December', 'no filter'))
        user_input = input()
        try:
            month_index = int(user_input)
            if(month_index in range(1, 14)):
                month = month_names.get(month_index)
                print("you select index: {} for month name : {}".format(
                    month_index, month))
                break
            else:
                raise Exception('Invalid range, choose from 1 to 12 values\n')
        except ValueError:
            print('Invalid input format, please provide a valid int\n')
        except Exception as error:
            print(error)
        except KeyboardInterrupt:
            print('Terminating Program, Goodbye :) \n')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    print('-'*40)

    while True:
        print('Finally, could you specify day of week index : \n')
        print("1 for {} \n2 for {} \n3 for {}\n4 for {}\n5 for {}\n6 for {}\n7 for {}\n8 for {}".format(
            'Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'no filter'))
        user_input = input()
        try:
            day_index = int(user_input)
            if(day_index in range(1, 9)):
                day = days_names.get(day_index)
                print("you select index: {} for month name : {}".format(
                    day_index, day))
                break
            else:
                raise Exception('Invalid range, choose from 1 to 8 values\n')
        except ValueError:
            print('Invalid input format, please provide a valid int\n')
        except Exception as error:
            print(error)
        except KeyboardInterrupt:
            print('Terminating Program, Goodbye :) \n')

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
        df - pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(
        df['Start Time'], format='%Y-%m-%d %H:%M:%S')

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1

        # filter by month to create the new dataframe
        df = df.loc[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df.loc[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print(common_month)

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print(common_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print(common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print(common_start)

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print(common_end)

    # display most frequent combination of start station and end station trip
    print(df.loc[(df['Start Station'] == common_start)
                 & (df['End Station'] == common_end)])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time

    # display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types

    # Display counts of gender

    # Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        print(df)
        station_stats(df)

        break

        """
       
       
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
"""


if __name__ == "__main__":
    main()
