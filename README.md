# INST-311-Final-Project

What our program does:

For our project, we created an NFL Match Simulator.
We populated our own CSV file (as shown in GitHub) with statistics from every NFL team consisting of varibales such as wins/losses/ties, 
passing yards per game, rushing yards per game, total points earned per game, total points concieded per game, sacks per game, 
interceptions per game, total touchdowns per game, safetys per game, and total field goals per game. We opted out of using an 
already established NFL CSV file due to it having information that we just did not find neccessary for this project. 

The NFL Match Simulator program will allow a user to pick any two NFL teams of their liking, and have them faceoff in an exhibition match 
to see who would win. The simulator is based off of the statistics mentioned above. Both teams decided by the user will be compared 
statistically, variable by variable, ultimatly achieving a probability score. Each time a team beats another in variable comparrison,
they will earn 1 point to their overall probability. Once each respective probability score is established for both user decided teams,
a randomizer is implimented to decide which team will win the overall match. The randomizer allows for there to be a sense of real world
possibility, allowing for the so called 'underdog' to win from time to time. The better a team is statistically in comparrision
to another team, the more points they will earn toward their probability, ultimatly giving them more chance to win the overall match.
_________________________________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________________________________
__________________________________________________________________________________________________________________________________________
How our program should be used:

When running the program, the user will be prompt with basic instruction when the file is run.
The user will be asked to input two NFL teams that they want to go head to head in a match against one other. The user is prompt to be
case sensitive when spelling their desired teams. Once the user inputs both desired teams into the program, the program will run and 
output which team won the variable/statistical faceoff. Simultaneously, the randomizer will output, you guessed it, a random number between
1-11 (We have 11 total statistical variables in the CSV file for each NFL team). This random number will decide which team wins the overall
match. We understand that this can be hard to grasp to the untrained user, so we added somewhat of a moc run into the code using comments
which will allow a user to get the gist of the program if there is any confusion.

Simply follow the automated promts, and have fun!



