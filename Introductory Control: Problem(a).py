"""
Design and write a program to calculate Net Run Rate scored by the two teams use controls to validate a condition such that the team with the higher run rate will top the points table and also think for the tie-breaker condition.

Steps to Follow: 
Understand how net run rate getting calculated (Cite the reference in submission comment)
Follow the computational thinking process.
Understand inputs required to calculate various parameters (Give Appropriate Comments to the code)
Design Controls -  Compound Statements and Suites
Provide Feedback to the User (Console level Feedback)
Test (Paper Calculation)
Validate (Paper Calculation = Code  Result)
"""
team1_scored = int(input("Enter the total runs scored by Team 1: "))
team1_faced = int(input("Enter the total overs faced by Team 1: "))
team1_conceded = int(input("Enter the total runs conceded by Team 1: "))
team1_bowled= int(input("Enter the total overs bowled by Team 1: "))

team2_scored = int(input("Enter the total runs scored by Team 2: "))
team2_faced = int(input("Enter the total overs faced by Team 2: "))
team2_conceded = int(input("Enter the total runs conceded by Team 2: "))
team2_bowled= int(input("Enter the total overs bowled by Team 2: "))

team1_Nrr = (team1_scored / team1_faced) - (team1_conceded / team1_bowled)
print("Team1 Net Run Rate=",round(team1_Nrr,2))
team2_Nrr = (team2_scored / team2_faced) - (team2_conceded / team1_bowled)
print("Team2 Net Run Rate=",round(team2_Nrr,2))

if team1_Nrr > team2_Nrr:
    print("Team 1 has a higher Net Run Rate and tops the points table.")
elif team2_Nrr > team1_Nrr:
    print("Team 2 has a higher Net Run Rate and tops the points table.")
else:
    print("Both teams have the same Net run rate are tied on points")
