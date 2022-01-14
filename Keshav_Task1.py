print("...................................................................................\n")
print("                  Stop! Who would cross the Bridge of Death                          ")
print("        Must answer me these questions three, 'ere the other side he see.          \n")
print("...................................................................................\n")

Entry=input("What is your name?\n")

if("Arthur" in Entry or "arthur" in Entry):
    #It check the arthur in Entry or not
    print("My liege! You may pass!")
else:
    quest=input("What is your quest?\n")
    if ('Grail' in quest)|("grail" in quest):  
        #It check grail in quest or not  
        color=input("What is your favourite colour?\n")
        #Using else if statement and checking the first character of name and color
        if (color[0]==Entry[0]):
            print("You may pass!")
        else:
            print("Incorrect! You must now face the Gorge of Eternal Peril.")    
    else:
        print("Only those who seek the Grail may pass.")