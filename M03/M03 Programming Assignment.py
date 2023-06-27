#7.4
things = ["mozzarella","cinderella","salmonella"]
#7.5
things[1] = "Cinderella"
print(things[1])
#it does change the element

#7.6
things[0] = things[0].upper()
print(things[0])

#7.7
del things[2]
print(things)

#9.1
def good():
    return ["Harry","Ron","Hermione"]

#9.2
def get_odds():
    oddsFound = 0
    oddsList = []
    for x in range(10):
        if (x % 2 ==1):
            oddsList.append(x)
            oddsFound+=1
            if(oddsFound==3):
                print(x)
    return oddsList
print(get_odds())