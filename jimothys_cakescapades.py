# Jimothy's Cake-scapades

# At the top of the file are declarations and variables we need.
#
# Scroll to the bottom and look for the main() function, that is
# where the program logic starts.

# an object describing our player
player = {
        "name" : "Jimothy",
        "location" : "Familyden",
        "spine" : "short",
        "items" : ["coin"],
        "friends" : [],
        "score" : 0
}

rooms = {
        "familyDen" : "Jimothy's family den",
        "rooftop" : "rooftop",
        "stormDrain" : "storm drain",
}

items = {
        "coin" : "Shiny coin",
        "birthdayCake" : "Birthday cake",
        "soggyCake" : "Soggy cake",
        "halfCake" : "Half a cake"
}

friends = {
        "carl" : "Carl"
}

def printGraphic(name):
        if (name == "title"):
                print ('       _ _                 _   _           _                              ')
                print ('      | (_)               | | | |         ( )                             ')
                print ('      | |_ _ __ ____  ___ | |_| |__  _   _|/ ___                          ')
                print ('  _   | | | |_   _  l/ _ l| __| |_ l| | | | / __|                         ')
                print (' | |__| | | | | | | | (_) | |_| | | | |_| | l__ l                         ')
                print (' l_____/|_|_| |_| |_|l___/l___|_| |_|l__, | |___/                         ')
                print (' / ____|    | |                      __/ /                | |             ')
                print ('| |      ___| | _____ ______ ___  __|___/_ _ ___  __ _  __| | ___  ___    ')
                print ('| |    / _` | |/ / _ l______/ __|/ __/ _` |  _  l/ _` |/ _` |/ _ l/ __|   ')
                print ('| |___ |(_| |   <  __/      l__ l (_| (_| | |_) | (_| | (_| |  __/l__ l   ')
                print ('l______l__,_|_|l_l___|      |___/l___l__,_| .__/ l__,_|l__,_|l___||___/   ')
                print ('                                           | |                            ')
                print ('                                           |_|                            ')
                print ('                                                                          ')



        
        if (name == "jimothy"):
                print ('              .-.-.         ')
                print ('     _(l-/)_" ,.  ,l  .-.   ')
                print ('    {((O^O))} ../, ,|/__|   ')
                print ('    `-.(Y).-` , | , |-.-`   ')
                print ('       l-//-l,_. l l`       ')
                print ('       ////    / /l l       ')
                print ('     ==`==`   ==`   ==`     ')
                print ('                            ')
                print ('          Jimothy           ')

        if (name == "carl"):
                print ('     ___        ')
                print ('    |* *|       ')
                print ('    / V l       ')
                print ('   (/   l)      ')
                print ('  ==="="=====<  ')
                print ('     UUU        ')
                print ('                ')
                print ('     Carl       ')

        if (name == "birthdayCake"):
                print ('                         ')
                print ('       $ $ $ $ $ $       ')
                print ('     __|_|_|_|_|_|__     ')
                print ('    | * * * * * * * |    ')
                print ('    |---------------|    ')
                print ('    | * * * * * * * |    ')
                print ('    |===============|    ')
                print ('                         ')
                print ('      birthday cake      ')

        if (name == "garbageCan"):
                print ('                       ')
                print ('      ____.-.____      ')
                print ('     [___________]     ')
                print ('    (d|||||||||||b)    ')
                print ('     `|||||||||||`     ')
                print ('      |||||||||||      ')
                print ('      |||||||||||      ')
                print ('      |||||||||||      ')
                print ('      |||||||||||      ')
                print ('      [---------]      ')
                print ('                       ')
                print ('  Brendas Garbage Can  ')

        if (name == "rainstorm"):
                print ('                      ')
                print ('      _________       ')
                print ('     ( _    -  )_     ')
                print ('    (_   _   -  _)    ')
                print ('     (_________)      ')
                print ('     / / / / /        ')
                print ('    / / / / /         ')
                print ('                      ')
                print ('      rainstorm       ')
        
        if (name == "coin"):
                print ('           ______           ')
                print ('        .-`      `-.        ')
                print ('      .`    .-.     `.      ')
                print ('     /     /   l      l     ')
                print ('    |      l    `>     |    ')
                print ('    | ""   / `._)      |    ')
                print ('     l    /   l 2000  /     ')
                print ('      `. /     |    _/      ')
                print ('        `-. ____ - `        ')
                print ('                            ')
                print ('         shiny coin         ')


