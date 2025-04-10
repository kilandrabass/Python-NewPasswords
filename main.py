# -*- coding: utf-8 -*-
"""
Name
Group members (first names):
COSC-010
New Password Lab
"""
from typing import Concatenate
import requests
import random
import datetime


def main():
    #This first line generates a list of user information
    userInfo = [getUserID(), 
                getDateOfBirth(),
                getPassword()]
    #
    #Part 1: In a single line, initialize three variables from
    #           from UserInfo: usr, dob, pswd
    #               - Hint: use indexing
    
    #           Print each of the values out. The DOB should be
    #           in a nice format (e.g., February 29, 1989)
    #               -Hint: again, use indexing here
    usr = userInfo[0]
    dob = userInfo[1]
    pswd = userInfo[2]

    month, day, year = dob
    month_names = ['January', 'February', 'March', 'April', 'May',        'June', 'July', 'August', 'September', 'October', 'November',         'December']
    month_name = month_names[int(month)-1]
    #format month name
    dob_formatted = f"{month_name} {day}, {year}"

    print("User ID:", usr)
    print("Date of Birth:", dob_formatted)
    print("Password:", pswd)
    
    pswd = changePassword()
    print("New Password: ", pswd)
    
    wordFun()
    

def getUserID():
    """
    This function collects the userID from the
    user and returns it.
    
    Returns
    -------
    userID : TYPE str
    """
    userID = input("Enter your user ID: ")
    return userID

def getPassword():
    """
    This function collects the current password from
    the user and returns it. 
    
    Returns
    -------
    password : TYPE str
    """
    password = input("Enter your current password: ")
    return password

def getDateOfBirth():
    """
    This function collects three pieces of info from the
    user regarding their date of birth: Month, Day, Year.
    It then puts these individual items together in the 
    form of a tuple and returns that tuple.    
    
    Returns
    -------
    dateOfBirth : TYPE tuple
    """

    print("Enter your date of birth as follows:")
    month = input("Enter the month: ")
    day = input("Enter the day: ")
    year = input("Enter the year: ")
    
    dateOfBirth = (month, day, year)    

    return dateOfBirth

def changePassword():
    """
    This function refers to a dictionary on the web
    to get a list of words with which it will generate
    a random password. It then gets 3 random words. 
    Then it asks the user whether the words should be 
    capitalized. Then it asks the user what kind of 
    punctuation should be used to separate the words:
    Period (.), Dash (-), Underscore (_) or None. Then
    it concatenates it all together into one string and
    returns that string as the new password.

    Returns
    -------
    newPassword : TYPE str
    """
    newPassword = ""
    response=requests.get("http://www.mit.edu/~ecprice/wordlist.10000")
    txt = response.text #This will be a string containing all the words
    #Split the string into a list
    wordList = txt.split()
    
    # Part 2a: Generate a list of words and then use random.choice() to 
    #           initialize 3 random words.
    word1 = random.choice(wordList)
    word2 = random.choice(wordList)
    word3 = random.choice(wordList)

    capitalize = input("Do you want the words be capitalized? (yes/no): ")
    if capitalize == "yes":
        word1 = word1.capitalize()
        word2 = word2.capitalize()
        word3 = word3.capitalize()
    punct = input("What punctuation do you want to use? (Period, Dash, Underscore, None): ")
    if punct == "Period":
        newPassword = word1 + "." + word2 + "." + word3  
    elif punct == "Dash":
        newPassword = word1 + "-" + word2 + "-" + word3
    elif punct == "Underscore":
        newPassword = word1 + "_" + word2 + "_" + word3
    elif punct == "None":
        newPassword = word1 + word2 + word3  
      
    print("Time for a new password!")
    print("Your new password will be a sequence of random words")
    return newPassword

def wordFun():
    """
    This function will use the same dictionary as in the changePassword
    function. It will first print out every word in the dictionary that
    begins and ends with the same letter. It will then print out every
    palindrome in the dictionary.

    Returns
    -------
    newPassword : TYPE str
    """
    newPassword = ""
    response=requests.get("http://www.mit.edu/~ecprice/wordlist.10000")
    txt = response.text #This will be a string containing all the words
    wordList = txt.split()
    #
    # Part 3a: The txt variable (assigned above) contains all the words
    #           in the dictionary. Loop through the words and print out
    #           only the words that begin and end with the same letter
    #
    #           -First uncomment the following three lines
  # first print out every word that begins and ends with the same letter
    print("First we'll print out a lot of words:")
    for word in wordList:
        if word[0] == word[-1]:
            print(word)

    # Part 3b: Now print out only the palindromes in the dictionary 
    #
    #           -First uncomment the following 3 lines          
    print("Now we'll print out only the words that are palindromes:")
    for word in wordList:
        if word[::-1] == word:
            print(word)
    
main() #Remember: Don't accidentlally delete this line!