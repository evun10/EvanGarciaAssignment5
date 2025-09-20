# PART 0:
def main():
    print("Evan Garcia Assignment 5")
    votersEligibility()

# PART 1:  Even or Odd
number = int(input("Enter your number: "))

if (number % 2 == 0):
    print("EVEN")
else:
    print("ODD")

# PART 2: Voting Eligibility & PART 3: How many voter's to check
def votersEligibility():
    totalVoters = []

    voters = int(input("How many voter's do you want to check? "))

    for i in range(voters):
        age = int(input("Enter your age: "))
        if (age >= 18):
            print("You are eligible to vote!")
        else:
            print("You are not eligible to vote.")
        totalVoters.append(age)
        print(totalVoters)

# PART 3: Temperatature
tempertature = int(input("Enter your temperature: "))

if (tempertature < 32):
    print("It's freezing!")
elif (tempertature >= 32 and tempertature <= 50):
    print("It's cold")
elif (tempertature >= 51 and tempertature <= 75):
    print("It's warm")
else:
    print("It's hot!")
    
# Calls main
main()