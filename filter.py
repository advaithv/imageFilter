from Graphics import *
from Myro import *
import random

def control():
    p = pickAFile()
    p = makePicture(p)
    show(p)
    return p
def colorX(dark,light):
    p = control()
    for pixel in getPixels(p):
        r, g, b = getRGB(pixel)
        total = r+g+b
        if total < 364:
            setRGB(pixel, dark)
        else:
            setRGB(pixel, light)
    return p
def colorY(dark,light,lightest):
    p = control()
    for pixel in getPixels(p):
        r, g, b = getRGB(pixel)
        total = r+g+b
        if total < 184:
            setRGB(pixel, dark)
        elif total <364:
            setRGB(pixel, light)
        else:
            setRGB(pixel, lightest)
    return p
def collectData(choice):
    color = []
    red = []
    green = []
    blue = []
    colors = open("colors.txt", "r")

    data = colors.readline()

    while( data != "" ):
        line = data.split()
        color.append(line[0])
        red.append(line[1])
        green.append(line[2])
        blue.append(line[3])
        data = colors.readline()
    colors.close()

    if choice == "2" or choice == "3":
        menu = ""
        for x in range(len(color)):
            menu = menu + str(x+1)+"\t"+str(color[x]+"\n")
        return menu
    else:
        options = []
        for x in range(len(choice)):
            option1 = ( int(red[choice[x]-1]), int(green[choice[x]-1]), int(blue[choice[x]-1]))
            options.append(option1)
        if len(choice) == 2:
            p = colorX(options[0],options[1])
        elif len(choice) == 3:
            p = colorY(options[0],options[1],options[2])
        savePicture(p,"filter.jpg")
def interface():
    condition = True
    while condition:
        choice = input("Mixing 2 or 3 Colors?")
        menu = collectData(choice)
        choices = []
        for x in range(int(choice)):
            colors = int(input(menu))
            choices.append(colors)
        picutre = collectData(choices)
        answer = input("Want To Try Other Colors\tY/N")
        if answer == 'Y':
            condition = True
        else:
            print("Transformation Complete")
            condition = False

interface()
