# creating the main menu for running calendar app
import sys


def main():
    """
    The main function draws the main menu. If the chosen operation is not a valid option (1-5),
    this should be printed and menu() should be called again. 5 exits the app. All other options
    should call the respective function. Until the functions are written, print statements and a
    menu() call should be in its place to verify correct behavior.
    :return:
    """
    print('.....MAIN MENU.....')
    print('1. Plan new run')
    print('2. See next planned run')
    print('3. Enter completed run')
    print('4. Statistics over completed runs')
    print('5. Exit program')

    choice = input('Choose your operation: ')
    if choice not in '12345':
        print('Please choose from the items 1-5')
        main()
    elif choice == '1':
        print('New run chosen ...')
        main()
        #new_run()
    elif choice == '2':
        print('Next run chosen ...')
        main()
        #next_run()
    elif choice == '3':
        print('Completed run chosen ...')
        main()
        #completed_run()
    elif choice == '4':
        print('See statistics chosen  ...')
        main()
        #run_statistics()
    elif choice == '5':
        sys.exit()
    else:
        print('Choose only one operation at a time ...')
        main()

# Start the main menu if the main_menu file is the one run
if __name__ == '__main__':
    main()
