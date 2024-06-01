'''Problem #1: Index Game'''
import random

def main():
    # 1. Understand how to create a list and add values
    # A list is an ordered collection of values
    
    names = ['Julie', 'Mehran', 'Simba', 'Ayesha']
    names.append('Karel')

    # 2. Understand how to loop over a list
    # this prints the list to the screen one value at a time
    for name in names:
        print(name)
    

    # 3. Understand how to look up the length of a list
    # use randint to select a valid "index" 
    max_index = len(names) -1 
    index = random.randint(0 , max_index)    

    # 4. Understand how to get a value by its index
    # get the item at the chosen index
    correct_value = names[index]
    

    # This is just like in Khansole Academy...
    # prompt the user for an answer, check if it is correct

    prompt=  input('What is in index...' + str(index))
    if prompt == correct_value:
        print('Good job')

    else:
        print('Correct answer was: ' + correct_value)

if __name__ == '__main__':
    main()




'''Problem #2: List Practice'''

def main():
    # Create a list called `fruit_list` that contains the following fruits: 
    # 'apple', 'banana', 'orange', 'grape', 'pineapple'.
    
    fruit_list = ['apple' , 'banana' , 'orange', 'grape' , 'pineapple' ]
    # Print the length of the list.
    print(len(fruit_list))


    
    # Add 'mango' at the end of the list. 
    fruit_list.append('mango')
    
    
    # Print the updated list.
    print(fruit_list)
    
if __name__ == "__main__":
    main()





'''Problem #3: Heads Up

Our next goal is to learn how to read data from files. Loading data from a file can be useful for many final projects. 
Write a program that runs a console version of the phone game Heads Up!


How the game is played remotely:
When it is your turn, close your eyes.
A word will be displayed in the HeadsUp program.
The rest of the section will try and describe it without saying the word.
You have to guess the word as quickly as possible.'''

'''Problem #3 Solution '''

import random

# Name of the file to read in!
FILE_NAME = 'cswords.txt'


def get_words_from_file():
    """
    This function has been implemented for you. It opens a file, 
    and stores all of the lines into a list of strings. 
    It returns a list of all lines in the file. 
    """
    f = open(FILE_NAME)
    lines = []
    for line in f:
        # removes whitespace characters (\n) from the start and end of the line
        line = line.strip() 
        # if the line was only whitespace characters, skip it 
        if line != "":
            lines.append(line)
    return lines

def play_game(words):

    while True:
        random_choice = random.choice(words)
        print(random_choice)
        input()


def main():
   words =  get_words_from_file()
   play_game(words)

if __name__ == '__main__':
    main()





