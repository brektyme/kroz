#!/usr/bin/env python

#kroz a terribly written "game"
import sys, os, time, csv, re

#Clears the terminal screen, the os call is for cross
#platform-ness
def clear():
  if(os.name == "nt"):
    os.system("cls")
  else:
    os.system("clear")

#opens the game data file
def open_File(filename):
    try:
        open(filename, 'r')

    except IOError:
        print("%s, %s\n" %("Unable to open", filename))
        sys.exit(1)
    return(open(filename, 'r'))

#opens the game data csv object 
def open_csv(txt_file):
    txt_file.seek(0, 0)
    return(csv.DictReader(txt_file, delimiter=','))

#returns the current locations line. In the form of a hash
def location_Line(csv_DR, txt_file, location):
    txt_file.seek(0, 0)
    line = next(csv_DR)
    while(line['Location'] != location):
        line = next(csv_DR)
    return(line)

#function that uses regex to populate game with player name
def insert_Name(line, name):
    name_re = re.compile("\$name")
    if(name_re.match(line['Text'])):
        line['Text'] = name_re.sub(name, line['Text'])
    return(line)

#Parses and returns either the Choices or Destinations from the CSV in the form of a hash
def parse_DST_Choices(line, key, delimiter=', '):
    parse = None
    if(line[key] != ""):
        i = 0
        parse = line[key].split(delimiter)
        while i < len(parse):
            parse[i] = parse[i].lower()
            i += 1
    return(parse)

#function that obtains player name. Need to expand the regex to accept Y or N both upper and lower for an answer.
def get_Name(name):
    ans = ""
    ans_re = re.compile("^yes$|^no$", re.I)
    while(ans != "yes"):
        name = input("%s: " %("What is your name?"))
        clear()
        ans = input("%s %s\t%s: " %("Your name is",name+".","\nIs this correct? (Yes\\No)")).lower()
        while(not ans_re.match(ans)):
            print("Please enter yes or no")
            ans = input("%s: %s\t%s: " %("Your name is",name+".", "\nIs this correct? (Yes\\No")).lower()
    return(name)

#The function for interaction with the user. NO ACTUAL GAME PLAY SHOULD HAPPEN HERE. Only presenting the user with the current text and choices. It should return the users choice. 
def put_Menu(line, location, name):
    clear()

    line = insert_Name(line, name)
    choices = parse_DST_Choices(line, 'Choices')
    text = line['Text']
    destinations = parse_DST_Choices(line, 'Destination')
    question = line['Question']
    choice_dict = {}
    choice = None
    print(choices)


    if (len(choices) == len(destinations)):
        i = 0
        while i < len(choices):
            print(i)
            choice_dict[choices[i]] = destinations[i]
            i += 1

    print("%s\n" %(text))
    
    while(choice not in choices):
        choice = input("%s\n%s" %(question, choices))
        if(choice not in choices):
            print("%s\n" %("I didn't understand your selection."))
    print(choice)

### Main Function###

def main():
    #Player name, entered by player
    name = ""
    #Player health, starting health is 20
    health = 20
    #inventory array, initially empty
    inventory = []
    enter = ""
    direction = ""
    act = ""
    #Location of the csv file containing the game data
    filename = 'kroz.csv'
    txt_file = None
    csv_DR = None
    txt_line = None

    clear()
    txt_file = open_File(filename)
    csv_DR = open_csv(txt_file)

    name = get_Name(name)

    print(location_Line(csv_DR, txt_file, 'intro'))
    #put_Menu((location_Line(csv_DR, txt_file, 'intro')), 'intro', name)

###Main Function Entry###

main()
