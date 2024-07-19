import random
import time
import re

dice_faces = [
    '''
     -------
    |       |
    |   ●   |
    |       |
     -------''',

    '''
     -------
    | ●     |
    |       |
    |     ● |
     -------''',

    '''
     -------
    | ●     |
    |   ●   |
    |     ● |
     -------''',

    '''
     -------
    | ●   ● |
    |       |
    | ●   ● |
     -------''',

    '''
     -------
    | ●   ● |
    |   ●   |
    | ●   ● |
     -------''',

    '''
     -------
    | ●   ● |
    | ●   ● |
    | ●   ● |
     -------'''
]

sequence = ["\\", "-", "/", "-"]

DICE = [4, 6, 8, 10, 12, 20, 100]

pattern = r'^\d{1,2}[Xx]\d+$'

def main():
    print("\n---  Welcome to shitty dice.py!  ---")
    print(dice_faces[random.randint(1,5)])
    old = 0
    while True:
        print(f"\nSides?")
        amount = 1
        try:
            choice = str(input())
            if re.match(re.compile(r'\b(help|h)\b', re.IGNORECASE), choice):
                print("Usage:")
                print("Write any int from the dice list")
                print("Or <int>x<int> for multi die rolls")
                continue
            print("---")
            if re.match(pattern, choice, re.IGNORECASE):
                choice, amount, *_ = re.split(r'[xX]', choice)
                choice = int(choice)
                amount = int(amount)
            elif choice:
                choice = int(choice)
            elif old != 0:
                print(f"Re-rolling {old}")
                choice = old
            else:
                choice = int(choice)
            if choice in DICE:
                roll = 0
                rolls = []
                for _ in range(int(amount)):
                    tmp = random.randint(1, choice)
                    rolls.append(tmp)
                    roll += tmp
                old = choice
                for i in range(10):
                    ii = i % len(sequence)    
                    print(sequence[ii], end='\r')
                    time.sleep(0.1)
                print("Your roll is:")
                print(roll)
                if (len(rolls) > 1):
                    print(f"and you rolled {rolls}")
                print("---")
            else:
                print(f"Can only roll one of {DICE}")
        except ValueError as err:
            print(f"Please write an int")



if __name__ == "__main__":
    main()

