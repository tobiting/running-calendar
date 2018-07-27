# create the functions needed for database communication

import sqlite3
import datetime
import os
import main_menu        # module that handles the main interface menu function


def db_connect():
    """
    Create a connection and TABLE run_data if database does not exist,
    else only connect to the database. Return value is a tuple with connection
    object and cursor object. These can be used for database manipulation
    and to commit changes and close the connection.
    """
    if 'run_database.db' not in os.listdir():
        conn = sqlite3.connect('run_database.db')
        # Create a cursor object to manipulate the database file
        c = conn.cursor()
        c.execute("CREATE TABLE run_data (run_id INTEGER, run_date TEXT, run_distance REAL, run_time REAL)")
        return conn, c
    else:
        conn = sqlite3.connect('run_database.db')
        # Create a cursor object to manipulate the database file
        c = conn.cursor()
        return conn, c


def check_data_entry(run_distance, run_time):
    """
    A function to guarantee that the inputs of run distance and time
    are convertible to floats. If they are not, the data should be entered
    again by a call to completed_run() function. Also, the user will get a
    second prompt to verify that the data entered was the correct data. If
    the data was correct, the return value should be True, otherwise False.
    """
    try:
        float(run_distance)
        float(run_time)
    except Exception:
        print('You need to input your distance and time as a number.')
        completed_run()
    correct = input(f'Are the inputs {run_distance} km and {run_time} minutes correct? (Y/N): ').upper()
    if correct == 'Y' or correct == 'YES':
        print('Input to be added to your log.')
        return True
    else:
        print('Please enter your correct data.')
        return False


def completed_run():
    """
    Input run distance and run time from a completed run. Run distance and time
    should be written into the database TABLE run_data together with the current
    date and a unique run id that counts the total number of runs.
    """
    # Collect data from completed run and check if they are correctly entered
    run_distance = input('Input your run distance (km): ')
    run_time = input('Input your run time (minutes): ')
    data_entries = check_data_entry(run_distance, run_time)
    if data_entries == False:
        completed_run()

    # Convert entered data to float
    run_distance = float(run_distance)
    run_time = float(run_time)

    # Connect to the database
    conn, c = db_connect()

    # Fetch all run_ids to calculate new_run_id to enter into database
    c.execute("SELECT run_id FROM run_data")
    all_ids = c.fetchall()
    if not all_ids:
        new_run_id = 1
    else:
        new_run_id = all_ids[-1][0] + 1

    # Insert the data of the newly completed run into the database
    c.execute("INSERT INTO run_data VALUES (?,?,?,?)",
              (new_run_id, str(datetime.date.today()), run_distance, run_time))

    # Print out current TABLE entries
    #c.execute("SELECT run_id FROM run_data")
    #print(c.fetchall())
    #c.execute("SELECT run_distance FROM run_data")
    #print(c.fetchall())

    # Commit changes to database, close connection and go back to main menu
    conn.commit()
    conn.close()
    main_menu.main()
