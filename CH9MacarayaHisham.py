'''
Python Programming 2: Chapter 9 Lab
Coder: Hisham D Macaraya
Date: 07.20.2024
Program Topic: Object-Oriented Programming, Classes, Objects, Lists and Loops
Program Name: Professor Evaluation Report
This program creates a Rating class to store and manipulate professor ratings. It then creates three instances of this class, calculates the average rating for each professor, and finds and displays the professor with the highest average rating.
'''

# CONSTANTS
TITLE = "Welcome to Professor Evaluation Report!\n"
NUM_RATING = 3
COL_TITLE = "Prof.Name   Easiness    Helpfulness   Clarity   AvgRating"
LINE = '-' * len(COL_TITLE)

class Rating:
    # Constructor method
    def __init__(self, name, easy, helpful, clear):
        self.__name = name
        self.__easy = easy
        self.__helpful = helpful
        self.__clear = clear

    # Getter methods
    def getName(self):
        # Returns the name of the professor
        return self.__name

    def getEasy(self):
        # Returns the easiness rating
        return self.__easy

    def getHelpful(self):
        # Returns the helpfulness rating
        return self.__helpful

    def getClear(self):
        # Returns the clarity rating
        return self.__clear

    # Setter methods
    def setName(self, name):
        # Sets the name of the professor
        self.__name = name

    def setEasy(self, easy):
        # Sets the easiness rating, ensuring it's between 1 and 5
        if 1 <= easy <= 5:
            self.__easy = easy

    def setHelpful(self, helpful):
        # Sets the helpfulness rating, ensuring it's between 1 and 5
        if 1 <= helpful <= 5:
            self.__helpful = helpful

    def setClear(self, clear):
        # Sets the clarity rating, ensuring it's between 1 and 5
        if 1 <= clear <= 5:
            self.__clear = clear

    # Method to calculate average rating
    def calcAvgRating(self):
        # Calculates the average of the easiness, helpfulness, and clarity ratings
        return (self.__easy + self.__helpful + self.__clear) / 3

# Function to display ratings
def displayRating(rateList):
    # Prints the column titles
    print(COL_TITLE)
    print(LINE)
    # Iterates over the list of ratings and prints each one in columns
    for rate in rateList:
        print(f"{rate.getName():<12} {rate.getEasy():<12} {rate.getHelpful():<14} {rate.getClear():<8} {rate.calcAvgRating():.2f}")
    print(LINE)

# Function to find the index of the highest average rating
def findHiIndex(rateList):
    # Initializes the highest index to 0
    highestIndex = 0
    # Initializes the highest average to the average rating of the first professor
    highestAvg = rateList[0].calcAvgRating()

    # Iterates over the rest of the list
    for i in range(1, len(rateList)):
        # If the current professor's average rating is higher than the highest found so far
        if rateList[i].calcAvgRating() > highestAvg:
            # Updates the highest average and index
            highestAvg = rateList[i].calcAvgRating()
            highestIndex = i

    # Returns the index of the professor with the highest average rating
    return highestIndex

# Function to display the professor with the highest average rating
def displayHiRating(rateList, hiIndex):
    print(f"The professor with the highest average rating is {rateList[hiIndex].getName()} with a rating of {rateList[hiIndex].calcAvgRating():.2f}")

# Main function
def main():
    # Prints the title
    print(TITLE)
    # Creates three Rating objects
    rate1 = Rating("Mary", 5, 5, 5)
    rate2 = Rating("Joe", 4, 5, 3)
    rate3 = Rating("Ria", 4, 4, 5)

    # Adds the Rating objects to a list
    rateList = [rate1, rate2, rate3]

    # Displays the ratings
    displayRating(rateList)

    # Finds the index of the highest average rating
    hiIndex = findHiIndex(rateList)

    # Displays the professor with the highest average rating
    displayHiRating(rateList, hiIndex)

# Calls the main function
main()