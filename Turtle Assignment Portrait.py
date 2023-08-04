'''
====================================
Turtle Assignment Portrait
Frank Ding
June 19 2022
Python 3.7.9
====================================
Problem Definition: Create a program of a self portrait using Turtle graphics

Input: None
Output: image of a self portrait with background

Process:
    while x<num: (cycles through the given coordinates in the parameters for the turtle to plot)
        t.goto(args[x], args[x+1])
        x+=2


====================================
List of Identifiers:
    t is equal to turtle.Turtle();
====================================
Hope you enjoy the program!

'''
import turtle;              #import turtle
from turtle import *;        #import turtle 

t = Turtle();                #INITIATE: 't' is equal to Turtle();
t.hideturtle();             #hides the turtle
t.screen.bgcolor("#2664EA");        #background colour is a nice shade of blue

turtle.setup(900, 900)      #makes the diameters of the screen 900 by 900
t.speed(0);                 #makes the speed of the turtle 0
t.up();                     #lifts turtle up


def tri(x, y, x2, y2, x3, y3, color):       #DECLARE 'tri' function with x, y, x2, y2, x3, y3, color required arguments
    '''
    Function:tri
    Description: makes a triangle with the given coordinates and fills it a certain color
    Parameters: 'x, y, x2, y2, x3, y3, color'
    Returns: None
    '''
    t.up();                 #lifts turtle
    t.goto(x, y);           #makes turtle go to those coordinates
    t.fillcolor(color);     #fills the turtle of that color
    t.begin_fill();         #begins the fill
    t.goto(x2, y2);         #goes to those coordinates
    t.goto(x3, y3);         #goes to those coordinates
    t.goto(x, y);           #goes to the first x y coordinate
    t.end_fill();           #ends the fill
def poly(color, *args):     #DECLARE 'poly' function with color, and an unlimited amount of required arguments
    '''
    Function: poly
    Description: creates and fills any polygon when given coordinates (infinite amount) and a color
    Returns: None
    List of Identifiers:
        let x represent the number index of args
        let num represent the length of the arguments in args
    '''
    x=0;                    #DECLARE and INITIATE 'x'              
    t.up();                 #lifts turtle
    num = len(args)         #DECLARE 'num'
    t.fillcolor(color)      #the fillcolor is color
    t.goto(args[x], args[x + 1])        #goes to those coordinates according to args
    t.begin_fill();         #BEGINS THE FILL
    while x<num:            #LOOP: while 'x' is less than 'num'
        t.goto(args[x], args[x+1])      #goes to those coordinates according to args
        x+=2;               #DECLARE: 'x' adds by 2
    x=0;                    #DECLARE: 'x' is equal to 0
    t.goto(args[x], args[x + 1])        #goes to those coordinates according to args
    t.end_fill();           #ends the fill
                
def armLeft():              #DECLARE 'armLeft' function
    '''
    Function: armLeft
    Description: makes the left arm 
    Returns: None
    '''
    tri(-109.0, 181.0, -81.0, 130.0, -81.0, 182.0, "#F73F1E");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-145.0, 183.0, -107.0, 160.0, -140.0, 147.0, "#FE582F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-111.0, 160.0, -140.0, 145.0, -103.0, 146.0, "#CD1A07");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-103.0, 147.0, -141.0, 147.0, -143.0, 102.0, "#FD542D");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-128.0, 117.0, -79.0, 130.0, -103.0, 150.0, "#E4351A");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-80.0, 131.0, -126.0, 118.0, -87.0, 81.0, "#DA260C");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-127.0, 117.0, -96.0, 74.0, -87.0, 82.0, "#F13B1C");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-81.0, 130.0, -88.0, 81.0, -74.0, 77.0, "#780300");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-80.0, 130.0, -76.0, 79.0, -49.0, 54.0, "#D11601");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-127.0, 118.0, -131.0, 36.0, -95.0, 75.0, "#FD4C28");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-97.0, 75.0, -80.0, 43.0, -115.0, -31.0, "#FA4524");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-97.0, 74.0, -129.0, 38.0, -115.0, -31.0, "#FA4524");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-81.0, 43.0, -60.0, -0.0, -116.0, -31.0, "#F03A19");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-82.0, 43.0, -65.0, 37.0, -59.0, -0.0, "#F03117");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-80.0, 44.0, -65.0, 37.0, -49.0, 53.0, "#D91805");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-98.0, 75.0, -83.0, 41.0, -50.0, 53.0, "#BD0901");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-128.0, 117.0, -140.0, 104.0, -130.0, 37.0, "#FA5731");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-59.0, -2.0, -115.0, -31.0, -65.0, -57.0, "#F94A27");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-60.0, -0.0, -65.0, -58.0, -38.0, -54.0, "#FC5833");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-65.0, -57.0, -86.0, -78.0, -37.0, -55.0, "#FD603C");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-114.0, -33.0, -93.0, -56.0, -65.0, -57.0, "#E33C21");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-95.0, -57.0, -121.0, -81.0, -67.0, -58.0, "#FA5630");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-115.0, -29.0, -120.0, -82.0, -93.0, -55.0, "#D32F13");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-121.0, -81.0, -66.0, -57.0, -86.0, -78.0, "#F44625");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-37.0, -54.0, -86.0, -79.0, -55.0, -97.0, "#F04829");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-39.0, -51.0, -55.0, -98.0, -17.0, -91.0, "#FF5C34");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-122.0, -82.0, -114.0, -98.0, -87.0, -77.0, "#AD220E");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-87.0, -77.0, -115.0, -98.0, -85.0, -84.0, "#C04337");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-86.0, -79.0, -84.0, -86.0, -56.0, -98.0, "#711D17");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-82.0, -86.0, -54.0, -106.0, -55.0, -98.0, "#1A0C09");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-55.0, -97.0, -53.0, -107.0, -19.0, -92.0, "#F55839");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-53.0, -107.0, -55.0, -116.0, -36.0, -98.0, "#CC513F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-34.0, -97.0, -57.0, -115.0, -42.0, -116.0, "#4A130D");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-75.0, 77.0, -99.0, 74.0, -49.0, 54.0, "#DD2E1B");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-88.0, 83.0, -98.0, 73.0, -73.0, 78.0, "#D6210F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-107.0, 182.0, -104.0, 148.0, -79.0, 130.0, "#E5280E");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-109.0, 182.0, -110.0, 159.0, -104.0, 148.0, "#F74024");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-146.0, 183.0, -110.0, 160.0, -108.0, 181.0, "#EE3215");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-107.0, 180.0, -146.0, 184.0, -78.0, 252.0, "#FC4E2A");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-78.0, 252.0, -126.0, 231.0, -146.0, 185.0, "#FD623B");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-79.0, 252.0, -108.0, 179.0, -80.0, 185.0, "#FC421F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-79.0, 252.0, -80.0, 183.0, -68.0, 268.0, "#FD5433");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-68.0, 268.0, -80.0, 183.0, -24.0, 197.0, "#FB421F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-69.0, 268.0, -26.0, 197.0, -19.0, 252.0, "#DF290E");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-36.0, 288.0, -69.0, 267.0, -18.0, 251.0, "#E74829");      #CALL: 'tri' function with three coordinates and a color parameters


