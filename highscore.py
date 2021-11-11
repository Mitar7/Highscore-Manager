"""
    Highscore Manager
    Mitar Milovanovic
    Python 3.9
    11.11.2021
"""

import os
from sys import exit

msg = """   
|---------------------|
|      Highscore      |
|---------------------|
|   1. Read file      |
|   2. Write in file  |
|   3. Delete record  |
|   4. Exit           |
|_____________________|
    """


# clears window
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# Read Highscore file and sort by scores
def read_file():
    highscore = {}

    clear()
    print('\n Highscores: \n')
    with open('hs.txt', 'r') as f:
        for line in f.readlines():
            if len(line) > 1:
                name, score = line.split(' ')
                highscore[name] = int(score)

    highscore = {k: v for k, v in sorted(highscore.items(), key=lambda item: item[1], reverse=True)}
    for key, value in highscore.items():
        print(key + ' ' + str(value))
    print('\n')
    x = input("Press Enter to return to main menu...")

    clear()
    main_program()


# Write new records into a file
def write_file():
    clear()
    print("Insert new record\n")
    name = input('Enter name: ')
    score = int(input('Enter score: '))

    if len(name) > 3:
        if score > 0:
            with open('hs.txt', 'a') as f:
                f.write('\n' + name + ' ' + str(score))
            x = input("Press Enter to return to main menu...")
            clear()
            main_program()
        else:
            print('Invalid score (score needs to be positive)!')
            x = input("Press Enter to try again...")
            clear()
            write_file()
    else:
        print('Invalid name!')
        x = input("Press Enter to try again...")
        clear()
        write_file()


# Delete record from the file
def delete_record():
    clear()
    print("\nDelete record\n")
    highscore = {}

    clear()
    print('\n Highscores: \n')
    with open('hs.txt', 'r') as f:
        for line in f.readlines():
            if len(line) > 1:
                name, score = line.split(' ')
                highscore[name] = int(score)

    highscore = {k: v for k, v in sorted(highscore.items(), key=lambda item: item[1], reverse=True)}
    for key, value in highscore.items():
        print(key + ' ' + str(value))
    print('\n')

    delete_this = input('Enter a line you would like to delete from the record: ')
    with open("hs.txt", "r") as f:
        lines = f.readlines()
    with open("hs.txt", "w") as f:
        for line in lines:
            if line.strip("\n") != delete_this:
                f.write(line)
    highscore.pop(delete_this.split(' ')[0])

    clear()
    x = input("Press Enter to return to main menu...")
    clear()
    main_program()


# Handles user input
def main_program():
    print(msg)
    option = int(input('Input here: '))
    if option == 1:
        read_file()
    elif option == 2:
        write_file()
    elif option == 3:
        delete_record()
    elif option == 4:
        exit()
    else:
        clear()
        print('Invalid input!')
        x = input("Press Enter to return to main menu...")
        clear()
        main_program()


if __name__ == '__main__':
    main_program()
