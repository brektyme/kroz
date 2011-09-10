#!/usr/bin/python

import sys, os, time

name = ""
health = 20
inventory = []
enter = ""
direction = ""
act = ""

def clear():
  if(os.name == "nt"):
    os.system("cls")
  else:
    os.system("clear")

def intro():
  clear()
  print('Hello traveler! What is your name?')
  name = input()
  clear()
  print(name + ', you find yourself at the mouth of a cave.')
  print('The entrance to the cave is poorly lit, but there is enough light to see.')
  print('Will you enter the cave?')
  enter = input().lower()

  while (enter != "yes" and enter != "no"):
    print('I did not understand you. Please try again')
    enter = input().lower()

  if (enter == 'yes'):
    firstroom()
  elif(enter == "no"):
    print('You\'re no fun')
    time.sleep(2)
    sys.exit()

#def dir():
#  direction = input()
#  while (direction != "north" and direction != "south" and direction != "east" and direction != "west"):
#    print('I did not understand you. Please try again')
#    direction = input()

def cavemouth():
  clear()
  print('You are back at the mouth of the cave')
  print('Re-enter?')
  enter = input().lower()

  while(enter != "yes" and enter != "no"):
    print('I did not understand you. Please try again')
    enter = input().lower()

  if(enter == "yes"):
    firstroom()
  elif(enter == "no"):
    sys.exit()

def firstroom():
  clear()
  print('You have entered the cave.')
  print('The cave seems to go on for quite a while.')
  print('There are stalagmites near your left and a small stream')
  print('that seems to be coming from a spring on your right.')
  print('You see exits north, south, and west')
  print('Which way will you go? (go direction)')
  direction = input().lower()
  while (direction != "go north" and direction != "go south" and direction != "go west"):
    print('I did not understand you. Please try again')
    direction = input().lower()
  if (direction == "go south"):
    cavemouth()
  elif (direction == "go north" and 'lamp' not in inventory):
    print('It is too dark to see, you turn back.')
    time.sleep(2)
    firstroom()
  elif (direction == "go north" and 'lamp' in inventory):
    darkroom()
  elif (direction == "go west"):
    lamproom()
  else:
    print('That is not possible')
    time.sleep(2)
    firstroom()

#def action():
#  act = input()
#  while(act != 'attack' and act != 'get' and act != 'go'):
#    print('You cannot do that!')
#    print('What would you do?')
#    act = input()

def lamproom():
  clear()
  print('This part of the cave is dark, but you can barely make out a few objects.')
  print('The smell of kerosene is thick in the air.')
  print('You see a small lamp next to your feet. It appears to have fuel left in it.')
  print('Curious, why would there be a lamp here')
  print('You see exits east and west')
  print('What will you do? (go direction/get item)')
  #action()
  act = input().lower()
  if (act == "get lamp"):
    inventory.append('lamp')
    print('You got a lamp!')
    time.sleep(2)
    lamproom()
  elif (act == "go east"):
    firstroom()
  elif (act == "go west" and 'lamp' not in inventory):
    print('It is too dark to continue that way.')
    time.sleep(2)
    lamproom()
  elif (act == "go west" and 'lamp' in inventory):
    deathroom()
  else:
    print('I didn\'t understand you.')
    time.sleep(2)
    lamproom()

def darkroom():
  clear()
  print('With the light of your lamp, you can see drawings on the wall of this part of the cave.')
  print('You see what looks to be ancient cave drawings.')
  print('Satisfied with your adventure, you return home.')
  time.sleep(2)
  sys.exit()

def deathroom():
  clear()
  print('A rotten stench fills your nose as you enter this area of the cave.')
  print('Suddenly out of nowhere something hits you on the head.')
  print('You start to black out as you see a hideous monster lower its head toward your midsection.')
  print('\n' + 'You have died.')
  time.sleep(2)
  sys.exit()
################################

intro()
