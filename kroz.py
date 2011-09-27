#!/usr/bin/env python

#kroz a terribly written "game"
import sys, os, time, csv, re

        
def clear():
  if(os.name == "nt"):
    os.system("cls")
  else:
    os.system("clear")


def open_File(filename):
    try:
        open(filename, 'r')

    except IOError:
        print("%s, %s\n" %("Unable to open", filename))
        sys.exit(1)
    return(open(filename, 'r'))

def open_csv(txt_file):
    txt_file.seek(0, 0)
    return(csv.DictReader(txt_file, delimiter=','))

def location_Line(csv_DR, txt_file, location):
    txt_file.seek(0, 0)
    line = next(csv_DR)
    while(line['Location'] != location):
        line = next(csv_DR)
    return(line)

def insert_Name(line, name):
    name_re = re.compile("\$name")
    if(name_re.match(line['Text'])):
        line['Text'] = name_re.sub(name, line['Text'])
    return(line)

def parse_DST_Choices(line, key, delimiter=', '):
    parse = None
    if(line[key] != ""):
        i = 0
        parse = line[key].split(delimiter)
        while i < len(parse):
            parse[i] = parse[i].lower()
            i += 1
    return(parse)



def get_Name(name):
    ans = ""
    ans_re = re.compile("^yes$|^no$", re.I)
    while(ans != "yes"):
        name = input("%s: " %("What is your name?"))
        clear()
        ans = input("%s %s\t%s: " %("Your name is", name,"Is this correct? (Yes\\No)")).lower()
        while(not ans_re.match(ans)):
            print("Please enter yes or no")
            ans = input("%s: %s\t%s: " %("Your name is", name, "Is this correct? (Yes\\No")).lower()
    return(name)

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
    


    


    


def main():
    name = ""
    health = 20
    inventory = []
    enter = ""
    direction = ""
    act = ""
    filename = 'kroz.csv'
    txt_file = None
    csv_DR = None
    txt_line = None

    clear()
    txt_file = open_File(filename)
    csv_DR = open_csv(txt_file)

    name = get_Name(name)
    put_Menu((location_Line(csv_DR, txt_file, 'intro')), 'intro', name)

main()