def introStory():
        # introducing Jimothy and the reason for his mission
        input("Start >")
        print ("")
        print ("Welcome to Jimothy's Family Den!")
        printGraphic("jimothy")
        print ("")
        input("next >")
        print ("")
        print ("Jimothy and his family are very close. Now that Jimothy is older,")
        print ("he is excited to be able to scrounge up food to bring back to the den.")
        print ("")
        input("next >")
        print ("")
        print ("Jimothy carries a lucky coin around. He believes it brings him good fortune.")
        print ("One afternoon while scampering across a fence, Jimothy came across a backyard party")
        print ("for Brenda's 40th.")
        print ("")
        input("next >")
        print ("")
        print ("Jimothy watched and for some reason, nobody ate any cake! Jimothy watched Brenda")
        print ("throw her birthday cake in the garbage after everyone left. What a waste!")
        print ("")
        print ("Jimothy decided that later tonight, he would stage a cake heist.")
        print ("")
        input("next >")
        print ("")
        print ("Later that night a storm rolls in...")
        print ("")
        printGraphic("rainstorm")
        print ("")
        input("next >")
        print ("")
        print ("Jimothy is still determined. He has two routes to get to the garbage")
        print ("bin with the cake.")
        print ("")
        print ("Should he:")
        print ("1. Run across the rooftops")
        print ("2. Scurry through the storm drain")
        print ("")
        while True:
            print ("options: [ 1 , 2 ]")
            print ("")
        
            pcmd = input(">")

            #the player can chose rooftops or storm drain
            if (pcmd == "1"):
                print ("Jimothy decides to take the rooftops.")
                print ("")
                input("To the roof >")
                rooftops()
                break
        
            elif (pcmd == "2"):
                print ("Jimothy decides to scurry through the storm drain")
                print ("")
                input("Down below the ground >")
                stormDrain()
                break
        
            # option 3: error
            else:
                print ("")
                print ("Jimothy doesn't know how to do that. Try again.")
                print ("")
            

def rooftops():
        print ("Jimothy begins his trek across several roofs to get to Brenda's house.")
        print ("")
        input("next >")
        print ("")
        printGraphic("carl")
        print ("")
        print ("Uh oh. It's Carl the crow. Jimothy stole a french fry from last spring,")
        print ("and a crow never forgets a face.")
        print ("What to do... what to do...")
        print ("")
        print ("Should he:")
        print ("1. Try to sneak past Carl")
        print ("2. Give Carl Jimothy's shiny coin")
        print ("3. Go back home")
        while True:
            print ("options: [ 1 , 2 , 3 ]")
            print ("")
        
            pcmd = input(">")

            # option 1: try to sneak past
            if (pcmd == "1"):
                print ("Jimothy tries to tip-toe past his enemy, Carl.")
                print ("But Carl hears his unique stride bumbling across the roof.")
                printGraphic("carl")
                print ("HEY. I know you! You're the raccoom who stole my french fry!")
                print ("")
                input("next >")
                print ("")
                print ("Carl let's out a loud crackle and suddenly a murder of crows appears.")
                print ("Jimothy spends the rest of the night huddled behind the garbage can")
                print ("until morning when the garbage truck came and scared the crows away...")
                print ("but also took the cake.")
                print ("")
                input("Game Over >")
                print ("")
                gameOver()
                break
        
            # option 2: give Carl your shiny coin
            elif (pcmd == "2"):
                print ("Jimothy remembers that crows love shiny things.")
                print ("He pulls out his shiny coin and offers it to Carl.")
                printGraphic("coin")
                player["items"].remove("coin")
                print ("")
                input("next >")
                print ("")
                print ("Carl initially looked furious to see Jimothy, but was quickly distracted")
                print ("by the shiny coin in Jimothy's hands.")
                print ("")
                input("next >")
                print ("")
                print ("Jimothy gives Carl the coin and Carl is excited and grateful. Now they are friends.")
                player["friends"].append("carl") # for adding a friend
                player["score"] += 100 # for making a friend
                print ("")
                input("next >")
                print ("")
                print ("Jimothy tells Carl about his plans to open the garbage bin,")
                print ("and now that Jimothy and Carl are friends, Carl offers to help.")
                print ("")
                input("next >")
                print ("")
                printGraphic("garbageCan")
                print ("")
                print ("There is a bungee strap attached to the bin, and Carl and Jimothy")
                print ("work together to quietly get the lid off.")
                print ("")
                input("next >")
                print ("")
                printGraphic("birthdayCake")
                print ("Success! But it's big...")
                print ("Jimothy could offer half to Carl, or try to haul the whole thing home.")
                print ("")
                while True:
                    print ("options: [ Half , Whole ]")
                    print ("")
                    pcmd = input(">")
                    print ("")

                    if (pcmd == "Half"):
                        print ("Jimothy decides to offer half to Carl. they become partners, and Carl")
                        print ("flies by Jimothy's Den anytime there's a birthday in the neighborhood.")
                        player["score"] += 50 # bonus for building a partnership
                        player["items"].append("halfCake")
                        print ("")
                        input("next >")
                        print ("")
                        print ("Jimothy scurries home with his half of the cake and tells his family all")
                        print ("about his plot with Carl. They stuff their faces and go to sleep fat and happy.")
                        print ("")
                        input("Game Over >")
                        print ("")
                        gameOver()
                        break

                    elif (pcmd == "Whole"):
                        print ("Jimothy decides to try to drag the entire cake home.")
                        print ("As he drags it across rooftops it soaks up a lot of rain.")
                        print ("")
                        input("next >")
                        print ("")
                        print ("Jimothy arrives at his den with a big soggy cake.")
                        player["score"] += 50 # for bringing home a soggy cake
                        player["items"].append("soggyCake")
                        print ("His family is still stoked, and the soggy cake is still delicious.")
                        print ("")
                        input("Game Over >")
                        print ("")
                        gameOver()
                        break
                
                    # option 3: error
                    else:
                        print ("")
                        print ("Jimothy doesn't know how to do that. Try again.")
                        print ("")

            # option 3: go back home
            elif (pcmd == "3"):
                print ("Jimothy goes back home with his short soggy tail tucked between his legs.")
                print ("His family goes to sleep hungry.")
                print ("")
                input("Game Over >")
                print ("")
                gameOver()
                break
        
            # option 4: error
            else:
                print ("")
                print ("Jimothy doesn't know how to do that. Try again.")
                print ("")
                    
