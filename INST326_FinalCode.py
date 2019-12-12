import csv
import random

'''This portion of the code constructs the categories being compared.
    The categories are column names from the csv file such as wins,
    losses, sacks, etc...
    There are eleven categories being compared in the Football class'''

class Football():
    def __init__(self,team,s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11):
        self.team = team
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        self.s7 = s7
        self.s8 = s8
        self.s9 = s9
        self.s10 = s10
        self.s11 = s11

"""This portion of the code opens and reads the CSV file and reads each row for
    the two teams being compared"""

"""The next portion of the code sets the first and second teams count to 0.
        Both teams stats are compared (by category), whichever teams has a higher
        stat earns a point for that specific category. The code returns the
        team who accumulated more points"""


def findBetterTeam(a, b):
    with open('nfl.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if(row['Team'] == a):
                teama = Football(row['Team'],row['Wins'], row['Loses'], row['Passing Yards per game'], row['Rushing Yards per game'],
                              row['Points Earned per game'], row['Points Concieded per game'], row['Sacks per game'], row['Interceptions per game'],
                              row['Total Touchdowns per game'],
                              row['Safetys per game'], row['Field Goals per game'])

            if(row['Team'] == b):
                teamb = Football(row['Team'],row['Wins'], row['Loses'], row['Passing Yards per game'], row['Rushing Yards per game'],
                              row['Points Earned per game'], row['Points Concieded per game'], row['Sacks per game'], row['Interceptions per game'],
                              row['Total Touchdowns per game'],
                              row['Safetys per game'], row['Field Goals per game'])


    ta = 0
    tb = 0

    if(teama.s1 > teamb.s1):
        ta += 1
    else:
        tb += 1
    if(teama.s2 > teamb.s2):
        ta += 1
    else:
        tb += 1
    if(teama.s3 > teamb.s3):
        ta += 1
    else:
        tb += 1
    if(teama.s4 > teamb.s4):
        ta += 1
    else:
        tb += 1
    if(teama.s5 > teamb.s5):
        ta += 1
    else:
        tb += 1
    if(teama.s6 > teamb.s6):
        ta += 1
    else:
        tb += 1
    if(teama.s7 > teamb.s7):
        ta += 1
    else:
        tb += 1
    if(teama.s8 > teamb.s8):
        ta += 1
    else:
        tb += 1
    if(teama.s9 > teamb.s9):
        ta += 1
    else:
        tb += 1
    if(teama.s10 > teamb.s10):
        ta += 1
    else:
        tb += 1
    if(teama.s11 > teamb.s11):
        ta += 1
    else:
        tb += 1
    if(ta > tb):
        return("The statistical faceoff winner is the " + teama.team + " with " + str(ta) + " points out of 11" )
    else:
        return("The statistical faceoff winner is the " + teamb.team + " with " + str(tb) + " points out of 11" )


"""This portion of the code asks for user input and prints results.
NOTE: input is case sensitive"""


def main():
    print('Enter two teams to find the statistical number...  NOTE: input is case sensitive, ex: Washington Redskins')
    print('')
    g = input("First Team: ")
    z = input("Second Team: ")
    print(findBetterTeam(g,z))
    print('')
    print('The chances the underdog team will win is a random number greater than the statistical number')
    print("The random number is: ", random.randrange(1, 11))
    print('')
    print('')


if __name__ == '__main__':    main()

''' The statistical winner is assigned the numbers 1 through the statistical value output within the terminal.
    
    Example: The statistical faceoff winner is the Carolina Panthers with 7 out of 11 points.
             Thus, the the Carolina Panthers are assigned the numbers 1 through 7 for their probability.
             Thus, the opposing team, whichever that may be, will be assigned the ladder numbers up to 11. 
             In this example, they would be give numbers 8 through 11

    The randomizer output allows there to be 'real world' probability invovled within the faceoff making it
    possible for the so called underdog to win.
    
    Example(Continued): In refernece to the example noted above, if the randomizer outputs any number between 
                        1 and 7 , the Carolina Panthers will recieve the win. If the randomizer outputs any 
                        number between 8 and 11, the opposing team wins.

    Please use this template when using the program at your own leisure, enjoy!'''