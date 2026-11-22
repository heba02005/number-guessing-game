import random

def input_number(a,b):
    while True:
        try:
            guessing = int(input('Enter the guessing number: '))
            if(guessing < a or guessing > b):
                print(f'please enter a number between {a} and {b}')
            else:
                break
        except ValueError:
            print('please enter a valid integer number')
    
    return guessing 
   

def guess_number(max_attempts):
    low = 1
    high = 100
    count = 0
    guessing = 0
    number = random.randint(low, high)
    while( guessing != number and count < max_attempts):
        guessing = input_number(low, high)
        count += 1
        if(count < max_attempts ):
            if( guessing < number):
                low = guessing+1
                print(f'your guessing number is less than the actual number , try again :')
            elif(guessing > number):
                high = guessing-1
                print(f'your guessing number is greater than the actual number , try again :')   
    else:
        if(guessing == number):
            print(f'congratulations you have guessed the number {number} in {count} attempts')   
        elif(count == max_attempts):
            print(f'you have used all your attempts the number was {number}')


def level_choice(Level):
    if Level == 'easy' :
        guess_number(10)
    elif Level == 'medium':
        guess_number(7)    
    elif Level == 'hard':
        guess_number(5) 
    else:
        print('Easy level is selected by default')
        guess_number(10)     

ask = True
print('Welcome to the number guessing game')
while (ask):
    level = input('Please select the level of difficulty (easy, medium, hard): ')
    level_choice(level.lower().strip())
    print('Do you want to play again? (yes/no)')
    var = input().lower().strip()
    if var == 'yes' or var == 'y':
        ask = True
    else:    
        ask = False