def stormDrain ():
        print ("Jimothy scurries through the storm drain and pops out right next to the garbage can.")
        printGraphic("garbageCan")
        print ("")
        input("next >")
        print ("")
        print ("He notices that the lid is held down with a bungee cord.")
        print ("Raccoons are known for craftiness and problem solving.")
        print ("")
        print ("What's the best way to get the lid off?")
        print ("Should he tip it over or work patiently to get the stap off")
        print ("")
        print ("1. Tip it over")
        print ("2. Work the bungee strap off")
        print ("")
        while True:
            print ("options: [ 1 , 2 ]")
            print ("")
            pcmd = input(">")
            print ("")
        
            # option 1 to tip it over
            if (pcmd == "1"):
                print ("Jimothy tips the can over and the lid pops off.")
                print ("But all the comotion woke up Brenda, who's furious.")
                print ("")
                input("next >")
                print ("")
                print ("Jimothy runs away with his short tail tucked between his legs.")
                print ("Jimothy's family goes to sleep hungry.")
                print ("")
                input("game over >")
                print ("")
                gameOver()
                break
            
            # option 2 to work the strap off
            elif (pcmd == "2"):
                print ("Jimothy decides to patiently work the bungee strap off.")
                print ("")
                input("next >")
                print ("")
                print ("His patience pays off! Jimothy collects the cake from the can.")
                printGraphic("birthdayCake")
                player["items"].append("birthdayCake")
                print ("")
                input("next >")
                print ("")
                print ("Jimothy starts heading home with the cake, but comes across a puddle.")
                print ("Raccoons have an urge to wash their food before they eat it.")
                print ("")
                print ("It could be nice for his family. Should Jimothy stop and wash his cake?")
                print ("")
                print ("1. Wash the cake")
                print ("2. Hurry home")
                while True:
                    print ("options: [ 1 , 2 ]")
                    print ("")
                    pcmd = input(">")
                    print ("")

                    # option 1 to wash the cake
                    if (pcmd == "1"):
                        print ("Jimothy starts rinsing his cake in a nearby puddle.")
                        print ("The cake disolves in the water and Jimothy can't salvage the cake.")
                        player["items"].remove("birthdayCake")
                        print ("")
                        input("next >")
                        print ("")
                        print ("Jimothy runs home with his short tail tucked between his legs.")
                        print ("Jimothy's family goes to sleep hungry.")
                        print ("")
                        input("game over >")
                        print ("")
                        gameOver()
                        break

                    # option 2 to hurry home
                    elif (pcmd == "2"):
                        print ("Jimothy decides it's not worth it and just wants to get the cake home.")
                        print ("")
                        input("next >")
                        print ("")
                        print ("When he arrives in the family den, his whole family celebrates.")
                        print ("Jimothy is the hero of the day and his family goes to sleep fat and happy.")
                        player["score"] += 100 # for bringing home the whole cake
                        print ("")
                        input("game over >")
                        print ("")
                        gameOver()
                        break
        
                    # option 3: error
                    else:
                        print ("")
                        print ("Jimothy doesn't know how to do that. Try again.")
                        print ("")
    
            # option 3: error
                else:
                    print ("")
                    print ("Jimothy doesn't know how to do that. Try again.")
                    print ("")


def gameOver():

    printGraphic("Jimothy")

    print("-------------------------------")
    print("Game Over")
    print("Jimothy's score:" )
    print( "Score: " + str(player["score"]) ) # customized with a score
    print( "Items: " + str(player["items"]) )
    print( "Friends: " + str(player["friends"]) )
    exit()
    

# Program start with this.
def main():
    printGraphic("title") # call the function to print an image
    introStory() # start the intro

main() # this is the first thing that happens