def hands():                                                        #DECLARE: 'hands' function
    '''
    Function: hands
    Description: makes the hands
    Returns: None
    '''
    tri(-35.0, -98.0, -42.0, -116.0, -18.0, -92.0, "#B0644F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-18.0, -91.0, -43.0, -115.0, 2.0, -115.0, "#FEC49A");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-43.0, -117.0, 9.0, -147.0, 31.0, -117.0, "#F2AB86");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-42.0, -116.0, -37.0, -144.0, 10.0, -147.0, "#DE9F7C");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-37.0, -145.0, -22.0, -166.0, 10.0, -147.0, "#D19175");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-21.0, -165.0, 10.0, -147.0, 4.0, -169.0, "#A8745F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-18.0, -91.0, 3.0, -115.0, -6.0, -94.0, "#FBB18A");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(-6.0, -95.0, 2.0, -117.0, 6.0, -107.0, "#ECA37F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(10.0, -148.0, 4.0, -170.0, 25.0, -149.0, "#EAB9B0");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(22.0, -129.0, 10.0, -147.0, 25.0, -150.0, "#E99979");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(17.0, -157.0, 5.0, -169.0, 38.0, -166.0, "#9A624E");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(16.0, -156.0, 37.0, -167.0, 32.0, -151.0, "#F2B2A7");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(26.0, -150.0, 17.0, -157.0, 32.0, -151.0, "#9A624E");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(38.0, -166.0, 2.0, -169.0, 40.0, -189.0, "#A07E72");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(23.0, -128.0, 25.0, -151.0, 26.0, -131.0, "#996A5B");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(26.0, -131.0, 25.0, -151.0, 32.0, -151.0, "#090203");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(26.0, -132.0, 32.0, -129.0, 32.0, -151.0, "#28130F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(24.0, -127.0, 25.0, -134.0, 32.0, -129.0, "#8D5037");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(32.0, -129.0, 32.0, -152.0, 37.0, -167.0, "#F2BFA3");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(24.0, -127.0, 32.0, -129.0, 32.0, -116.0, "#D28662");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(32.0, -116.0, 32.0, -132.0, 38.0, -162.0, "#915741");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(32.0, -117.0, 37.0, -166.0, 46.0, -85.0, "#F7BB97");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(47.0, -85.0, 38.0, -165.0, 48.0, -135.0, "#E2A17F");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(48.0, -135.0, 36.0, -165.0, 56.0, -140.0, "#714633");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(56.0, -140.0, 47.0, -135.0, 56.0, -122.0, "#996B52");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(57.0, -122.0, 53.0, -98.0, 48.0, -135.0, "#A3735B");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(48.0, -135.0, 48.0, -86.0, 53.0, -96.0, "#CC9171");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(47.0, -85.0, 31.0, -116.0, 19.0, -94.0, "#FDC89C");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(28.0, -79.0, 19.0, -96.0, 48.0, -85.0, "#F0B796");      #CALL: 'tri' function with three coordinates and a color parameters
    tri(20.0, -93.0, 2.0, -116.0, 32.0, -116.0, "#ECBB95");


def logo():             #DECLARE: 'logo' function
    '''
    Function: logo
    Description: makes the hoodie logo
    Returns: None
    '''
    tri(-80.0, 183.0, -80.0, 130.0, -71.0, 168.0, "#726151");   #CALL: 'tri' function with three coordinates and a color parameters
    tri(-71.0, 167.0, -78.0, 155.0, -65.0, 153.0, "#61554C");   #===!!FYI I'm not going to comment this comment for all of the 'tri' calls at this point because it just repeats!!===
    tri(-65.0, 153.0, -80.0, 130.0, -78.0, 156.0, "#82634A");
    tri(-65.0, 151.0, -80.0, 131.0, -50.0, 138.0, "#735746");
    tri(-65.0, 152.0, -50.0, 137.0, -46.0, 156.0, "#5B514B");
    tri(-46.0, 156.0, -49.0, 138.0, -29.0, 167.0, "#695D56");
    tri(-29.0, 167.0, -49.0, 137.0, -24.0, 144.0, "#826D59");
    tri(-31.0, 166.0, -25.0, 143.0, -3.0, 156.0, "#696041");
    tri(-3.0, 156.0, -26.0, 143.0, 4.0, 133.0, "#574231");
    tri(5.0, 134.0, -3.0, 157.0, 32.0, 134.0, "#94563B");
    tri(32.0, 133.0, 28.0, 159.0, -3.0, 156.0, "#786C52");
    tri(-80.0, 184.0, -71.0, 167.0, -59.0, 181.0, "#7D7662");
    tri(-59.0, 181.0, -80.0, 184.0, -24.0, 197.0, "#977251");
    tri(-24.0, 197.0, -61.0, 179.0, -47.0, 178.0, "#897554");
    tri(-47.0, 178.0, -26.0, 197.0, -31.0, 180.0, "#897554");
    tri(-31.0, 180.0, -25.0, 197.0, -28.0, 167.0, "#6D6744");
    tri(-28.0, 169.0, -25.0, 196.0, -18.0, 168.0, "#5E5431");
    tri(-18.0, 168.0, -25.0, 197.0, 3.0, 163.0, "#5C4225");
    tri(3.0, 163.0, -25.0, 196.0, -9.0, 188.0, "#8F4227");
    tri(-9.0, 188.0, 1.0, 163.0, 22.0, 169.0, "#5E554A");
    tri(22.0, 168.0, -10.0, 187.0, 28.0, 187.0, "#725945");
    tri(-72.0, 168.0, -53.0, 169.0, -65.0, 153.0, "#C9C6B4");
    tri(-58.0, 168.0, -65.0, 152.0, -46.0, 156.0, "#9D9786");
    tri(-46.0, 156.0, -56.0, 168.0, -46.0, 177.0, "#DCD8CB");
    tri(-46.0, 177.0, -59.0, 178.0, -57.0, 168.0, "#EBE6D4");
    tri(-55.0, 168.0, -70.0, 166.0, -58.0, 181.0, "#E2DFCE");
    tri(-46.0, 176.0, -47.0, 157.0, -30.0, 181.0, "#969078");
    tri(-30.0, 181.0, -47.0, 156.0, -27.0, 168.0, "#CCC8B7");
    tri(-27.0, 168.0, -4.0, 155.0, -30.0, 165.0, "#D3C9B6");
    tri(-29.0, 169.0, -5.0, 155.0, 4.0, 163.0, "#BF927F");
    tri(-29.0, 168.0, 5.0, 163.0, -19.0, 169.0, "#C1B7A5");
    tri(2.0, 163.0, -4.0, 156.0, 23.0, 168.0, "#BCB1A1");
    tri(23.0, 168.0, -3.0, 156.0, 29.0, 158.0, "#D7CEBE");
    tri(28.0, 187.0, 21.0, 170.0, 35.0, 156.0, "#BC4B3B");
    tri(35.0, 156.0, 23.0, 167.0, 28.0, 157.0, "#B15F54");
    tri(28.0, 157.0, 32.0, 134.0, 35.0, 156.0, "#B24430");
    tri(26.0, 188.0, 40.0, 161.0, 79.0, 175.0, "#4C3C32");
    tri(79.0, 175.0, 40.0, 161.0, 73.0, 146.0, "#6A5B42");
    tri(73.0, 146.0, 42.0, 163.0, 34.0, 156.0, "#ABA38E");
    tri(35.0, 156.0, 52.0, 145.0, 71.0, 146.0, "#D1C8B8");
    tri(72.0, 147.0, 50.0, 146.0, 54.0, 125.0, "#77634E");
    tri(54.0, 127.0, 32.0, 132.0, 51.0, 146.0, "#674B2B");
    tri(51.0, 146.0, 34.0, 156.0, 32.0, 133.0, "#4F4432");
    tri(25.0, 187.0, 45.0, 163.0, 33.0, 155.0, "#4C3C32");
    tri(52.0, 128.0, 74.0, 123.0, 73.0, 146.0, "#9F7250");


def bodyTop():             #DECLARE: 'bodyTop' function
    '''
    Function: bodyTop
    Description: makes the top of the body
    Returns: None
    '''
    tri(-18.0, 253.0, -26.0, 194.0, -9.0, 187.0, "#D12808"); #CALL: 'tri' function with three coordinates and a color parameters
    tri(-9.0, 187.0, -19.0, 253.0, -6.0, 229.0, "#B01304");  #===!!FYI I'm not going to comment this comment for all of the 'tri' calls at this point because it just repeats!!===
    tri(-6.0, 228.0, -19.0, 253.0, 7.0, 243.0, "#DD2C0B");
    tri(7.0, 243.0, -7.0, 227.0, 30.0, 247.0, "#BA2814");
    tri(30.0, 247.0, -6.0, 227.0, 69.0, 230.0, "#8F1007");
    tri(69.0, 230.0, 27.0, 246.0, 84.0, 256.0, "#B31C10");
    tri(84.0, 256.0, 65.0, 259.0, 29.0, 247.0, "#E26C63");
    tri(-6.0, 228.0, 28.0, 183.0, 70.0, 231.0, "#D5280C");
    tri(70.0, 231.0, 28.0, 186.0, 78.0, 174.0, "#ED3616");
    tri(79.0, 175.0, 68.0, 230.0, 97.0, 202.0, "#FC3C19");
    tri(97.0, 202.0, 68.0, 230.0, 99.0, 240.0, "#FE4B28");
    tri(99.0, 240.0, 84.0, 256.0, 69.0, 231.0, "#C62A1F");
    tri(-6.0, 230.0, -12.0, 188.0, 25.0, 188.0, "#DD2C0B");
    tri(98.0, 240.0, 96.0, 199.0, 111.0, 231.0, "#FA5639");
    tri(77.0, 174.0, 82.0, 135.0, 96.0, 203.0, "#F13616");
    tri(96.0, 203.0, 81.0, 136.0, 86.0, 132.0, "#9D110B");
    tri(96.0, 204.0, 90.0, 161.0, 110.0, 230.0, "#A40D08");
    tri(90.0, 162.0, 120.0, 203.0, 109.0, 229.0, "#F54224");
    tri(109.0, 229.0, 118.0, 203.0, 143.0, 191.0, "#F04B33");
    tri(143.0, 191.0, 110.0, 231.0, 126.0, 220.0, "#E37565");
    tri(119.0, 202.0, 86.0, 132.0, 144.0, 191.0, "#E63C25");
    tri(120.0, 204.0, 91.0, 164.0, 85.0, 131.0, "#C41E0C");
    tri(144.0, 191.0, 84.0, 131.0, 126.0, 118.0, "#F04022");
    tri(126.0, 118.0, 151.0, 150.0, 143.0, 191.0, "#FD4B2C");
    tri(150.0, 150.0, 124.0, 119.0, 154.0, 96.0, "#FB4F31");
    tri(87.0, 133.0, 78.0, 112.0, 125.0, 118.0, "#CE1B06");
    tri(125.0, 118.0, 69.0, 96.0, 78.0, 112.0, "#F33B1F");
    tri(69.0, 97.0, 107.0, 84.0, 125.0, 119.0, "#CD1908");
    tri(125.0, 119.0, 154.0, 97.0, 106.0, 84.0, "#BD1805");
    tri(81.0, 137.0, 89.0, 132.0, 69.0, 96.0, "#9B0803");
    tri(81.0, 137.0, 73.0, 125.0, 70.0, 97.0, "#D52108");
    tri(72.0, 145.0, 75.0, 124.0, 81.0, 138.0, "#F23511");
    tri(82.0, 137.0, 72.0, 146.0, 77.0, 176.0, "#FA431F");
    tri(54.0, 128.0, 50.0, 81.0, 73.0, 123.0, "#F1310F");
    tri(74.0, 126.0, 50.0, 80.0, 70.0, 98.0, "#D52108");
    tri(70.0, 98.0, 56.0, 55.0, 51.0, 83.0, "#BA0E03");
    tri(51.0, 83.0, 30.0, 136.0, 56.0, 127.0, "#F1310F");
    tri(68.0, 96.0, 56.0, 57.0, 73.0, 82.0, "#F83D1F");
    tri(33.0, 135.0, 18.0, 84.0, 52.0, 83.0, "#E82F0E");
    tri(52.0, 85.0, 57.0, 56.0, 19.0, 84.0, "#E13417");
    tri(20.0, 84.0, -51.0, 138.0, 4.0, 132.0, "#EF3918");
    tri(0.0, 133.0, 19.0, 83.0, 34.0, 136.0, "#E82D0C");
    tri(-25.0, 146.0, -51.0, 139.0, 5.0, 132.0, "#E24425");
    tri(18.0, 85.0, 57.0, 58.0, 47.0, 5.0, "#D82511");
    tri(47.0, 6.0, 60.0, 28.0, 56.0, 59.0, "#CA1A0C");
    tri(56.0, 59.0, 72.0, 82.0, 60.0, 26.0, "#CF1E0A");
    tri(64.0, 44.0, 76.0, 66.0, 73.0, 81.0, "#7F0000");
    tri(59.0, 28.0, 47.0, 5.0, 60.0, 18.0, "#B70E03");
    tri(61.0, 19.0, 59.0, 28.0, 79.0, 18.0, "#8F0C04");
    tri(19.0, 85.0, -29.0, 2.0, 48.0, 6.0, "#F74525");
    tri(19.0, 84.0, -28.0, 4.0, -51.0, 53.0, "#FA4625");
    tri(-51.0, 53.0, 20.0, 84.0, -50.0, 139.0, "#FA421E");
    tri(-50.0, 139.0, -48.0, 53.0, -80.0, 132.0, "#F2310D");
    tri(-50.0, 57.0, -66.0, 39.0, -28.0, 3.0, "#F53E22");
    tri(-28.0, 4.0, -60.0, 1.0, -65.0, 38.0, "#D41F0A");
    tri(-60.0, -0.0, 13.0, -16.0, -29.0, 3.0, "#F53F22");
    tri(-29.0, 3.0, 47.0, 7.0, 13.0, -17.0, "#FD502D");
    tri(13.0, -17.0, 40.0, -14.0, 47.0, 6.0, "#F14024");
    tri(47.0, 6.0, 41.0, -38.0, 40.0, -13.0, "#F44828");
    tri(12.0, -15.0, 41.0, -36.0, 42.0, -13.0, "#B31307");
    tri(11.0, -16.0, 35.0, -60.0, 41.0, -34.0, "#E0331D");
    tri(13.0, -14.0, -7.0, -66.0, 35.0, -60.0, "#C51906");
    tri(15.0, -16.0, -60.0, -0.0, -9.0, -66.0, "#E83014");
    tri(-9.0, -66.0, -37.0, -54.0, -59.0, -0.0, "#F34727");
    tri(-36.0, -55.0, 4.0, -78.0, -9.0, -65.0, "#E9442D");
    tri(-9.0, -65.0, 35.0, -60.0, 3.0, -77.0, "#F24A2F");
    tri(3.0, -78.0, 29.0, -79.0, 35.0, -60.0, "#DF3A27");
    tri(-37.0, -55.0, 4.0, -79.0, -7.0, -83.0, "#BB2012");
    tri(-7.0, -81.0, -18.0, -92.0, -39.0, -52.0, "#F45A3A");
    tri(-18.0, -92.0, -7.0, -81.0, 4.0, -79.0, "#7D1812");
    tri(4.0, -78.0, -20.0, -92.0, -6.0, -94.0, "#D04835");
    tri(-6.0, -94.0, 3.0, -78.0, 6.0, -106.0, "#733C37");
    tri(6.0, -106.0, 20.0, -95.0, 2.0, -78.0, "#483939");
    tri(2.0, -78.0, 29.0, -79.0, 19.0, -94.0, "#683535");
    tri(18.0, -94.0, 3.0, -115.0, 6.0, -107.0, "#634E47");


def armRight():         #DECLARE 'armRight' function
    '''
    Function: armRight
    Description: makes the right arm
    Returns: None
    '''  
    tri(69.0, 97.0, 70.0, 80.0, 107.0, 84.0, "#F63C1B"); #CALL: 'tri' function with three coordinates and a color parameters
    tri(107.0, 84.0, 75.0, 64.0, 127.0, 66.0, "#B60C01");  #===!!FYI I'm not going to comment this comment for all of the 'tri' calls at this point because it just repeats!!===
    tri(127.0, 66.0, 106.0, 84.0, 153.0, 100.0, "#DC1E04");
    tri(154.0, 99.0, 143.0, 33.0, 125.0, 67.0, "#F44022");
    tri(124.0, 68.0, 95.0, 45.0, 144.0, 36.0, "#9C2616");
    tri(124.0, 66.0, 98.0, 44.0, 64.0, 41.0, "#981203");
    tri(63.0, 41.0, 124.0, 65.0, 75.0, 65.0, "#CA220A");
    tri(65.0, 45.0, 59.0, 27.0, 97.0, 45.0, "#D10F04");
    tri(97.0, 45.0, 61.0, 29.0, 113.0, 27.0, "#DA1601");
    tri(113.0, 27.0, 99.0, 44.0, 134.0, 14.0, "#E62C0D");
    tri(134.0, 15.0, 97.0, 45.0, 144.0, 21.0, "#E64932");
    tri(144.0, 22.0, 98.0, 43.0, 144.0, 37.0, "#AB210E");
    tri(57.0, 29.0, 79.0, 17.0, 112.0, 27.0, "#F9421F");
    tri(112.0, 27.0, 78.0, 18.0, 81.0, -55.0, "#F23C1A");
    tri(80.0, -55.0, 41.0, -34.0, 80.0, 18.0, "#FA4521");
    tri(80.0, 18.0, 61.0, 19.0, 49.0, 5.0, "#F94520");
    tri(48.0, 5.0, 41.0, -36.0, 80.0, 18.0, "#FC4922");
    tri(37.0, -29.0, 46.0, -86.0, 83.0, -58.0, "#FA4521");
    tri(112.0, 29.0, 80.0, -57.0, 123.0, -29.0, "#D0371F");
    tri(123.0, -29.0, 112.0, 26.0, 135.0, 16.0, "#A02816");
    tri(135.0, 16.0, 122.0, -29.0, 132.0, -15.0, "#630D09");
    tri(132.0, -15.0, 122.0, -27.0, 142.0, -13.0, "#610A05");
    tri(143.0, -12.0, 143.0, -56.0, 122.0, -26.0, "#7C1911");
    tri(122.0, -25.0, 118.0, -54.0, 143.0, -56.0, "#C7321D");
    tri(143.0, -56.0, 122.0, -75.0, 120.0, -53.0, "#D13922");
    tri(120.0, -53.0, 100.0, -66.0, 123.0, -76.0, "#8C1A0B");
    tri(100.0, -67.0, 98.0, -51.0, 119.0, -52.0, "#580804");
    tri(121.0, -53.0, 122.0, -28.0, 97.0, -50.0, "#540502");
    tri(99.0, -50.0, 81.0, -56.0, 124.0, -28.0, "#942F24");
    tri(71.0, 81.0, 74.0, 63.0, 107.0, 84.0, "#B60C01");
    tri(80.0, -58.0, 98.0, -48.0, 101.0, -67.0, "#AC3423");
    tri(101.0, -65.0, 82.0, -85.0, 82.0, -55.0, "#7A1B10");
    tri(82.0, -55.0, 47.0, -86.0, 81.0, -85.0, "#E6371A");
    tri(81.0, -85.0, 72.0, -98.0, 47.0, -85.0, "#EE4B2E");
    tri(42.0, -33.0, 49.0, -87.0, 28.0, -80.0, "#F65B39");
    tri(47.0, -83.0, 72.0, -98.0, 52.0, -98.0, "#56251A");
    tri(52.0, -98.0, 57.0, -125.0, 73.0, -98.0, "#2B1411");


def hoodie():           #DECLARE 'hoodie' function
    '''
    Function: hoodie
    Description: makes the hoodie hood
    Returns: None
    '''     
    tri(44.0, 260.0, 28.0, 246.0, 68.0, 258.0, "#AC9592");    #CALL: 'tri' function with three coordinates and a color parameters
    tri(68.0, 258.0, 43.0, 259.0, 43.0, 279.0, "#625554");    #===!!FYI I'm not going to comment this comment for all of the 'tri' calls at this point because it just repeats!!===
    tri(44.0, 278.0, 67.0, 258.0, 50.0, 278.0, "#8A8586");
    tri(50.0, 278.0, 85.0, 256.0, 66.0, 258.0, "#B7BAC7");
    tri(45.0, 279.0, 43.0, 260.0, 31.0, 271.0, "#5B4842");
    tri(32.0, 272.0, 31.0, 285.0, 45.0, 280.0, "#8F8B89");

    t.fillcolor("#4F3A37");     #fills color to that
    t.goto(31.0, 286.0);        #goes to those coordinates    
    t.begin_fill();             #begins the fill
    t.goto(26.0, 280.0);
    t.goto(29.0, 272.0);
    t.goto(28.0, 264.0);
    t.goto(26.0, 263.0);
    t.goto(29.0, 259.0);
    t.goto(39.0, 255.0);
    t.goto(43.0, 258.0);
    t.goto(44.0, 263.0);
    t.goto(45.0, 280.0);
    t.goto(32.0, 285.0);
    t.goto(27.0, 283.0);
    t.end_fill();               #ends the fill
    

def legLeft():                                              #DECLARE 'legLeft' function
    '''
    Function: legLeft
    Description: makes the left leg
    Returns: None
    '''  
    tri(-81.0, -82.0, -55.0, -96.0, -52.0, -106.0, "#1A0C09");    #CALL: 'tri' function with three coordinates and a color parameters
    tri(-52.0, -106.0, -56.0, -116.0, -84.0, -85.0, "#3F3030");    #===!!FYI I'm not going to comment this comment for all of the 'tri' calls at this point because it just repeats!!===
    tri(-84.0, -85.0, -114.0, -96.0, -57.0, -114.0, "#574848");
    tri(-56.0, -114.0, -78.0, -194.0, -115.0, -97.0, "#584E50");
    tri(-114.0, -98.0, -139.0, -194.0, -83.0, -194.0, "#625A5C");
    tri(-55.0, -113.0, -79.0, -192.0, -37.0, -145.0, "#463E3E");
    tri(-37.0, -145.0, -57.0, -113.0, -42.0, -114.0, "#362421");
    tri(-38.0, -143.0, -78.0, -194.0, -21.0, -165.0, "#3C3536");
    tri(-21.0, -165.0, -45.0, -193.0, -77.0, -194.0, "#141414");
    tri(-77.0, -192.0, -68.0, -210.0, -46.0, -194.0, "#484344");
    tri(-45.0, -190.0, -68.0, -209.0, -44.0, -213.0, "#070707");
    tri(-44.0, -213.0, -49.0, -190.0, -27.0, -181.0, "#131313");
    tri(-28.0, -180.0, -46.0, -213.0, -24.0, -209.0, "#514446");
    tri(-24.0, -209.0, -18.0, -231.0, -44.0, -213.0, "#4B3837");
    tri(-44.0, -213.0, -65.0, -234.0, -18.0, -232.0, "#2D0D0F");
    tri(-44.0, -212.0, -66.0, -234.0, -69.0, -208.0, "#423F40");

    tri(-67.0, -209.0, -126.0, -233.0, -64.0, -233.0, "#484446");
    tri(-64.0, -233.0, -142.0, -271.0, -124.0, -232.0, "#292727");
    tri(-126.0, -230.0, -155.0, -257.0, -143.0, -274.0, "#342F2F");
    tri(-153.0, -256.0, -153.0, -242.0, -124.0, -231.0, "#585151");
    tri(-124.0, -231.0, -141.0, -216.0, -151.0, -244.0, "#5D5654");
    tri(-140.0, -220.0, -124.0, -230.0, -137.0, -192.0, "#635D5D");
    tri(-137.0, -192.0, -77.0, -193.0, -125.0, -231.0, "#5E5759");

    tri(-65.0, -229.0, -144.0, -273.0, -78.0, -313.0, "#1D1A18");
    tri(-78.0, -312.0, -66.0, -230.0, -36.0, -307.0, "#0C0B0A");
    tri(-36.0, -307.0, -18.0, -231.0, -66.0, -232.0, "#060505");
    tri(-19.0, -230.0, -37.0, -309.0, 11.0, -282.0, "#050404");
    tri(11.0, -282.0, -21.0, -337.0, -36.0, -309.0, "#130C0B");
    tri(-36.0, -307.0, -72.0, -322.0, -79.0, -313.0, "#1A1814");
    tri(-78.0, -188.0, -130.0, -235.0, -67.0, -210.0, "#565051");

    tri(9.0, -282.0, -38.0, -308.0, -13.0, -366.0, "#0A0807");
    tri(-13.0, -365.0, 9.0, -279.0, 55.0, -346.0, "#181513");
    tri(55.0, -346.0, 6.0, -281.0, 32.0, -268.0, "#191513");
    tri(32.0, -268.0, 75.0, -320.0, 53.0, -347.0, "#1F1A17");


def legRight():         #DECLARE 'legRight' function
    '''
    Function: legRight
    Description: makes the right leg
    Returns: None
    '''  
    tri(123.0, -75.0, 80.0, -83.0, 130.0, -92.0, "#443C3E");      #CALL: 'tri' function with three coordinates and a color parameters  
    tri(131.0, -92.0, 58.0, -123.0, 81.0, -82.0, "#4C4143");    #===!!FYI I'm not going to comment this comment for all of the 'tri' calls at this point because it just repeats!!===

    tri(56.0, -118.0, 81.0, -167.0, 131.0, -89.0, "#574E50");
    tri(131.0, -89.0, 151.0, -183.0, 80.0, -167.0, "#524B4D");
    tri(127.0, -89.0, 151.0, -134.0, 151.0, -182.0, "#454447");
    tri(129.0, -90.0, 150.0, -132.0, 140.0, -93.0, "#231F1F");
    tri(56.0, -117.0, 57.0, -142.0, 82.0, -166.0, "#4F4949");
    tri(82.0, -166.0, 57.0, -139.0, 56.0, -165.0, "#4D4646");
    tri(56.0, -165.0, 38.0, -165.0, 58.0, -140.0, "#32241F");
    tri(36.0, -167.0, 61.0, -185.0, 56.0, -165.0, "#170F0D");
    tri(56.0, -165.0, 82.0, -167.0, 66.0, -169.0, "#524847");
    tri(56.0, -163.0, 78.0, -205.0, 59.0, -184.0, "#4F494A");
    tri(60.0, -184.0, 36.0, -166.0, 53.0, -193.0, "#393535");
    tri(54.0, -191.0, 78.0, -203.0, 58.0, -184.0, "#5B5556");
    tri(54.0, -191.0, 79.0, -230.0, 79.0, -202.0, "#3C3738");
    tri(79.0, -202.0, 79.0, -230.0, 153.0, -234.0, "#201D1D");
    tri(153.0, -234.0, 78.0, -203.0, 154.0, -207.0, "#2C292A");
    tri(154.0, -207.0, 151.0, -181.0, 78.0, -203.0, "#444041");
    tri(78.0, -203.0, 81.0, -166.0, 150.0, -183.0, "#565052");
    tri(81.0, -166.0, 65.0, -169.0, 79.0, -205.0, "#5F585A");
    tri(55.0, -161.0, 67.0, -169.0, 80.0, -203.0, "#4F494A");
    tri(54.0, -192.0, 78.0, -231.0, 54.0, -206.0, "#474243");
    tri(54.0, -206.0, 47.0, -206.0, 53.0, -193.0, "#2F2929");
    tri(52.0, -206.0, 54.0, -228.0, 78.0, -230.0, "#534E4D");
    tri(78.0, -231.0, 41.0, -247.0, 54.0, -227.0, "#282422");
    tri(41.0, -245.0, 31.0, -268.0, 78.0, -230.0, "#181513");
    tri(78.0, -230.0, 153.0, -234.0, 80.0, -204.0, "#201D1D");
    tri(79.0, -203.0, 154.0, -205.0, 154.0, -236.0, "#2C292A");
    tri(78.0, -230.0, 31.0, -266.0, 100.0, -306.0, "#1F1B19");
    tri(78.0, -230.0, 153.0, -234.0, 100.0, -305.0, "#201B18");
    tri(100.0, -305.0, 138.0, -274.0, 153.0, -235.0, "#1F1C19");
    tri(102.0, -302.0, 71.0, -320.0, 30.0, -266.0, "#1F1A17");


def neckShadow():           #DECLARE 'neckShadow' function
    '''
    Function: neckShadow
    Description: makes the shadow of the neck
    Returns: None   
    '''
    t.fillcolor("#8E4D3B"); #fills color to that
    t.goto(-18.0, 276.0);
    t.begin_fill();         #begins filling
    t.goto(-15.0, 274.0);   #goes to those coordinates
    t.goto(-12.0, 270.0);
    t.goto(-6.0, 265.0);
    t.goto(-5.0, 259.0);
    t.goto(-3.0, 254.0);
    t.goto(2.0, 254.0);
    t.goto(4.0, 251.0);
    t.goto(2.0, 249.0);
    t.goto(0.0, 247.0);
    t.goto(0.0, 247.0);
    t.goto(0.0, 242.0);
    t.goto(0.0, 238.0);
    t.goto(44.0, 249.0);
    t.goto(31.0, 257.0);
    t.goto(26.0, 258.0);
    t.goto(23.0, 259.0);
    t.goto(22.0, 261.0);
    t.goto(22.0, 263.0);
    t.goto(21.0, 264.0);
    t.goto(21.0, 267.0);
    t.goto(23.0, 270.0);
    t.goto(23.0, 273.0);
    t.goto(23.0, 273.0);
    t.goto(22.0, 276.0);
    t.goto(22.0, 276.0);
    t.goto(22.0, 279.0);
    t.goto(21.0, 283.0);
    t.goto(19.0, 282.0);
    t.goto(19.0, 281.0);
    t.goto(16.0, 280.0);
    t.goto(13.0, 279.0);
    t.goto(11.0, 278.0);
    t.goto(7.0, 276.0);
    t.goto(4.0, 276.0);
    t.goto(1.0, 276.0);
    t.goto(-3.0, 276.0);
    t.goto(-7.0, 276.0);
    t.goto(-9.0, 276.0);
    t.goto(-13.0, 277.0);
    t.end_fill();           #ends the fill


def neck():                 #DEFINE 'neck' function
    '''
    Function: neck
    Description: makes the neck
    Returns: None
    '''  
    t.fillcolor("#DF8C5A")  #fills the color to that color
    t.goto(26.0, 286.0);    #goes to that coordinate
    t.begin_fill();         #begins the fill
    t.goto(29.0, 261.0);
    t.goto(41.0, 257.0);
    t.goto(45.0, 249.0);
    t.goto(28.0, 242.0);
    t.goto(-25.0, 238.0);
    t.goto(-48.0, 274.0);
    t.goto(-36.0, 287.0);
    t.goto(-36.0, 296.0);
    t.goto(-28.0, 285.0);
    t.goto(-23.0, 282.0);
    t.goto(-23.0, 282.0);
    t.goto(-19.0, 279.0);
    t.goto(-16.0, 279.0);
    t.goto(-13.0, 277.0);
    t.goto(-10.0, 277.0);
    t.goto(-5.0, 276.0);
    t.goto(-1.0, 276.0);
    t.goto(2.0, 276.0);
    t.goto(5.0, 276.0);
    t.goto(10.0, 278.0);
    t.goto(15.0, 279.0);
    t.goto(20.0, 282.0);
    t.goto(25.0, 285.0);
    t.goto(26.0, 288.0);
    t.end_fill();           #ends the fill

    t.fillcolor("#6F3726"); #sets the fill color to that color
    t.goto(22.0, 283.0);
    t.begin_fill();         #begins the fill
    t.goto(19.0, 257.0);
    t.goto(37.0, 248.0);
    t.goto(47.0, 256.0);
    t.goto(42.0, 256.0);
    t.goto(39.0, 257.0);
    t.goto(34.0, 258.0);
    t.goto(28.0, 260.0);
    t.goto(27.0, 262.0);
    t.goto(29.0, 267.0);
    t.goto(28.0, 272.0);
    t.goto(28.0, 275.0);
    t.goto(27.0, 278.0);
    t.goto(27.0, 280.0);
    t.goto(27.0, 284.0);
    t.goto(27.0, 286.0);
    t.goto(25.0, 286.0);
    t.goto(25.0, 285.0);
    t.goto(24.0, 284.0);
    t.goto(22.0, 283.0);
    t.end_fill();           #ends the fill

def face():     #DEFINE 'face' function
    '''
    Function: face
    Description: makes a face shape
    Returns: None
    '''  
    t.fillcolor("#DE8F70")  #sets fill color to #DE8F70
    t.goto(-35.0, 295.0);   #goes to that coordinate
    t.begin_fill();         #begins the fill
    t.goto(-34.0, 293.0);
    t.goto(-32.0, 292.0);
    t.goto(-32.0, 292.0);
    t.goto(-30.0, 289.0);
    t.goto(-28.0, 285.0);
    t.goto(-25.0, 283.0);
    t.goto(-22.0, 281.0);
    t.goto(-19.0, 279.0);
    t.goto(-17.0, 278.0);
    t.goto(-12.0, 277.0);
    t.goto(-5.0, 277.0);
    t.goto(1.0, 277.0);
    t.goto(1.0, 277.0);
    t.goto(5.0, 277.0);
    t.goto(8.0, 276.0);
    t.goto(11.0, 278.0);
    t.goto(14.0, 280.0);
    t.goto(18.0, 282.0);
    t.goto(24.0, 284.0);
    t.goto(26.0, 287.0);
    t.goto(29.0, 290.0);
    t.goto(31.0, 292.0);
    t.goto(34.0, 296.0);
    t.goto(36.0, 302.0);
    t.goto(38.0, 305.0);
    t.goto(39.0, 309.0);
    t.goto(41.0, 313.0);
    t.goto(41.0, 320.0);
    t.goto(40.0, 328.0);
    t.goto(42.0, 345.0);
    t.goto(42.0, 350.0);
    t.goto(42.0, 355.0);
    t.goto(42.0, 361.0);
    t.goto(41.0, 368.0);
    t.goto(38.0, 374.0);
    t.goto(38.0, 379.0);
    t.goto(35.0, 382.0);
    t.goto(30.0, 386.0);
    t.goto(27.0, 389.0);
    t.goto(26.0, 391.0);
    t.goto(22.0, 393.0);
    t.goto(20.0, 395.0);
    t.goto(16.0, 397.0);
    t.goto(14.0, 399.0);
    t.goto(12.0, 399.0);
    t.goto(8.0, 400.0);
    t.goto(6.0, 400.0);
    t.goto(-1.0, 402.0);
    t.goto(-7.0, 399.0);
    t.goto(-12.0, 399.0);
    t.goto(-15.0, 401.0);
    t.goto(-19.0, 402.0);
    t.goto(-23.0, 399.0);
    t.goto(-26.0, 397.0);
    t.goto(-28.0, 393.0);
    t.goto(-29.0, 389.0);
    t.goto(-31.0, 386.0);
    t.goto(-32.0, 382.0);
    t.goto(-34.0, 382.0);
    t.goto(-38.0, 380.0);
    t.goto(-42.0, 377.0);
    t.goto(-45.0, 375.0);
    t.goto(-48.0, 369.0);
    t.goto(-49.0, 365.0);
    t.goto(-49.0, 358.0);
    t.goto(-49.0, 355.0);
    t.goto(-48.0, 350.0);
    t.goto(-48.0, 343.0);
    t.goto(-47.0, 335.0);
    t.goto(-46.0, 330.0);
    t.goto(-44.0, 326.0);
    t.goto(-43.0, 320.0);
    t.goto(-43.0, 311.0);
    t.goto(-41.0, 310.0);
    t.goto(-39.0, 305.0);
    t.goto(-38.0, 304.0);
    t.goto(-36.0, 298.0);
    t.goto(-36.0, 296.0);
    t.end_fill();           #ends the fill
    
def faceShadowChin():       #DEFINE 'faceShadowChin' function
    '''
    Function: faceShadowChin
    Description: on the face, it creates a shadow on the chin area
    Returns: None
    '''  
    t.fillcolor("#B54821"); #sets the fill color
    t.begin_fill();         #begins the fill
    t.goto(-34.0, 294.0);   #goes to the specified coordinate
    t.goto(-32.0, 295.0);
    t.goto(-30.0, 295.0);
    t.goto(-29.0, 291.0);
    t.goto(-27.0, 290.0);
    t.goto(-25.0, 290.0);
    t.goto(-22.0, 287.0);
    t.goto(-20.0, 285.0);
    t.goto(-17.0, 284.0);
    t.goto(-13.0, 284.0);
    t.goto(-8.0, 283.0);
    t.goto(-5.0, 283.0);
    t.goto(-2.0, 283.0);
    t.goto(0.0, 285.0);
    t.goto(1.0, 288.0);
    t.goto(7.0, 290.0);
    t.goto(4.0, 287.0);
    t.goto(7.0, 286.0);
    t.goto(13.0, 286.0);
    t.goto(15.0, 284.0);
    t.goto(19.0, 281.0);
    t.goto(13.0, 278.0);
    t.goto(11.0, 278.0);
    t.goto(9.0, 277.0);
    t.goto(4.0, 276.0);
    t.goto(-2.0, 276.0);
    t.goto(-5.0, 276.0);
    t.goto(-7.0, 276.0);
    t.goto(-10.0, 276.0);
    t.goto(-11.0, 276.0);
    t.goto(-12.0, 276.0);
    t.goto(-15.0, 279.0);
    t.goto(-17.0, 279.0);
    t.goto(-20.0, 280.0);
    t.goto(-23.0, 281.0);
    t.goto(-26.0, 284.0);
    t.goto(-31.0, 287.0);
    t.goto(-32.0, 290.0);
    t.goto(-33.0, 291.0);
    t.goto(-33.0, 294.0);
    t.goto(-33.0, 295.0);
    t.end_fill();               #ends the fill

def faceShadowChin1():      #DEFINE 'faceShadowChin1' function
    '''
    Function: faceShadowChin1
    Description: on the face, this function makes a shadow on the chin area. This is the second function that does this (numbered 1 because it starts with index 0)
    Returns: None
    '''  
    t.fillcolor("#9F5F43"); #sets fill color
    t.goto(6.0, 289.0);     #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(8.0, 290.0);
    t.goto(9.0, 292.0);
    t.goto(13.0, 294.0);
    t.goto(15.0, 296.0);
    t.goto(18.0, 298.0);
    t.goto(20.0, 298.0);
    t.goto(20.0, 296.0);
    t.goto(20.0, 293.0);
    t.goto(18.0, 293.0);
    t.goto(17.0, 289.0);
    t.goto(16.0, 287.0);
    t.goto(18.0, 283.0);
    t.goto(18.0, 281.0);
    t.goto(16.0, 282.0);
    t.goto(15.0, 284.0);
    t.goto(14.0, 285.0);
    t.goto(12.0, 286.0);
    t.goto(10.0, 286.0);
    t.goto(7.0, 286.0);
    t.goto(6.0, 286.0);
    t.goto(4.0, 286.0);
    t.goto(4.0, 288.0);
    t.goto(7.0, 289.0);
    t.end_fill();       #ends the fill

def faceShadowChin2():      #DECLARE 'faceShadowChin2' function
    '''
    Function: faceShadowChin2
    Description: makes a shadow on the face in the chin area. This is the third function that does this, hence the index number 2
    Returns: None
    '''  
    t.fillcolor("#945244")  #sets fill color
    t.goto(11.0, 293.0);    #goes to the specified coordinate
    t.begin_fill();     #begins the fill
    t.goto(17.0, 281.0);
    t.goto(19.0, 282.0);
    t.goto(23.0, 283.0);
    t.goto(25.0, 285.0);
    t.goto(27.0, 287.0);
    t.goto(27.0, 290.0);
    t.goto(30.0, 291.0);
    t.goto(33.0, 294.0);
    t.goto(35.0, 300.0);
    t.goto(37.0, 302.0);
    t.goto(37.0, 303.0);
    t.goto(40.0, 310.0);
    t.goto(42.0, 317.0);
    t.goto(41.0, 322.0);
    t.goto(42.0, 330.0);
    t.goto(42.0, 330.0);
    t.goto(40.0, 330.0);
    t.goto(38.0, 329.0);
    t.goto(37.0, 328.0);
    t.goto(35.0, 326.0);
    t.goto(34.0, 324.0);
    t.goto(33.0, 321.0);
    t.goto(30.0, 320.0);
    t.goto(26.0, 320.0);
    t.goto(24.0, 320.0);
    t.goto(24.0, 319.0);
    t.goto(24.0, 319.0);
    t.goto(23.0, 319.0);
    t.goto(23.0, 319.0);
    t.goto(23.0, 317.0);
    t.goto(23.0, 314.0);
    t.goto(22.0, 311.0);
    t.goto(20.0, 311.0);
    t.goto(21.0, 314.0);
    t.goto(20.0, 314.0);
    t.goto(18.0, 316.0);
    t.goto(18.0, 318.0);
    t.goto(18.0, 320.0);
    t.goto(18.0, 324.0);
    t.goto(16.0, 323.0);
    t.goto(16.0, 320.0);
    t.goto(15.0, 317.0);
    t.goto(15.0, 317.0);
    t.goto(17.0, 314.0);
    t.goto(20.0, 309.0);
    t.goto(21.0, 308.0);
    t.goto(21.0, 306.0);
    t.goto(21.0, 304.0);
    t.goto(19.0, 304.0);
    t.goto(19.0, 303.0);
    t.goto(19.0, 302.0);
    t.goto(19.0, 299.0);
    t.goto(16.0, 298.0);
    t.goto(15.0, 302.0);
    t.goto(15.0, 304.0);
    t.goto(14.0, 304.0);
    t.goto(12.0, 304.0);
    t.goto(13.0, 302.0);
    t.goto(13.0, 297.0);
    t.goto(12.0, 297.0);
    t.goto(12.0, 293.0);
    t.goto(8.0, 291.0);
    t.end_fill();           #ends the fill
def faceShadowChin3():      #DECLARE 'faceShadowChin3' function
    '''
    Function: faceShadowChin3
    Description: makes a shadow on the chin on the face. This is the fourth function that does this function, hence the 3rd index number in the name of the function
    Returns: None
    '''  
    t.fillcolor("#AB6A54"); #sets the fill color to #AB6A54
    t.goto(0.0, 305.0);     #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-3.0, 302.0);
    t.goto(-3.0, 297.0);
    t.goto(4.0, 297.0);
    t.goto(9.0, 297.0);
    t.goto(12.0, 293.0);
    t.goto(10.0, 293.0);
    t.goto(7.0, 293.0);
    t.goto(2.0, 291.0);
    t.goto(0.0, 289.0);
    t.goto(-1.0, 286.0);
    t.goto(3.0, 282.0);
    t.goto(15.0, 285.0);
    t.goto(25.0, 295.0);
    t.goto(36.0, 315.0);
    t.goto(34.0, 328.0);
    t.goto(32.0, 328.0);
    t.goto(30.0, 325.0);
    t.goto(27.0, 324.0);
    t.goto(23.0, 323.0);
    t.goto(20.0, 323.0);
    t.goto(18.0, 325.0);
    t.goto(16.0, 326.0);
    t.goto(15.0, 321.0);
    t.goto(15.0, 319.0);
    t.goto(11.0, 316.0);
    t.goto(7.0, 316.0);
    t.goto(5.0, 316.0);
    t.goto(6.0, 315.0);
    t.goto(-1.0, 304.0);
    t.end_fill();           #ends the fill

def upperLip():             #DECLARE 'upperLip' function
    '''
    Function: upperLip
    Description: makes the upper lip!!!!!!!!!
    Returns: None
    '''  
    t.fillcolor("#AF5648")  #sets the fill color to #AF5648
    t.goto(-18.0, 307.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-17.0, 308.0);
    t.goto(-14.0, 308.0);
    t.goto(-12.0, 308.0);
    t.goto(-10.0, 308.0);
    t.goto(-6.0, 308.0);
    t.goto(-4.0, 308.0);
    t.goto(-1.0, 307.0);
    t.goto(2.0, 307.0);
    t.goto(6.0, 308.0);
    t.goto(8.0, 308.0);
    t.goto(10.0, 308.0);
    t.goto(12.0, 307.0);
    t.goto(16.0, 306.0);
    t.goto(19.0, 309.0);
    t.goto(17.0, 310.0);
    t.goto(12.0, 311.0);
    t.goto(10.0, 312.0);
    t.goto(9.0, 313.0);
    t.goto(6.0, 314.0);
    t.goto(1.0, 314.0);
    t.goto(0.0, 311.0);
    t.goto(-1.0, 313.0);
    t.goto(-5.0, 313.0);
    t.goto(-9.0, 313.0);
    t.goto(-9.0, 311.0);
    t.goto(-11.0, 311.0);
    t.goto(-13.0, 311.0);
    t.goto(-15.0, 310.0);
    t.goto(-17.0, 309.0);
    t.goto(-17.0, 307.0);
    t.end_fill();           #ends the fill

def lowerLip():         #DECLARE 'lowerLip' function
    '''
    Function: lowerLip
    Description: makes the lower lip!!!!!!
    Returns: None
    '''  
    t.fillcolor("#E2676C"); #sets the fill color to the specified HEX code
    t.goto(-14.0, 307.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-11.0, 305.0);
    t.goto(-3.0, 305.0);
    t.goto(-1.0, 304.0);
    t.goto(4.0, 304.0);
    t.goto(7.0, 306.0);
    t.goto(10.0, 307.0);
    t.goto(10.0, 308.0);
    t.goto(10.0, 308.0);
    t.goto(7.0, 309.0);
    t.goto(5.0, 308.0);
    t.goto(3.0, 308.0);
    t.goto(0.0, 308.0);
    t.goto(-4.0, 308.0);
    t.goto(-8.0, 308.0);
    t.goto(-10.0, 308.0);
    t.goto(-13.0, 308.0);
    t.goto(-15.0, 308.0);
    t.goto(-16.0, 309.0);
    t.goto(-18.0, 309.0);
    t.end_fill();           #ends the fill
def nose():                 #DECLARE 'nose' function
    '''
    Function: nose
    Description: draws the nose
    Returns: None
    '''  
    t.fillcolor("#FB9B85"); #sets the fill color
    t.goto(-3.0, 353.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.pensize(2);           #pensize is 2
    t.pencolor("#9A4E37");  #pencolor is specified
    t.down();               #lowers the turtle
    t.goto(-2.0, 351.0);    #goes to the specified coordinate
    t.goto(-3.0, 347.0);
    t.goto(-5.0, 342.0);
    t.goto(-8.0, 337.0);
    t.goto(-10.0, 334.0);
    t.goto(-10.0, 332.0);
    t.goto(-13.0, 331.0);
    t.goto(-13.0, 328.0);
    t.goto(-12.0, 326.0);
    t.goto(-11.0, 325.0);
    t.goto(-9.0, 325.0);
    t.goto(-6.0, 325.0);
    t.goto(-4.0, 324.0);
    t.goto(-1.0, 322.0);
    t.goto(0.0, 322.0);
    t.goto(2.0, 322.0);
    t.goto(4.0, 324.0);
    t.goto(10.0, 326.0);
    t.goto(13.0, 325.0);
    t.goto(15.0, 328.0);
    t.goto(13.0, 331.0);
    t.goto(11.0, 332.0);
    t.goto(9.0, 334.0);
    t.goto(9.0, 334.0);
    t.goto(7.0, 339.0);
    t.goto(5.0, 344.0);
    t.goto(5.0, 347.0);
    t.goto(5.0, 352.0);
    t.goto(5.0, 353.0);
    t.goto(5.0, 353.0);
    t.goto(1.0, 353.0);
    t.goto(-2.0, 353.0);
    t.goto(-4.0, 351.0);
    t.end_fill();           #ends the fill
    t.up();                 #lifts the turtle

def noseShadow():           #DEFINE 'noseShadow' function
    '''
    Function: noseShadow
    Description: makes the shadow for the nose
    Returns: None
    '''  
    t.fillcolor("#682E20"); #sets the fill color to a dark brown
    t.goto(2.0, 321.0);     #goes to the specified coordinate
    t.begin_fill();         #starts the filling
    t.goto(0.0, 322.0);
    t.goto(-1.0, 321.0);
    t.goto(-1.0, 319.0);
    t.goto(2.0, 318.0);
    t.goto(6.0, 318.0);
    t.goto(10.0, 316.0);
    t.goto(13.0, 317.0);
    t.goto(14.0, 318.0);
    t.goto(15.0, 319.0);
    t.goto(16.0, 324.0);
    t.goto(16.0, 325.0);
    t.goto(15.0, 327.0);
    t.goto(15.0, 325.0);
    t.goto(13.0, 324.0);
    t.goto(11.0, 324.0);
    t.goto(9.0, 324.0);
    t.goto(8.0, 324.0);
    t.goto(5.0, 324.0);
    t.goto(4.0, 323.0);
    t.goto(2.0, 321.0);
    t.goto(0.0, 321.0);
    t.end_fill();           #finishes the filling
    
def noseShadow1():          #DECLARE 'noseShadow1' function
    '''
    Function: noseShadow1
    Description: makes the shadow of the nose. This is the second function that does this so it has an index number of 1 in its name
    Returns: None
    '''  
    t.fillcolor("#833A2B"); #sets the fill color
    t.goto(-10.0, 325.0);   #goes to the specified coordiante
    t.begin_fill();         #begins the fill
    t.goto(-11.0, 323.0);
    t.goto(-11.0, 322.0);
    t.goto(-8.0, 322.0);
    t.goto(-5.0, 321.0);
    t.goto(-3.0, 323.0);
    t.goto(-5.0, 324.0);
    t.goto(-7.0, 324.0);
    t.goto(-10.0, 324.0);
    t.end_fill();           #ends the fill

def leftGlass():            #DECLARE 'leftGlass' function
    '''
    Function: leftGlass
    Description: makes my left glasses
    Returns: None
    '''  
    t.pensize(2);               #sets pensize to 2
    t.pencolor("#4D3A3E");      #sets pencolor to that HEX code
    t.goto(-48.0, 354.0);       #goes to that point
    t.down();                   #lowers turtle
    t.goto(-48.0, 350.0);
    t.goto(-48.0, 350.0);
    t.goto(-43.0, 353.0);
    t.goto(-41.0, 353.0);
    t.goto(-40.0, 353.0);
    t.goto(-39.0, 351.0);
    t.goto(-39.0, 346.0);
    t.goto(-39.0, 342.0);
    t.goto(-37.0, 340.0);
    t.goto(-35.0, 337.0);
    t.goto(-33.0, 336.0);
    t.goto(-28.0, 337.0);
    t.goto(-23.0, 337.0);
    t.goto(-19.0, 337.0);
    t.goto(-15.0, 336.0);
    t.goto(-12.0, 338.0);
    t.goto(-8.0, 340.0);
    t.goto(-7.0, 343.0);
    t.goto(-6.0, 345.0);
    t.goto(-5.0, 349.0);
    t.goto(-4.0, 353.0);
    t.goto(-4.0, 356.0);
    t.goto(-5.0, 357.0);
    t.goto(-10.0, 358.0);
    t.goto(-13.0, 358.0);
    t.goto(-15.0, 358.0);
    t.goto(-16.0, 359.0);
    t.goto(-20.0, 359.0);
    t.goto(-25.0, 359.0);
    t.goto(-28.0, 359.0);
    t.goto(-28.0, 359.0);
    t.goto(-31.0, 358.0);
    t.goto(-33.0, 358.0);
    t.goto(-38.0, 358.0);
    t.goto(-39.0, 357.0);
    t.goto(-43.0, 356.0);
    t.goto(-46.0, 354.0);
    t.goto(-48.0, 352.0);
    t.goto(-49.0, 351.0);
    t.up();             #lifts turtle

def rightGlass():           #DECLARE 'rightGlass' function
    '''
    Function: rightGlass
    Description: makes my right glasses
    Returns: None
    '''  
    t.pensize(2);               #sets pensize to 2
    t.pencolor("#4D3A3E");      #sets pencolor to that
    t.goto(40.0, 358.0);        #goes to that coordinate
    t.down();                   #lowers turtle
    t.goto(40.0, 357.0);
    t.goto(40.0, 354.0);
    t.goto(40.0, 350.0);
    t.goto(40.0, 347.0);
    t.goto(39.0, 347.0);
    t.goto(39.0, 345.0);
    t.goto(39.0, 344.0);
    t.goto(38.0, 345.0);
    t.goto(39.0, 342.0);
    t.goto(37.0, 338.0);
    t.goto(34.0, 336.0);
    t.goto(14.0, 337.0);
    t.goto(12.0, 339.0);
    t.goto(10.0, 341.0);
    t.goto(7.0, 344.0);
    t.goto(7.0, 347.0);
    t.goto(6.0, 349.0);
    t.goto(5.0, 355.0);
    t.goto(5.0, 357.0);
    t.goto(7.0, 357.0);
    t.goto(9.0, 357.0);
    t.goto(10.0, 358.0);
    t.goto(17.0, 358.0);
    t.goto(18.0, 359.0);
    t.goto(36.0, 359.0);
    t.goto(39.0, 359.0);
    t.goto(39.0, 358.0);
    t.goto(40.0, 357.0);
    t.goto(40.0, 357.0);    
    t.up();                 #lifts turtle
    t.goto(-5.0, 357.0);        
    t.down();               #lowers turtle
    t.goto(6.0, 356.0);
    t.up();                 #lifts turtle

def eyeOutside():           #DEFINE 'eyeOutside' function
    '''
    Function: eyeOutside
    Description: makes the outside ring of the left eye 
    Returns: None
    '''  
    t.fillcolor("#935945"); #sets the fill color
    t.goto(-31.0, 352.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the filling
    t.goto(-28.0, 354.0);
    t.goto(-26.0, 355.0);
    t.goto(-24.0, 355.0);
    t.goto(-21.0, 355.0);
    t.goto(-19.0, 355.0);
    t.goto(-16.0, 355.0);
    t.goto(-14.0, 352.0);
    t.goto(-12.0, 351.0);
    t.goto(-14.0, 349.0);
    t.goto(-18.0, 349.0);
    t.goto(-21.0, 349.0);
    t.goto(-21.0, 349.0);
    t.goto(-27.0, 349.0);
    t.goto(-29.0, 350.0);
    t.goto(-31.0, 351.0);
    t.goto(-33.0, 353.0);
    t.end_fill();           #ends the filling process

def eyeWhite():         #DEFINE 'eyeWhite' function
    '''
    Function: eyeWhite
    Description: draws the eye whites of the left eye
    Returns: None
    '''  
    t.fillcolor("#96746A"); #sets the fill color
    t.goto(-24.0, 355.0);       #goes to the specified coordinate
    t.begin_fill();             #begins the fill
    t.goto(-27.0, 353.0);
    t.goto(-30.0, 353.0);
    t.goto(-30.0, 353.0);
    t.goto(-31.0, 351.0);
    t.goto(-28.0, 350.0);
    t.goto(-25.0, 349.0);
    t.goto(-21.0, 349.0);
    t.goto(-18.0, 349.0);
    t.goto(-13.0, 349.0);
    t.goto(-13.0, 351.0);
    t.goto(-15.0, 352.0);
    t.goto(-17.0, 353.0);
    t.goto(-18.0, 355.0);
    t.goto(-21.0, 355.0);
    t.goto(-25.0, 355.0);
    t.end_fill();           #ends the fill

def eyeBall():              #DEFINE 'eyeBall' function
    '''
    Function: eyeBall
    Description: makes the eyeball of the left eye
    Returns: None
    '''  
    t.fillcolor("#3B2B2E"); #sets the fill color
    t.goto(-24.0, 355.0);   #goes to the specified location
    t.begin_fill();         #begins the filling process
    t.goto(-26.0, 353.0);
    t.goto(-25.0, 349.0);
    t.goto(-19.0, 350.0);
    t.goto(-18.0, 352.0);
    t.goto(-18.0, 354.0);
    t.goto(-26.0, 355.0);
    t.goto(-26.0, 356.0);
    t.end_fill();           #ends the filling process

def eyeRight():             #DECLARE 'eyeRight' function
    '''
    Function: eyeRight
    Description: makes the right eye border
    Returns: None
    '''  
    t.fillcolor("#3B1E18"); #sets the fill color
    t.goto(16.0, 354.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(17.0, 355.0);
    t.goto(19.0, 356.0);
    t.goto(21.0, 356.0);
    t.goto(24.0, 356.0);
    t.goto(29.0, 354.0);
    t.goto(32.0, 353.0);
    t.goto(33.0, 351.0);
    t.goto(27.0, 349.0);
    t.goto(24.0, 349.0);
    t.goto(17.0, 349.0);
    t.goto(14.0, 349.0);
    t.goto(13.0, 349.0);
    t.goto(12.0, 350.0);
    t.goto(13.0, 353.0);
    t.goto(13.0, 353.0);
    t.goto(15.0, 355.0);
    t.goto(17.0, 355.0);
    t.end_fill();           #ends the fill

def eyeWhiteRight():        #DEFINE 'eyeWhiteRight' function
    '''
    Function:  eyeWhiteRight
    Description: draws the eyewhites of the right eye
    Returns: None
    '''  
    t.fillcolor("#6E5652"); #sets the fill color 
    t.goto(25.0, 355.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(27.0, 355.0);
    t.goto(28.0, 353.0);
    t.goto(31.0, 351.0);
    t.goto(30.0, 351.0);
    t.goto(27.0, 351.0);
    t.goto(21.0, 351.0);
    t.goto(18.0, 351.0);
    t.goto(16.0, 351.0);
    t.goto(14.0, 351.0);
    t.goto(16.0, 355.0);
    t.goto(18.0, 356.0);
    t.end_fill();       #ends the fill
def eyeBallRight():         #DEFINE 'eyeBallRight' function
    '''
    Function: eyeBallRight
    Description: makes the eyeball in the right eye
    Returns: None
    '''  
    t.fillcolor("#1C0C0C"); #sets the fill color
    t.goto(17.0, 355.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(19.0, 356.0);
    t.goto(21.0, 356.0);
    t.goto(26.0, 356.0);
    t.goto(24.0, 354.0);
    t.goto(24.0, 352.0);
    t.goto(21.0, 350.0);
    t.goto(18.0, 351.0);
    t.goto(18.0, 353.0);
    t.goto(17.0, 355.0);
    t.end_fill();           #ends the fill

def eyeBrowLeft():          #DEFINE 'eyeBrowLeft'
    '''
    Function: eyeBrowLeft
    Description: makes the left eyebrow
    Returns: None
    '''  
    t.fillcolor("#55372C"); #sets the fillcolor
    t.goto(-31.0, 372.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-27.0, 372.0);
    t.goto(-21.0, 371.0);
    t.goto(-17.0, 371.0);
    t.goto(-12.0, 371.0);
    t.goto(-10.0, 368.0);
    t.goto(-11.0, 365.0);
    t.goto(-16.0, 364.0);
    t.goto(-21.0, 366.0);
    t.goto(-31.0, 365.0);
    t.goto(-32.0, 363.0);
    t.goto(-38.0, 361.0);
    t.goto(-37.0, 366.0);
    t.goto(-36.0, 367.0);
    t.goto(-34.0, 370.0);
    t.goto(-28.0, 371.0);
    t.goto(-25.0, 371.0);
    t.end_fill();           #ends the fill
def eyeBrowRight():         #DEFINE 'eyeBrowRight' function
    '''
    Function: eyeBrowRight
    Description: makes the right eyebrow
    Returns: None
    '''  
    t.fillcolor("#442C28"); #sets the fillcolor
    t.goto(22.0, 373.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(20.0, 373.0);
    t.goto(14.0, 371.0);
    t.goto(9.0, 369.0);
    t.goto(11.0, 367.0);
    t.goto(14.0, 367.0);
    t.goto(21.0, 367.0);
    t.goto(23.0, 366.0);
    t.goto(29.0, 366.0);
    t.goto(32.0, 365.0);
    t.goto(37.0, 364.0);
    t.goto(35.0, 370.0);
    t.goto(32.0, 373.0);
    t.goto(29.0, 374.0);
    t.goto(27.0, 375.0);
    t.goto(27.0, 375.0);
    t.goto(25.0, 374.0);
    t.goto(25.0, 373.0);
    t.goto(21.0, 373.0);
    t.goto(20.0, 373.0);
    t.goto(19.0, 373.0);
    t.goto(17.0, 373.0);
    t.end_fill();           #ends the fill


def hairShadow():           #DEFINE 'hairShadow' function
    '''
    Function: hairShadow
    Description: makes the hair shadow
    Returns: None
    '''  
    t.fillcolor("#905640"); #sets the fill color
    t.goto(-50.0, 364.0);   #goes to the specified coordinate
    t.begin_fill()          #begins the fill
    t.goto(-39.0, 374.0);
    t.goto(-37.0, 374.0);
    t.goto(-32.0, 377.0);
    t.goto(-31.0, 379.0);
    t.goto(-29.0, 382.0);
    t.goto(-24.0, 387.0);
    t.goto(-21.0, 389.0);
    t.goto(-17.0, 391.0);
    t.goto(-13.0, 389.0);
    t.goto(-10.0, 385.0);
    t.goto(-7.0, 379.0);
    t.goto(-2.0, 383.0);
    t.goto(4.0, 387.0);
    t.goto(6.0, 387.0);
    t.goto(12.0, 383.0);
    t.goto(13.0, 381.0);
    t.goto(21.0, 378.0);
    t.goto(22.0, 378.0);
    t.goto(30.0, 376.0);
    t.goto(33.0, 372.0);
    t.goto(36.0, 369.0);
    t.goto(42.0, 370.0);
    t.goto(39.0, 376.0);
    t.goto(39.0, 377.0);
    t.goto(35.0, 383.0);
    t.goto(27.0, 387.0);
    t.goto(22.0, 390.0);
    t.goto(21.0, 396.0);
    t.goto(16.0, 399.0);
    t.goto(10.0, 400.0);
    t.goto(3.0, 402.0);
    t.goto(2.0, 402.0);
    t.goto(-3.0, 403.0);
    t.goto(-9.0, 404.0);
    t.goto(-12.0, 404.0);
    t.goto(-16.0, 404.0);
    t.goto(-19.0, 404.0);
    t.goto(-23.0, 400.0);
    t.goto(-29.0, 393.0);
    t.goto(-34.0, 385.0);
    t.goto(-39.0, 381.0);
    t.goto(-43.0, 376.0);
    t.goto(-49.0, 370.0);
    t.goto(-49.0, 366.0);
    t.end_fill();           #ends fill

def hairShadow1():          #DEFINE 'hairShadow1'
    '''
    Function: hairShadow1
    Description: makes the hair shadow upper part
    Returns: None
    '''  
    t.fillcolor("#71422E"); #sets fill color
    t.goto(-44.0, 377.0);   #goes to the specified location
    t.begin_fill();         #begins the fill
    t.goto(-40.0, 377.0);
    t.goto(-37.0, 377.0);
    t.goto(-33.0, 384.0);
    t.goto(-28.0, 388.0);
    t.goto(-27.0, 393.0);
    t.goto(-23.0, 393.0);
    t.goto(-16.0, 395.0);
    t.goto(-12.0, 393.0);
    t.goto(-9.0, 390.0);
    t.goto(-3.0, 390.0);
    t.goto(3.0, 393.0);
    t.goto(8.0, 393.0);
    t.goto(15.0, 387.0);
    t.goto(20.0, 380.0);
    t.goto(22.0, 380.0);
    t.goto(28.0, 379.0);
    t.goto(31.0, 376.0);
    t.goto(36.0, 374.0);
    t.goto(41.0, 372.0);
    t.goto(43.0, 370.0);
    t.goto(40.0, 377.0);
    t.goto(30.0, 391.0);
    t.goto(16.0, 410.0);
    t.goto(-25.0, 420.0);
    t.goto(-46.0, 412.0);
    t.goto(-52.0, 393.0);
    t.goto(-50.0, 374.0);
    t.goto(-45.0, 374.0);
    t.goto(-40.0, 376.0);
    t.end_fill();           #ends the fill

def hair():                 #DEFINE 'hair' function
    '''
    Function: hair
    Description: makes the hair
    Returns: None
    '''  
    t.fillcolor("#251F1F"); #sets the fill color
    t.goto(-49.0, 341.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-51.0, 363.0);
    t.goto(-49.0, 372.0);
    t.goto(-44.0, 376.0);
    t.goto(-39.0, 380.0);
    t.goto(-36.0, 383.0);
    t.goto(-34.0, 386.0);
    t.goto(-31.0, 388.0);
    t.goto(-28.0, 392.0);
    t.goto(-24.0, 397.0);
    t.goto(-22.0, 402.0);
    t.goto(-17.0, 402.0);
    t.goto(-15.0, 402.0);
    t.goto(-11.0, 400.0);
    t.goto(-3.0, 399.0);
    t.goto(2.0, 401.0);
    t.goto(4.0, 401.0);
    t.goto(6.0, 401.0);
    t.goto(9.0, 400.0);
    t.goto(9.0, 402.0);
    t.goto(14.0, 402.0);
    t.goto(15.0, 401.0);
    t.goto(16.0, 400.0);
    t.goto(16.0, 400.0);
    t.goto(19.0, 398.0);
    t.goto(23.0, 390.0);
    t.goto(34.0, 385.0);
    t.goto(41.0, 376.0);
    t.goto(41.0, 373.0);
    t.goto(43.0, 368.0);
    t.goto(43.0, 361.0);
    t.goto(43.0, 353.0);
    t.goto(43.0, 346.0);
    t.goto(43.0, 344.0);
    t.goto(47.0, 349.0);
    t.goto(50.0, 352.0);
    t.goto(51.0, 356.0);
    t.goto(51.0, 360.0);
    t.goto(51.0, 367.0);
    t.goto(52.0, 376.0);
    t.goto(52.0, 377.0);
    t.goto(52.0, 382.0);
    t.goto(53.0, 388.0);
    t.goto(54.0, 399.0);
    t.goto(50.0, 404.0);
    t.goto(48.0, 406.0);
    t.goto(45.0, 410.0);
    t.goto(38.0, 415.0);
    t.goto(36.0, 419.0);
    t.goto(36.0, 423.0);
    t.goto(31.0, 426.0);
    t.goto(27.0, 427.0);
    t.goto(26.0, 428.0);
    t.goto(25.0, 429.0);
    t.goto(19.0, 432.0);
    t.goto(15.0, 433.0);
    t.goto(10.0, 436.0);
    t.goto(9.0, 436.0);
    t.goto(4.0, 439.0);
    t.goto(-4.0, 439.0);
    t.goto(-7.0, 439.0);
    t.goto(-5.0, 442.0);
    t.goto(-5.0, 443.0);
    t.goto(-7.0, 443.0);
    t.goto(-9.0, 441.0);
    t.goto(-14.0, 438.0);
    t.goto(-14.0, 442.0);
    t.goto(-18.0, 440.0);
    t.goto(-22.0, 438.0);
    t.goto(-25.0, 436.0);
    t.goto(-28.0, 434.0);
    t.goto(-30.0, 433.0);
    t.goto(-38.0, 430.0);
    t.goto(-41.0, 427.0);
    t.goto(-45.0, 425.0);
    t.goto(-52.0, 419.0);
    t.goto(-55.0, 418.0);
    t.goto(-56.0, 416.0);
    t.goto(-58.0, 414.0);
    t.goto(-61.0, 409.0);
    t.goto(-63.0, 405.0);
    t.goto(-64.0, 399.0);
    t.goto(-64.0, 395.0);
    t.goto(-65.0, 390.0);
    t.goto(-65.0, 384.0);
    t.goto(-64.0, 378.0);
    t.goto(-62.0, 373.0);
    t.goto(-62.0, 368.0);
    t.goto(-60.0, 364.0);
    t.goto(-61.0, 359.0);
    t.goto(-60.0, 353.0);
    t.goto(-58.0, 349.0);
    t.goto(-54.0, 347.0);
    t.goto(-56.0, 347.0);
    t.goto(-53.0, 344.0);
    t.goto(-51.0, 343.0);
    t.goto(-50.0, 342.0);
    t.end_fill();           #ends fill

def earLeftOutside():       #DEFINE 'earLeftOutside' function   
    '''
    Function: earLeftOutside
    Description: makes the outside of the left ear
    Returns: None
    '''  
    t.fillcolor("#E5876E"); #sets the fill color
    t.goto(-48.0, 340.0);   #goes to the specific coordinate
    t.begin_fill()          #begins the fill
    t.goto(-51.0, 343.0);
    t.goto(-55.0, 343.0);
    t.goto(-57.0, 346.0);
    t.goto(-60.0, 347.0);
    t.goto(-64.0, 347.0);
    t.goto(-66.0, 345.0);
    t.goto(-66.0, 343.0);
    t.goto(-65.0, 338.0);
    t.goto(-65.0, 335.0);
    t.goto(-62.0, 327.0);
    t.goto(-57.0, 321.0);
    t.goto(-50.0, 315.0);
    t.goto(-44.0, 312.0);
    t.goto(-42.0, 311.0);
    t.goto(-43.0, 317.0);
    t.goto(-43.0, 320.0);
    t.goto(-43.0, 323.0);
    t.goto(-45.0, 326.0);
    t.goto(-47.0, 331.0);
    t.goto(-48.0, 337.0);
    t.goto(-48.0, 340.0);
    t.goto(-49.0, 342.0);
    t.end_fill();           #ends the fill

def earLeftShadow():            #DEFINE 'earLeftShadow' function
    '''
    Function: earLeftShadow
    Description: makes the shadow of the left ear
    Returns: None
    '''  
    t.fillcolor("#B6150B");     #sets the fill color
    t.goto(-52.0, 337.0);       #goes to the specified coordinate
    t.begin_fill();             #begins the fill
    t.goto(-53.0, 340.0);
    t.goto(-54.0, 342.0);
    t.goto(-58.0, 343.0);
    t.goto(-60.0, 343.0);
    t.goto(-63.0, 341.0);
    t.goto(-63.0, 339.0);
    t.goto(-62.0, 335.0);
    t.goto(-61.0, 330.0);
    t.goto(-59.0, 328.0);
    t.goto(-56.0, 325.0);
    t.goto(-58.0, 329.0);
    t.goto(-59.0, 333.0);
    t.goto(-60.0, 336.0);
    t.goto(-60.0, 337.0);
    t.goto(-59.0, 337.0);
    t.goto(-58.0, 337.0);
    t.goto(-55.0, 338.0);
    t.goto(-53.0, 338.0);
    t.goto(-52.0, 337.0);
    t.end_fill();           #ends the fill

def earLeftCircle():                #DEFINE 'earLeftCircle' function
    '''
    Function: earLeftCircle
    Description: makes the left circle in the ear
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#A2402D"); #sets the fill color
    t.goto(-52.0, 335.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-49.0, 335.0);
    t.goto(-49.0, 332.0);
    t.goto(-49.0, 332.0);
    t.goto(-50.0, 328.0);
    t.goto(-50.0, 326.0);
    t.goto(-50.0, 325.0);
    t.goto(-50.0, 323.0);
    t.goto(-54.0, 325.0);
    t.goto(-56.0, 327.0);
    t.goto(-56.0, 329.0);
    t.goto(-56.0, 330.0);
    t.goto(-58.0, 329.0);
    t.goto(-58.0, 329.0);
    t.goto(-58.0, 331.0);
    t.goto(-57.0, 335.0);
    t.goto(-53.0, 335.0);
    t.goto(-49.0, 336.0);
    t.goto(-49.0, 335.0);
    t.end_fill();           #ends the fill

def earLeftRing():          #DEFINE 'earLeftRing' function
    '''
    Function: earLeftRing
    Description: makes the left ring in the ear
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#D0774D"); #sets the fill color
    t.goto(-46.0, 329.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-45.0, 326.0);
    t.goto(-42.0, 323.0);
    t.goto(-43.0, 318.0);
    t.goto(-44.0, 315.0);
    t.goto(-45.0, 317.0);
    t.goto(-47.0, 319.0);
    t.goto(-49.0, 320.0);
    t.goto(-53.0, 321.0);
    t.goto(-53.0, 322.0);
    t.goto(-47.0, 320.0);
    t.goto(-45.0, 320.0);
    t.goto(-45.0, 323.0);
    t.goto(-47.0, 324.0);
    t.goto(-47.0, 326.0);
    t.goto(-46.0, 328.0);
    t.goto(-46.0, 328.0);
    t.end_fill();           #ends the fill

def earRightOutside():          #DEFINE 'earRightOutside' function
    '''
    Function: earRightOutside
    Description: makes the outside of the right ear
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#9F5451"); #sets the fill color
    t.goto(41.0, 343.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(45.0, 346.0);
    t.goto(49.0, 347.0);
    t.goto(51.0, 347.0);
    t.goto(54.0, 347.0);
    t.goto(56.0, 345.0);
    t.goto(57.0, 341.0);
    t.goto(57.0, 337.0);
    t.goto(57.0, 333.0);
    t.goto(55.0, 331.0);
    t.goto(53.0, 328.0);
    t.goto(49.0, 323.0);
    t.goto(44.0, 321.0);
    t.goto(42.0, 320.0);
    t.goto(41.0, 319.0);
    t.goto(42.0, 341.0);
    t.end_fill();           #ends the fill

def earRightRed():          #DEFINE 'earRightRed' function
    '''
    Function: earRightRed
    Description: makes the red part of the right ear
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#730C07"); #sets the fill color
    t.goto(50.0, 343.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(51.0, 343.0);
    t.goto(52.0, 339.0);
    t.goto(53.0, 337.0);
    t.goto(53.0, 337.0);
    t.goto(53.0, 335.0);
    t.goto(50.0, 332.0);
    t.goto(49.0, 329.0);
    t.goto(46.0, 324.0);
    t.goto(55.0, 339.0);
    t.goto(54.0, 343.0);
    t.goto(54.0, 343.0);
    t.goto(51.0, 343.0);
    t.end_fill();           #begins the fill

def earRightCircle():       #DEFINE 'earRightCircle' function
    '''
    Function: earRightCircle
    Description: makes the circle in the right ear
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#6B1312"); #sets the fill color
    t.goto(43.0, 342.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(45.0, 335.0);
    t.goto(47.0, 332.0);
    t.goto(46.0, 328.0);
    t.goto(43.0, 325.0);
    t.goto(43.0, 325.0);
    t.goto(43.0, 341.0);
    t.end_fill();           #ends the fill

def earRightShadow():       #DEFINE 'earRightShadow' function
    '''
    Function: earRightShadow
    Description: makes the shadow in the right ear
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#9D4136"); #sets the fill color
    t.goto(43.0, 340.0);    #goes to the specified coordinate
    t.begin_fill();         #begins the filling
    t.goto(46.0, 334.0);
    t.goto(47.0, 329.0);
    t.goto(43.0, 325.0);
    t.goto(44.0, 323.0);
    t.goto(51.0, 332.0);
    t.goto(51.0, 338.0);
    t.goto(52.0, 340.0);
    t.goto(52.0, 342.0);
    t.goto(49.0, 344.0);
    t.goto(47.0, 343.0);
    t.goto(47.0, 342.0);
    t.goto(46.0, 341.0);
    t.goto(45.0, 341.0);
    t.goto(43.0, 341.0);
    t.end_fill();           #ends the filling

def hoodieCheck():              #DEFINE 'hoodieCheck' function
    '''
    Function: hoodieCheck
    Description: checks for line leaks in the hoodie
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#E90101");     #sets the fill color
    t.goto(-115.0, -96.0);      #goes to the specified coordinate
    t.begin_fill();             #begin the fill
    t.goto(-87.0, -84.0);
    t.goto(-52.0, -96.0);
    t.goto(-17.0, -89.0);
    t.goto(3.0, -92.0);
    t.goto(21.0, -79.0);
    t.goto(47.0, -75.0);
    t.goto(65.0, -82.0);
    t.goto(119.0, -74.0);
    t.goto(133.0, 16.0);
    t.goto(141.0, 24.0);
    t.goto(151.0, 92.0);
    t.goto(140.0, 172.0);
    t.goto(140.0, 198.0);
    t.goto(125.0, 218.0);
    t.goto(96.0, 235.0);
    t.goto(83.0, 257.0);
    t.goto(62.0, 253.0);
    t.goto(22.0, 245.0);
    t.goto(-1.0, 243.0);
    t.goto(-21.0, 251.0);
    t.goto(-47.0, 255.0);
    t.goto(-78.0, 242.0);
    t.goto(-94.0, 239.0);
    t.goto(-119.0, 226.0);
    t.goto(-133.0, 208.0);
    t.goto(-144.0, 189.0);
    t.goto(-142.0, 106.0);
    t.goto(-113.0, -27.0);
    t.goto(-115.0, -64.0);
    t.goto(-122.0, -83.0);
    t.goto(-113.0, -98.0);
    t.end_fill();           #ends the fill
    
def pantCheckLeft():                #DEFINE 'pantCheckLeft' function
    '''
    Function: pantCheckLeft
    Description: fills empty lines in the pants
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#443E3E"); #sets the fill color
    t.goto(-113.0, -96.0);  #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-87.0, -82.0);
    t.goto(-60.0, -104.0);
    t.goto(-51.0, -110.0);
    t.goto(-43.0, -139.0);
    t.goto(-26.0, -159.0);
    t.goto(-39.0, -184.0);
    t.goto(-34.0, -202.0);
    t.goto(24.0, -314.0);
    t.goto(57.0, -394.0);
    t.goto(28.0, -402.0);
    t.goto(-6.0, -368.0);
    t.goto(-33.0, -303.0);
    t.goto(-71.0, -317.0);
    t.goto(-132.0, -277.0);
    t.goto(-140.0, -274.0);
    t.goto(-144.0, -257.0);
    t.goto(-126.0, -156.0);
    t.goto(-113.0, -97.0);
    t.end_fill();           #ends the fill

def handCheck():            #DEFINE 'handCheck' function
    '''
    Function: handCheck
    Description: fills in extra spaces in the hands
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#FFB289"); #sets the fill color
    t.goto(-21.0, -93.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-28.0, -98.0);
    t.goto(-37.0, -106.0);
    t.goto(-38.0, -106.0);
    t.goto(-41.0, -112.0);
    t.goto(-38.0, -146.0);
    t.goto(-23.0, -163.0);
    t.goto(4.0, -168.0);
    t.goto(34.0, -181.0);
    t.goto(34.0, -165.0);
    t.goto(63.0, -143.0);
    t.goto(62.0, -110.0);
    t.goto(56.0, -85.0);
    t.goto(41.0, -75.0);
    t.goto(27.0, -76.0);
    t.goto(-25.0, -91.0);
    t.end_fill();           #ends the fill

def pantCheckRight():       #DEFINE 'pantCheckRight' function
    '''
    Function: pantCheckRight
    Description: fills in the empty holes in the right pant
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#615756"); #sets the fill color
    t.goto(120.0, -70.0);   #goes to the specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(95.0, -74.0);
    t.goto(82.0, -76.0);
    t.goto(67.0, -96.0);
    t.goto(55.0, -114.0);
    t.goto(55.0, -124.0);
    t.goto(54.0, -134.0);
    t.goto(44.0, -148.0);
    t.goto(35.0, -159.0);
    t.goto(37.0, -167.0);
    t.goto(54.0, -191.0);
    t.goto(49.0, -201.0);
    t.goto(52.0, -208.0);
    t.goto(56.0, -225.0);
    t.goto(46.0, -239.0);
    t.goto(34.0, -263.0);
    t.goto(26.0, -286.0);
    t.goto(57.0, -328.0);
    t.goto(80.0, -315.0);
    t.goto(97.0, -301.0);
    t.goto(132.0, -274.0);
    t.goto(138.0, -271.0);
    t.goto(153.0, -233.0);
    t.goto(148.0, -130.0);
    t.goto(139.0, -97.0);
    t.goto(127.0, -91.0);
    t.goto(121.0, -72.0);
    t.goto(112.0, -73.0);
    t.goto(85.0, -79.0);
    t.end_fill();           #ends the fill
    
def faceCheck():                #DEFINE 'faceCheck' function
    '''
    Function: faceCheck
    Description: fills in the empty spaces in the face
    Variables: none
    Returns: None
    '''  
    t.fillcolor("#E89062"); #sets the fill color
    t.goto(-25.0, 408.0);   #goes to a specified coordinate
    t.begin_fill();         #begins the fill
    t.goto(-42.0, 388.0);
    t.goto(-60.0, 379.0);
    t.goto(-53.0, 358.0);
    t.goto(-51.0, 334.0);
    t.goto(-35.0, 303.0);
    t.goto(3.0, 286.0);
    t.goto(34.0, 305.0);
    t.goto(44.0, 338.0);
    t.goto(47.0, 354.0);
    t.goto(45.0, 376.0);
    t.goto(32.0, 398.0);
    t.goto(9.0, 413.0);
    t.goto(-22.0, 415.0);
    t.end_fill();           #ends the fill

def shoe(): #DEFINE 'shoe' function
    '''
    Function: shoe
    Description: makes the shoe
    Variables: none
    Returns: None
    '''  
    poly("#CDC7BE",-26.0,-335.0,-26.0,-335.0,-27.0,-341.0,-27.0,-345.0,-22.0,-352.0,-16.0,-365.0,-7.0,-371.0,2.0,-378.0,8.0,-385.0,16.0,-390.0,19.0,-397.0,24.0,-403.0,28.0,-418.0,33.0,-425.0,46.0,-431.0,49.0,-434.0,55.0,-437.0,66.0,-438.0,74.0,-438.0,80.0,-436.0,89.0,-434.0,95.0,-429.0,101.0,-426.0,103.0,-418.0,101.0,-411.0,96.0,-400.0,94.0,-396.0,90.0,-392.0,87.0,-386.0,86.0,-384.0,82.0,-380.0,73.0,-374.0,61.0,-365.0,57.0,-359.0,49.0,-350.0,28.0,-336.0,19.0,-327.0,8.0,-317.0);  #CALL 'poly' function with the color to fill and the coordinates
    poly("#782726",-27.0,-336.0,-27.0,-342.0,-27.0,-347.0,-24.0,-355.0,-19.0,-365.0,-14.0,-368.0,-4.0,-375.0,-1.0,-377.0,8.0,-381.0,-3.0,-368.0,-12.0,-360.0,-16.0,-356.0,-22.0,-346.0,-24.0,-342.0,-27.0,-338.0,-28.0,-336.0);     #CALL 'poly' function with the color to fill and the coordinates
    poly("#141414",-9.0,-363.0,-6.0,-364.0,-3.0,-369.0,-2.0,-371.0,2.0,-375.0,7.0,-379.0,10.0,-382.0,12.0,-383.0,21.0,-393.0,24.0,-397.0,27.0,-401.0,30.0,-404.0,32.0,-412.0,34.0,-416.0,46.0,-424.0,50.0,-427.0,60.0,-430.0,66.0,-431.0,78.0,-432.0,87.0,-433.0,83.0,-430.0,87.0,-422.0,88.0,-421.0,89.0,-421.0,90.0,-421.0,93.0,-421.0,98.0,-422.0,100.0,-422.0,102.0,-414.0,100.0,-411.0,97.0,-406.0,93.0,-399.0,93.0,-394.0,91.0,-392.0,88.0,-387.0,84.0,-381.0,83.0,-379.0,78.0,-374.0,74.0,-372.0,72.0,-371.0,70.0,-369.0,68.0,-365.0,64.0,-359.0,62.0,-357.0,58.0,-351.0,57.0,-350.0,55.0,-346.0,54.0,-344.0,54.0,-344.0,51.0,-346.0,48.0,-346.0,44.0,-347.0,39.0,-348.0,34.0,-350.0,25.0,-353.0,18.0,-354.0,5.0,-357.0,0.0,-360.0,-10.0,-362.0,-10.0,-363.0);   #CALL 'poly' function with the color to fill and the coordinates

def me():
    '''
    Function: me
    Description: makes my self portrait
    Variables: none
    Returns: None
    '''      
    #doublechecking
    hoodieCheck();          #CALL 'hoodieCheck' function (descriptions of functions are commented inside the function)
    pantCheckLeft();        #CALL 'pantCheckLeft' function
    handCheck();            #CALL 'handCheck' function
    pantCheckRight();       #CALL 'pantCheckRight' function
    faceCheck();            #CALL 'faceCheck' function
    
    #shoe
    shoe();                 #CALL 'shoe' function
    
    # face
    face();                 #CALL 'face' function
    faceShadowChin3();      #CALL 'faceShadowChin3' function
    faceShadowChin();       #CALL 'faceShadowChin' function
    faceShadowChin1();      #CALL 'faceShadowChin1' function
    faceShadowChin2();      #CALL 'faceShadowChin2' function

    #ear
    earLeftOutside();       #CALL 'earLeftOutside' function
    earLeftShadow();        #CALL 'earLeftShadow' function
    earLeftRing();          #CALL 'earLeftRing' function
    earLeftCircle();        #CALL 'earLeftCircle' function
    


    earRightOutside();        #CALL 'earRightOutside' function
    earRightShadow();           #CALL 'earRightShadow' function
    earRightCircle();           #CALL 'earRightCircle' function
    earRightRed();              #CALL 'earRightRed' function


    #hair
    hairShadow();           #CALL 'hairShadow' function
    hairShadow1();          #CALL 'hairShadow1' function
    hair();                 #CALL 'hair'



    #lip
    upperLip();             #CALL 'upperLip' function
    lowerLip();             #CALL 'lowerLip' function
    neck();                 #CALL 'neck' function
    neckShadow()            #CALL 'neckShadow' function

    #nose
    nose();                 #CALL 'nose' function
    noseShadow();           #CALL 'noseShadow' function
    noseShadow1();          #CALL 'noseShadow1' function

    #glasses
    leftGlass();            #CALL 'leftGlass' function
    rightGlass();           #CALL 'rightGlass' function

    #eyeballLeft
    eyeOutside();           #CALL 'eyeOutside' function
    eyeWhite();             #CALL 'eyeWhite' function
    eyeBall();              #CALL 'eyeBall' function

    #eyeballRight
    eyeRight();             #CALL 'eyeRight' function
    eyeWhiteRight();        #CALL 'eyeWhiteRight' function
    eyeBallRight();         #CALL 'eyeBallRight' function

    #eyebrows
    eyeBrowLeft();          #CALL 'eyeBrowLeft' function
    eyeBrowRight();         #CALL 'eyeBrowRight' function
    
    # body
    armLeft();              #CALL 'armLeft' function
    armRight();             #CALL 'armRight' function
    hands();                #CALL 'hands' function
    logo();                 #CALL 'logo' function
    bodyTop();              #CALL 'bodyTop' function
    hoodie();               #CALL 'hoodie' function
    legLeft();              #CALL 'legLeft' function
    legRight();             #CALL 'legRight' function

def chair():                #DEFINE 'chair' function
    '''
    Function: chair
    Description: makes the bench/chair that I will sit on
    Variables: none
    Returns: None
    '''   
    poly("grey",-233.0,-258.0,-236.0,-430.0,-256.0,-438.0,-259.0,-262.0);           #CALL 'poly' function with the color and coordinates as arguments sent
    poly("grey",250.0,-264.0,253.0,-423.0,286.0,-438.0,286.0,-268.0);               #CALL 'poly' function with the color and coordinates as arguments sent
    poly("black",-301.0,-268.0,-297.0,-444.0,-255.0,-444.0,-257.0,-264.0);          #CALL 'poly' function with the color and coordinates as arguments sent
    poly("black",282.0,-274.0,283.0,-443.0,320.0,-444.0,314.0,-275.0);              #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#ffd3a3", -266.0, -77.0, -314.0, -220.0, 327.0, -220.0, 262.0, -77.0);   #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#b5814a",-313.0,-220.0,-308.0,-267.0,322.0,-275.0,328.0,-219.0);          #CALL 'poly' function with the color and coordinates as arguments sent
def hillShape():                                                                    #DEFINE 'hillShape' function
    '''
    Function: hillShape
    Description: makes the hill
    Variables: none
    Returns: None
    '''   
    poly("#3C5018",-600.0,-51.0,-581.0,-47.0,-572.0,-44.0,-556.0,-43.0,-541.0,-41.0,-520.0,-37.0,-498.0,-33.0,-480.0,-32.0,-453.0,-29.0,-439.0,-26.0,-415.0,-26.0,-386.0,-24.0,-358.0,-21.0,-342.0,-21.0,-321.0,-22.0,-302.0,-23.0,-270.0,-23.0,-321.0,-23.0,-297.0,-24.0,-280.0,-24.0,-240.0,-24.0,-213.0,-24.0,-176.0,-27.0,-138.0,-28.0,-116.0,-33.0,139.0,-61.0,178.0,-65.0,199.0,-69.0,229.0,-73.0,243.0,-74.0,266.0,-77.0,293.0,-80.0,326.0,-85.0,349.0,-88.0,389.0,-96.0,435.0,-102.0,482.0,-105.0,507.0,-111.0,521.0,-115.0,554.0,-118.0,587.0,-122.0,601.0,-123.0,631.0,-370.0,601.0,-456.0,-610.0,-456.0,-615.0,-50.0);                       #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#8FB625",-448.0,-27.0,-407.0,-25.0,-373.0,-21.0,-345.0,-22.0,-250.0,-33.0,-225.0,-38.0,-198.0,-42.0,-153.0,-48.0,-95.0,-55.0,9.0,-72.0,297.0,-160.0,319.0,-161.0,351.0,-161.0,394.0,-165.0,441.0,-171.0,441.0,-262.0,408.0,-268.0,334.0,-265.0,247.0,-263.0,236.0,-269.0,140.0,-270.0,-165.0,-226.0,-300.0,-208.0,-327.0,-208.0,-349.0,-201.0,-395.0,-198.0,-442.0,-197.0,-449.0,-197.0,-450.0,-29.0)          #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#476326",440.0,-137.0,422.0,-135.0,405.0,-130.0,374.0,-125.0,340.0,-121.0,312.0,-114.0,276.0,-109.0,247.0,-104.0,180.0,-97.0,115.0,-90.0,57.0,-81.0,5.0,-73.0,-53.0,-59.0,-98.0,-46.0,-146.0,-36.0,-173.0,-30.0,-207.0,-29.0,-234.0,-23.0,-268.0,-22.0,-286.0,-22.0,-310.0,-22.0,-340.0,-23.0,-369.0,-23.0,-392.0,-23.0,-407.0,-26.0,-427.0,-27.0,-448.0,-27.0,-450.0,-30.0,-449.0,-53.0,-406.0,-48.0,-393.0,-47.0,-373.0,-45.0,-340.0,-42.0,-329.0,-40.0,-308.0,-40.0,-292.0,-40.0,-259.0,-42.0,-228.0,-43.0,-209.0,-50.0,-182.0,-65.0,-166.0,-71.0,-109.0,-87.0,-59.0,-97.0,11.0,-119.0,93.0,-128.0,161.0,-137.0,223.0,-150.0,259.0,-154.0,290.0,-156.0,313.0,-157.0,332.0,-159.0,358.0,-163.0,374.0,-165.0,384.0,-167.0,404.0,-169.0,413.0,-169.0,433.0,-169.0,441.0,-171.0);          #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#31471A",-447.0,-206.0,-425.0,-202.0,-409.0,-200.0,-376.0,-200.0,-336.0,-212.0,-289.0,-225.0,-224.0,-236.0,-166.0,-246.0,-95.0,-258.0,-16.0,-283.0,36.0,-285.0,102.0,-294.0,186.0,-296.0,238.0,-283.0,277.0,-281.0,325.0,-270.0,346.0,-266.0,365.0,-264.0,393.0,-260.0,418.0,-260.0,438.0,-261.0,441.0,-265.0,438.0,-280.0,367.0,-281.0,341.0,-285.0,292.0,-289.0,258.0,-291.0,205.0,-285.0,164.0,-287.0,105.0,-290.0,52.0,-292.0,12.0,-287.0,-90.0,-287.0,-131.0,-291.0,-174.0,-288.0,-227.0,-291.0,-250.0,-285.0,-269.0,-272.0,-312.0,-251.0,-343.0,-236.0,-378.0,-227.0,-416.0,-219.0,-435.0,-218.0,-449.0,-220.0);                        #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#1C2B0C",-448.0,-218.0,-422.0,-220.0,-405.0,-221.0,-372.0,-230.0,-326.0,-242.0,-274.0,-251.0,-223.0,-262.0,-165.0,-272.0,-128.0,-274.0,-95.0,-280.0,-57.0,-285.0,-82.0,-290.0,-123.0,-287.0,-142.0,-286.0,-173.0,-286.0,-217.0,-287.0,-234.0,-286.0,-252.0,-286.0,-261.0,-288.0,-283.0,-288.0,-297.0,-287.0,-313.0,-285.0,-331.0,-286.0,-343.0,-290.0,-355.0,-290.0,-371.0,-289.0,-384.0,-289.0,-397.0,-289.0,-414.0,-289.0,-444.0,-291.0,-448.0,-291.0,-450.0,-291.0);           #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#1E1E21",-451.0,-292.0,-434.0,-294.0,-410.0,-294.0,-377.0,-295.0,-327.0,-291.0,-280.0,-289.0,-247.0,-289.0,-212.0,-289.0,-182.0,-291.0,-142.0,-296.0,-275.0,-296.0,-309.0,-304.0,-338.0,-304.0,-367.0,-306.0,-407.0,-309.0,-431.0,-310.0,-449.0,-313.0,-450.0,-310.0);              #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#213500",-409.0,-362.0,-384.0,-356.0,-350.0,-353.0,-307.0,-350.0,-238.0,-346.0,-191.0,-343.0,-146.0,-338.0,-106.0,-336.0,-82.0,-336.0,-115.0,-342.0,-142.0,-345.0,-186.0,-355.0,-221.0,-355.0,-254.0,-355.0,-291.0,-359.0,-342.0,-364.0,-381.0,-367.0,-413.0,-368.0);               #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#304312",-125.0,-380.0,-92.0,-372.0,-49.0,-368.0,-5.0,-364.0,41.0,-359.0,103.0,-358.0,157.0,-360.0,217.0,-349.0,284.0,-339.0,330.0,-336.0,402.0,-330.0,436.0,-336.0,396.0,-345.0,339.0,-348.0,291.0,-351.0,244.0,-359.0,193.0,-362.0,146.0,-365.0,115.0,-366.0,70.0,-366.0,26.0,-372.0,-14.0,-379.0,-48.0,-381.0,-95.0,-388.0,-118.0,-388.0,-141.0,-390.0,-153.0,-390.0);                   #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#658B1F",312.0,-158.0,329.0,-167.0,351.0,-183.0,394.0,-208.0,427.0,-237.0,440.0,-257.0,442.0,-167.0,385.0,-165.0,370.0,-164.0,342.0,-160.0,330.0,-160.0,316.0,-160.0,313.0,-160.0,304.0,-161.0);                    #CALL 'poly' function with the color and coordinates as arguments sent


def cloud():                #DEFINE 'cloud' function
    '''
    Function: cloud
    Description: makes the background clouds
    Variables: none
    Returns: None
    '''      
    #fadeaway
    poly("#497EF0",441.0,202.0,419.0,202.0,393.0,198.0,353.0,198.0,291.0,205.0,257.0,209.0,230.0,213.0,208.0,220.0,181.0,228.0,174.0,231.0,170.0,236.0,170.0,239.0,140.0,251.0,121.0,262.0,104.0,265.0,78.0,261.0,48.0,252.0,26.0,249.0,-16.0,243.0,-45.0,245.0,-69.0,252.0,-90.0,270.0,-111.0,281.0,-140.0,292.0,-161.0,293.0,-179.0,293.0,-199.0,306.0,-205.0,317.0,-213.0,332.0,-231.0,348.0,-242.0,361.0,-242.0,371.0,-229.0,382.0,-193.0,381.0,-186.0,386.0,-183.0,401.0,-198.0,424.0,-207.0,440.0,-214.0,450.0,-415.0,451.0,-444.0,450.0,-448.0,389.0,-449.0,354.0,-435.0,304.0,-426.0,252.0,-430.0,194.0,-428.0,161.0,-427.0,135.0,-434.0,115.0,-444.0,5.0,-451.0,22.0,-450.0,2.0,-448.0,-8.0,-448.0,-24.0,-323.0,-56.0,-121.0,-77.0,49.0,-92.0,194.0,-101.0,315.0,-113.0,397.0,-108.0,429.0,-111.0,443.0,-110.0,441.0,139.0,441.0,145.0,442.0,179.0);       #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#7FA4F3",-448.0,187.0,-440.0,187.0,-426.0,185.0,-413.0,182.0,-402.0,181.0,-385.0,176.0,-370.0,166.0,-347.0,150.0,-329.0,138.0,-296.0,126.0,-272.0,125.0,-248.0,119.0,-219.0,105.0,-188.0,97.0,-205.0,87.0,-261.0,98.0,-283.0,98.0,-296.0,95.0,-287.0,75.0,-260.0,63.0,-239.0,54.0,-213.0,45.0,-196.0,37.0,-171.0,34.0,-157.0,34.0,-140.0,37.0,-117.0,43.0,-83.0,52.0,-55.0,56.0,-33.0,58.0,-7.0,63.0,18.0,66.0,46.0,69.0,60.0,71.0,80.0,74.0,112.0,75.0,128.0,79.0,139.0,82.0,161.0,83.0,183.0,85.0,206.0,91.0,228.0,96.0,256.0,102.0,275.0,107.0,299.0,112.0,321.0,113.0,357.0,115.0,390.0,118.0,420.0,118.0,436.0,118.0,438.0,118.0,409.0,127.0,424.0,124.0,441.0,121.0,442.0,115.0,441.0,100.0,441.0,72.0,440.0,28.0,441.0,-26.0,441.0,-107.0,433.0,-119.0,370.0,-128.0,270.0,-133.0,142.0,-120.0,-58.0,-113.0,-200.0,-105.0,-307.0,-84.0,-381.0,-71.0,-425.0,-56.0,-448.0,-37.0,-445.0,-21.0,-440.0,-1.0,-450.0,25.0,-450.0,58.0,-448.0,88.0,-448.0,109.0,-449.0,128.0,-446.0,147.0,-443.0,162.0,-445.0,174.0,-446.0,180.0,-449.0,186.0);     #CALL 'poly' function with the color and coordinates as arguments sent


    poly("#4A78ED",-273.0,452.0,-260.0,444.0,-252.0,435.0,-241.0,429.0,-227.0,417.0,-212.0,407.0,-189.0,397.0,-166.0,386.0,-154.0,380.0,-144.0,374.0,-130.0,372.0,-137.0,365.0,-117.0,359.0,-102.0,355.0,-79.0,351.0,-48.0,344.0,-47.0,328.0,-28.0,308.0,-4.0,290.0,21.0,274.0,45.0,256.0,73.0,249.0,105.0,239.0,123.0,237.0,133.0,237.0,152.0,236.0,168.0,237.0,182.0,239.0,177.0,251.0,157.0,257.0,157.0,262.0,168.0,278.0,159.0,293.0,157.0,303.0,164.0,312.0,154.0,336.0,145.0,345.0,169.0,343.0,183.0,344.0,196.0,352.0,215.0,346.0,206.0,362.0,198.0,377.0,187.0,393.0,179.0,411.0,172.0,434.0,174.0,449.0,175.0,452.0);     #CALL 'poly' function with the color and coordinates as arguments sent


    poly("#F8F6F7",209.0,152.0,217.0,144.0,230.0,142.0,237.0,135.0,248.0,135.0,262.0,140.0,272.0,139.0,274.0,137.0,282.0,134.0,295.0,134.0,301.0,134.0,304.0,130.0,312.0,128.0,318.0,130.0,329.0,136.0,324.0,140.0,320.0,145.0,322.0,148.0,328.0,148.0,332.0,145.0,336.0,141.0,344.0,140.0,353.0,139.0,361.0,139.0,363.0,131.0,363.0,128.0,367.0,122.0,372.0,119.0,379.0,115.0,387.0,115.0,389.0,118.0,386.0,128.0,390.0,130.0,386.0,137.0,378.0,144.0,378.0,155.0,378.0,163.0,374.0,166.0,369.0,169.0,359.0,175.0,352.0,179.0,351.0,184.0,343.0,184.0,341.0,180.0,332.0,181.0,332.0,185.0,320.0,190.0,315.0,190.0,310.0,194.0,302.0,191.0,288.0,190.0,284.0,195.0,279.0,197.0,270.0,196.0,270.0,192.0,264.0,190.0,263.0,187.0,258.0,187.0,257.0,187.0,257.0,181.0,257.0,175.0,257.0,174.0,258.0,169.0,254.0,166.0,251.0,165.0,249.0,163.0,245.0,162.0,242.0,162.0,240.0,162.0,233.0,162.0,232.0,160.0,227.0,158.0,226.0,155.0,225.0,155.0,223.0,155.0,218.0,153.0,213.0,154.0,212.0,156.0,210.0,155.0);        #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#ABC1F4",209.0,153.0,214.0,154.0,225.0,152.0,229.0,155.0,229.0,149.0,240.0,147.0,244.0,142.0,248.0,142.0,259.0,146.0,265.0,150.0,271.0,156.0,277.0,150.0,282.0,144.0,288.0,143.0,300.0,143.0,304.0,145.0,308.0,146.0,311.0,154.0,315.0,154.0,320.0,158.0,327.0,157.0,336.0,157.0,340.0,162.0,347.0,167.0,352.0,167.0,357.0,166.0,365.0,164.0,378.0,162.0,377.0,153.0,379.0,151.0,379.0,146.0,380.0,150.0,380.0,156.0,388.0,156.0,392.0,149.0,397.0,147.0,407.0,145.0,409.0,143.0,406.0,129.0,392.0,131.0,392.0,124.0,391.0,122.0,382.0,118.0,380.0,112.0,373.0,116.0,365.0,125.0,365.0,127.0,359.0,132.0,355.0,136.0,353.0,137.0,347.0,139.0,341.0,140.0,337.0,143.0,335.0,146.0,325.0,147.0,320.0,147.0,328.0,136.0,328.0,132.0,318.0,130.0,309.0,126.0,302.0,126.0,297.0,132.0,287.0,133.0,272.0,134.0,260.0,135.0,258.0,141.0,245.0,137.0,234.0,136.0,230.0,138.0,226.0,142.0,219.0,145.0,211.0,148.0,207.0,153.0);                            #CALL 'poly' function with the color and coordinates as arguments sent

    poly("#F8F6F7",267.0,121.0,274.0,126.0,282.0,125.0,296.0,125.0,297.0,128.0,304.0,128.0,312.0,128.0,318.0,128.0,326.0,126.0,337.0,126.0,340.0,128.0,355.0,128.0,356.0,128.0,362.0,128.0,363.0,130.0,374.0,132.0,387.0,130.0,393.0,129.0,405.0,122.0,412.0,118.0,423.0,118.0,428.0,117.0,437.0,103.0,438.0,98.0,443.0,92.0,433.0,90.0,432.0,88.0,425.0,83.0,413.0,83.0,410.0,82.0,405.0,74.0,403.0,70.0,396.0,52.0,388.0,43.0,378.0,45.0,372.0,46.0,364.0,44.0,351.0,44.0,343.0,46.0,345.0,41.0,337.0,34.0,331.0,35.0,319.0,40.0,314.0,45.0,303.0,53.0,299.0,58.0,293.0,65.0,292.0,72.0,283.0,76.0,280.0,78.0,274.0,85.0,278.0,88.0,280.0,94.0,274.0,101.0,272.0,104.0,271.0,109.0,268.0,118.0,272.0,125.0,276.0,125.0,285.0,125.0,297.0,128.0,314.0,128.0,332.0,130.0,342.0,130.0,359.0,126.0,364.0,127.0);      #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#F8F6F7",197.0,116.0,212.0,116.0,216.0,112.0,220.0,103.0,228.0,94.0,235.0,95.0,241.0,84.0,247.0,80.0,250.0,68.0,249.0,58.0,242.0,53.0,228.0,58.0,222.0,60.0,217.0,56.0,222.0,53.0,220.0,51.0,213.0,51.0,206.0,51.0,204.0,52.0,200.0,52.0,199.0,52.0,196.0,53.0,191.0,58.0,190.0,68.0,183.0,70.0,177.0,74.0,174.0,84.0,176.0,95.0,181.0,100.0,190.0,102.0,189.0,113.0,194.0,115.0);    #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#B7CAFF",177.0,43.0,189.0,41.0,196.0,41.0,207.0,39.0,218.0,33.0,231.0,33.0,240.0,31.0,252.0,30.0,259.0,30.0,273.0,25.0,275.0,17.0,290.0,14.0,286.0,7.0,267.0,5.0,264.0,7.0,252.0,12.0,241.0,18.0,223.0,21.0,211.0,22.0,195.0,23.0,181.0,24.0,165.0,28.0,154.0,31.0,148.0,31.0,144.0,31.0,138.0,31.0,134.0,43.0,134.0,59.0,134.0,70.0,138.0,84.0,142.0,89.0,156.0,90.0,168.0,86.0,171.0,80.0,179.0,71.0,180.0,58.0,176.0,53.0,179.0,47.0,180.0,43.0);                                  #CALL 'poly' function with the color and coordinates as arguments sent

    poly("#93A9F3",33.0,294.0,42.0,285.0,49.0,284.0,63.0,282.0,65.0,282.0,78.0,274.0,91.0,271.0,100.0,265.0,116.0,260.0,123.0,249.0,131.0,247.0,135.0,245.0,153.0,242.0,163.0,242.0,174.0,242.0,182.0,245.0,171.0,251.0,157.0,257.0,150.0,262.0,145.0,267.0,143.0,272.0,141.0,276.0,136.0,281.0,132.0,283.0,126.0,284.0,121.0,286.0,121.0,290.0,116.0,300.0,110.0,304.0,103.0,313.0,96.0,313.0,87.0,313.0,82.0,315.0,76.0,318.0,65.0,325.0,56.0,332.0,51.0,332.0,48.0,334.0,39.0,340.0);        #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#B0C7FC",44.0,296.0,41.0,296.0,50.0,288.0,60.0,287.0,74.0,283.0,85.0,273.0,101.0,270.0,116.0,260.0,128.0,256.0,147.0,248.0,138.0,258.0,133.0,264.0,122.0,273.0,117.0,277.0,108.0,281.0,96.0,281.0,87.0,284.0,77.0,292.0,69.0,295.0,66.0,298.0,60.0,301.0,51.0,302.0,49.0,302.0,38.0,304.0);       #CALL 'poly' function with the color and coordinates as arguments sent

    poly("#93A9F3",94.0,302.0,94.0,309.0,92.0,313.0,90.0,321.0,94.0,322.0,108.0,318.0,118.0,314.0,127.0,314.0,132.0,315.0,145.0,318.0,154.0,323.0,153.0,327.0,141.0,335.0,139.0,339.0,134.0,343.0,130.0,347.0,128.0,351.0,131.0,356.0,142.0,358.0,149.0,354.0,155.0,353.0,161.0,353.0,161.0,358.0,151.0,363.0,148.0,365.0,142.0,369.0,137.0,377.0,127.0,384.0,119.0,392.0,114.0,399.0,111.0,405.0,118.0,409.0,130.0,406.0,138.0,403.0,149.0,395.0,155.0,391.0,168.0,382.0,157.0,372.0,164.0,373.0,180.0,368.0,184.0,364.0,188.0,366.0,184.0,375.0,184.0,382.0,177.0,388.0,170.0,396.0,169.0,401.0,166.0,403.0,162.0,405.0,159.0,409.0,154.0,413.0,149.0,417.0,145.0,419.0,148.0,421.0,143.0,427.0,140.0,430.0,139.0,436.0,144.0,444.0,147.0,447.0,147.0,450.0,118.0,450.0,67.0,449.0,40.0,448.0,-82.0,451.0,-137.0,449.0,-151.0,451.0,-170.0,451.0,-203.0,450.0,-193.0,442.0,-176.0,433.0,-166.0,430.0,-151.0,426.0,-145.0,419.0,-136.0,412.0,-130.0,404.0,-120.0,400.0,-110.0,394.0,-96.0,393.0,-86.0,394.0,-75.0,394.0,-59.0,392.0,-53.0,388.0,-48.0,380.0,-21.0,364.0,-20.0,357.0,-15.0,340.0,-11.0,332.0);      #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#B3CBFA",49.0,371.0,57.0,366.0,68.0,355.0,77.0,347.0,80.0,343.0,86.0,337.0,93.0,334.0,98.0,331.0,108.0,330.0,117.0,331.0,125.0,333.0,115.0,341.0,108.0,346.0,93.0,354.0,89.0,359.0,104.0,355.0,116.0,349.0,130.0,346.0,120.0,356.0,111.0,364.0,102.0,371.0,96.0,377.0,113.0,373.0,118.0,377.0,113.0,388.0,105.0,395.0,93.0,403.0,78.0,411.0,74.0,416.0,70.0,421.0,50.0,432.0,42.0,427.0,29.0,425.0,21.0,427.0,16.0,432.0,7.0,443.0,4.0,447.0,3.0,449.0,-11.0,449.0,-91.0,451.0,-108.0,449.0,-84.0,440.0,-76.0,435.0,-64.0,425.0,-47.0,414.0,-37.0,405.0,-19.0,396.0,-3.0,393.0,22.0,380.0);                               #CALL 'poly' function with the color and coordinates as arguments sent

    poly("#93ACFA",76.0,451.0,77.0,444.0,85.0,433.0,99.0,427.0,110.0,420.0,125.0,418.0,137.0,406.0,147.0,399.0,156.0,389.0,167.0,383.0,159.0,377.0,162.0,374.0,179.0,370.0,188.0,370.0,179.0,378.0,172.0,388.0,164.0,399.0,157.0,406.0,151.0,413.0,139.0,420.0,134.0,426.0,124.0,433.0,118.0,438.0,113.0,446.0,110.0,449.0,110.0,450.0);        #CALL 'poly' function with the color and coordinates as arguments sent

    poly("#C9E1FE",-262.0,254.0,-255.0,256.0,-251.0,264.0,-247.0,266.0,-238.0,266.0,-231.0,264.0,-227.0,251.0,-226.0,241.0,-217.0,234.0,-209.0,229.0,-203.0,221.0,-188.0,211.0,-182.0,205.0,-190.0,200.0,-204.0,205.0,-209.0,214.0,-212.0,219.0,-215.0,221.0,-223.0,225.0,-230.0,230.0,-237.0,232.0,-239.0,233.0,-244.0,241.0,-248.0,239.0,-256.0,235.0,-259.0,235.0,-262.0,239.0,-269.0,240.0,-280.0,240.0,-283.0,246.0,-270.0,253.0,-262.0,255.0);    #CALL 'poly' function with the color and coordinates as arguments sent

    poly("#D6DBEE",-288.0,247.0,-291.0,247.0,-297.0,249.0,-300.0,249.0,-302.0,251.0,-304.0,253.0,-309.0,256.0,-316.0,257.0,-318.0,257.0,-320.0,257.0,-324.0,255.0,-329.0,254.0,-332.0,254.0,-334.0,253.0,-334.0,252.0,-333.0,252.0,-334.0,252.0,-334.0,252.0,-336.0,255.0,-339.0,256.0,-340.0,258.0,-345.0,258.0,-346.0,258.0,-349.0,257.0,-350.0,255.0,-355.0,255.0,-357.0,251.0,-355.0,249.0,-352.0,248.0,-350.0,244.0,-346.0,242.0,-343.0,240.0,-340.0,237.0,-338.0,237.0,-335.0,237.0,-332.0,237.0,-319.0,237.0,-319.0,238.0,-316.0,239.0,-307.0,240.0,-306.0,240.0,-292.0,240.0,-292.0,240.0,-289.0,243.0,-289.0,244.0,-289.0,244.0,-291.0,245.0);     #CALL 'poly' function with the color and coordinates as arguments sent


    poly("#A7C9FF",-448.0,134.0,-445.0,131.0,-434.0,129.0,-428.0,128.0,-423.0,127.0,-427.0,125.0,-430.0,123.0,-427.0,118.0,-414.0,116.0,-405.0,114.0,-399.0,111.0,-392.0,109.0,-392.0,103.0,-391.0,99.0,-377.0,92.0,-365.0,89.0,-353.0,84.0,-338.0,82.0,-328.0,87.0,-333.0,91.0,-343.0,93.0,-347.0,95.0,-336.0,97.0,-328.0,101.0,-320.0,103.0,-315.0,108.0,-320.0,112.0,-330.0,113.0,-333.0,113.0,-332.0,116.0,-330.0,122.0,-339.0,125.0,-347.0,126.0,-343.0,132.0,-334.0,139.0,-337.0,144.0,-346.0,146.0,-350.0,150.0,-361.0,155.0,-364.0,157.0,-363.0,165.0,-364.0,168.0,-376.0,168.0,-384.0,167.0,-407.0,166.0,-411.0,167.0,-435.0,171.0,-443.0,174.0,-451.0,179.0);         #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#E6F0F6",-401.0,109.0,-389.0,108.0,-382.0,108.0,-372.0,110.0,-366.0,112.0,-363.0,116.0,-355.0,123.0,-354.0,126.0,-354.0,129.0,-354.0,133.0,-345.0,137.0,-341.0,137.0,-338.0,139.0,-340.0,143.0,-346.0,143.0,-351.0,142.0,-356.0,140.0,-359.0,143.0,-362.0,145.0,-366.0,146.0,-371.0,149.0,-378.0,149.0,-381.0,149.0,-386.0,149.0,-398.0,150.0,-399.0,150.0,-401.0,153.0,-405.0,156.0,-409.0,157.0,-413.0,158.0,-419.0,162.0,-430.0,164.0,-439.0,166.0,-446.0,169.0,-448.0,169.0,-448.0,167.0,-448.0,162.0,-448.0,158.0,-447.0,151.0,-447.0,145.0,-446.0,145.0,-439.0,145.0,-434.0,143.0,-427.0,142.0,-425.0,140.0,-422.0,133.0,-422.0,129.0,-417.0,121.0,-416.0,118.0,-410.0,113.0,-400.0,111.0);    #CALL 'poly' function with the color and coordinates as arguments sent

    #bottom cloud
    poly("#F3EFF7",-284.0,-8.0,-284.0,-8.0,-278.0,-6.0,-274.0,-6.0,-257.0,-5.0,-255.0,-5.0,-243.0,-6.0,-227.0,-8.0,-216.0,-8.0,-205.0,-8.0,-195.0,-7.0,-192.0,-7.0,-183.0,-5.0,-177.0,-5.0,-168.0,-0.0,-161.0,-2.0,-152.0,-6.0,-149.0,-6.0,-139.0,-10.0,-131.0,-13.0,-127.0,-21.0,-135.0,-21.0,-140.0,-21.0,-146.0,-21.0,-162.0,-22.0,-167.0,-22.0,-182.0,-20.0,-191.0,-19.0,-197.0,-17.0,-206.0,-15.0,-222.0,-15.0,-237.0,-16.0,-246.0,-16.0,-267.0,-12.0,-284.0,-10.0,-293.0,-7.0,-299.0,-4.0);       #CALL 'poly' function with the color and coordinates as arguments sent

    #top right

    poly("#7295FB",250.0,449.0,247.0,445.0,246.0,443.0,233.0,436.0,219.0,427.0,220.0,415.0,230.0,403.0,252.0,402.0,267.0,413.0,268.0,424.0,283.0,424.0,291.0,425.0,305.0,424.0,305.0,414.0,310.0,401.0,325.0,399.0,341.0,399.0,359.0,403.0,358.0,414.0,368.0,421.0,384.0,420.0,393.0,425.0,400.0,415.0,399.0,405.0,389.0,400.0,374.0,400.0,364.0,397.0,362.0,391.0,356.0,386.0,347.0,382.0,338.0,379.0,334.0,370.0,353.0,371.0,356.0,362.0,343.0,362.0,333.0,356.0,343.0,336.0,367.0,338.0,378.0,323.0,396.0,313.0,415.0,310.0,435.0,306.0,445.0,318.0,445.0,333.0,441.0,346.0,440.0,364.0,440.0,382.0,445.0,405.0,441.0,441.0,418.0,449.0,377.0,447.0,344.0,445.0,297.0,445.0,266.0,444.0,244.0,445.0,236.0,445.0);        #CALL 'poly' function with the color and coordinates as arguments sent
    poly("#E5EBF4",245.0,447.0,247.0,443.0,247.0,440.0,238.0,434.0,231.0,427.0,229.0,416.0,235.0,408.0,249.0,407.0,264.0,407.0,268.0,419.0,258.0,427.0,263.0,428.0,274.0,429.0,287.0,429.0,299.0,431.0,308.0,427.0,323.0,426.0,328.0,424.0,344.0,423.0,359.0,427.0,370.0,433.0,381.0,435.0,395.0,433.0,403.0,423.0,410.0,404.0,395.0,403.0,377.0,407.0,354.0,402.0,358.0,391.0,366.0,387.0,379.0,389.0,394.0,389.0,400.0,376.0,393.0,365.0,383.0,361.0,368.0,360.0,358.0,352.0,359.0,342.0,373.0,337.0,389.0,337.0,398.0,327.0,411.0,316.0,425.0,309.0,432.0,310.0,445.0,314.0,441.0,449.0,436.0,449.0,417.0,449.0,398.0,449.0,383.0,449.0,345.0,449.0,328.0,449.0,301.0,449.0,282.0,449.0,256.0,450.0,239.0,450.0);        #CALL 'poly' function with the color and coordinates as arguments sent

def border():           #DEFINE 'border' function
    '''
    Function: border
    Description: makes the border of the program in case you go full screen (blocks out the impurities off screen)
    Variables: none
    Returns: None
    '''     
    poly("black",-445.0,499.0,-452.0,-441.0,459.0,-446.0,446.0,497.0,946.0,498.0,949.0,-483.0,-956.0,-487.0,-958.0,503.0);        #CALL 'poly' function with the color and coordinates as arguments sent
def background():       #DEFINE 'background' function
    '''
    Function: background 
    Description: calls the background functions
    Variables: none
    Returns: None
    '''     
    cloud();            #CALL 'cloud' function
    hillShape();        #CALL 'hillShape' function
    chair();            #CALL 'chair' function
    border();           #CALL 'border' function
    t.goto(76.0,365.0); #goes to the specified coordinate
    t.write("passport photo pose", font=("Arial", 12, "normal"));      #writes text
    
def main():             #DEFINE 'main' function
    '''
    Function: main
    Description: calls all the important functions
    Variables: none
    Returns: None
    '''  
    background();       #CALL 'background' function
    me();               #CALL 'me' function




main();                 #CALL 'main' function
t.done();
