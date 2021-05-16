import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

city_names = {1: 'chicago', 2: 'new york city', 3: 'washington'}

# this is a dictionary used to map each month to a number for better performance and reducing errors
month_names = {1: 'january', 2: 'february', 3: 'march',
               4: 'april', 5: 'may', 6: 'june', 7: 'all'}

# this is a dictionary used to map each day to a number for better performance and reducing errors
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
    # variables that the function will return
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

                # in case the user input is in valid state only
                city = city_names.get(city_index)
                print("you select index: {} for city name : {}".format(
                    city_index, city))
                break

            else:
                # in case the user chooses a number outside the range, i will raise an exception
                raise Exception('Invalid range, choose from 1 to 3 values\n')

        # Error handling
        except ValueError:
            # if user provides string instead of number
            print('Invalid input format, please provide a valid int\n')

        except Exception as error:
            # if user provides chooses a number outside the range,
            print(error)

        except KeyboardInterrupt:
            # if user wants to terminate the program
            print('Terminating Program, Goodbye :) \n')

    # get user input for month (all, january, february, ... , june)
    print('-'*40)

    while True:
        print('Secondly, could you specify month index : \n')
        print("1 for {} \n2 for {} \n3 for {}\n4 for {}\n5 for {}\n6 for {}\n7 for {}\n".format(
            'January', 'February', 'March', 'April', 'May', 'June', 'no filter'))
        user_input = input()
        try:
            month_index = int(user_input)
            if(month_index in range(1, 8)):
                month = month_names.get(month_index)
                print("you select index: {} for month name : {}".format(
                    month_index, month))
                break
            else:
                raise Exception('Invalid range, choose from 1 to 7 values\n')
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
    print("Most common month:{}\n".format(common_month))

    # display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("Most common day of week :{}\n".format(common_day))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common start hour :{}\n".format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print("Most commonly used start station:\n{}\n".format(common_start))

    # display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print("Most commonly used end station:\n{}\n".format(common_end))

    # display most frequent combination of start station and end station trip
    df['combination_col'] = df['Start Station'] + " to " + df['End Station']
    most_freq_com = df['combination_col'].mode()[0]
    print("Most frequent combination of start station and end station trip:\n{}\n".format(
        most_freq_com))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total travel time:{}\n".format(total_time))

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean travel time:{}\n".format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n{}\n".format(user_types))

    # if the data frame does not have the gender and birth year information
    if (('Gender' in df) and ('Birth Year' in df)):
        # Display counts of gender
        user_gender = df['Gender'].value_counts()
        print("Counts of user gender:\n{}\n".format(user_gender))

        # Display earliest, most recent, and most common year of birth

        # 1- display most common year
        most_common_year = df['Birth Year'].mode()[0]
        print("Most common year :\n{}\n".format(most_common_year))

        # 2- display earliest year
        earliest_year = df['Birth Year'].min()
        print("Earliest year :\n{}\n".format(earliest_year))

        # 3- display recent year
        recent_year = df['Birth Year'].max()
        print("Most recent year :\n{}\n".format(recent_year))

    else:
        print("Sorry the data file doesn't have information about gender and birth year\n")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_raw_data(df):
    print('l')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        print(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        break

        """
       
       
      
       

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
"""


if __name__ == "__main__":
    main()
