# create function to draw run history

import sqlite3
import os
import numpy as np
import matplotlib.pyplot as plt
import main_menu                    # module that draws main menu


def run_statistics():
    """
    This function will retrieve data from the database containing the
    completed runs. It should then visualize this data in a bar-plot.
    Both run_time and run_distance should be shown in the same diagram.
    """
    # connect to the database and create cursor
    if 'run_database.db' in os.listdir():
        conn = sqlite3.connect('run_database.db')
        c = conn.cursor()
    else:
        print('No database available')
        main_menu.main()

    # retrieve all the run_ids and convert the data to an array
    # data is converted to numpy array to be able to to element-wise arithmetic
    c.execute("SELECT run_id FROM run_data")
    run_ids = c.fetchall()
    run_ids = np.array([run_ids[i][0] for i in range(len(run_ids))])

    # retrieve all the run_distances and convert the data to an array
    # data is converted to numpy array to be able to to element-wise arithmetic
    c.execute("SELECT run_distance FROM run_data")
    run_distances = c.fetchall()
    run_distances = np.array([run_distances[k][0] for k in range(len(run_distances))])

    # retrieve all the run_times and convert the data to an array
    # data is converted to numpy array to be able to to element-wise arithmetic
    c.execute("SELECT run_time FROM run_data")
    run_times = c.fetchall()
    run_times = np.array([run_times[k][0] for k in range(len(run_times))])

    # create bar-plot with run_id on x-axis and run_distances and run_time on y-axis
    fig, ax1 = plt.subplots()
    bar1 = ax1.bar(run_ids - 0.125, run_distances, 0.25, color='C1', label = 'Distance')
    ax1.set_xlabel('Run number')
    ax1.set_ylabel('Run distance (km)', color='C1')

    # create another y-axis with different scale for run_times
    ax2 = ax1.twinx()
    bar2 = ax2.bar(run_ids + 0.125, run_times, 0.25, color='C0', label = 'Time')
    ax2.set_ylabel('Run time (minutes)', color='C0')
    fig.tight_layout()
    plt.title('Run distance and time for each completed run')
    plt.show()

    # close the connection to the database
    conn.close()

    # go back to main menu
    main_menu.main()
