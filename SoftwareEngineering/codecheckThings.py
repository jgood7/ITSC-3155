def main():
    colors = {"red", "orange", "blue", "green"}
    if inRainbow(colors):
        print("yes")
    else:
        print("no")
    
def inRainbow(colors):
    rainbow = ("red","orange","yellow","green","blue","indigo","violet")
    for each in colors:
        if rainbow.__contains__(each):
            next
        else:
            return False
        return True

def probTwo():
    basket1 = {"apples","oranges","grapes"}
    basket2 = {"blueberries","pears","apples","oranges","lemons"}
    basket3 = {"bananas","lemons","grapes","apples"}

    fruit = basket1.union(basket2).difference(basket3)
    print(fruit)
    return True

def probThree():
    inputStr = input("Enter a text string: ")
    text = inputStr.upper()

# TODO: define a set named notUsed that contains the letters of
# the alphabet that are not contained in the user entered string.
    notUsed = {"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"}
    notUsed = notUsed.difference(list(text))
    for element in sorted(notUsed) :
        print(element, end="")
    print()

def probFour():
    periodicTable = {
   "H": "Hydrogen", "C": "Carbon", "O": "Oxygen",
   "Fe": "Iron", "Au": "Gold", "Na": "Sodium",
   "Ag": "Silver", "Pb": "Lead", "Pu": "Plutonimum"
}

# Use the prompt "Enter symbol (or Q to quit): "
# Print either "Invalid symbol." if an error occurs
# or "element = element name" ("%s = %s")

    element = input("Enter symbol (or Q to quit): ")
    while element!="Q":
        found = False
        for x in periodicTable:
            if element==x:
                found = True
                print(x,"=",periodicTable[x])
        if found==False:
            print("Invalid symbol")
        element = input("Enter symbol (or Q to quit): ")
    return 0


probFour()

