#ToDoList
#George Lefebvre
#Mr. J APCSP
#1/11/2024

#initialize
list = []

#Functions
def addtask():

    newtask = input("What task would you like to add to your list?")
    list.append(newtask)
    print("Your new list is" + str(list))
def viewlist():
    print("Your current list is" + str(list))
def removetask():
    notask = input("What task would you like to remove?")
    list.remove(notask)
    print("Your new list is" + str(list))
def quitprogram():
    print("Thank you for using this platform.")
    
def completetask(whichelement):
    list.index(whichelement)
def removeall():   
    list.clear()
    print("Your list has been cleared.")
def alphasort():
    list.sort()
    print("Your new list is" + str(list))
def countlist():
    print("The number of items in your current list is " + len(list))


def run():
    add = str(input("Would you like to add a task to your list?"))
    if (add == "yes"):
        addtask()
        run()
    elif (add == "no"):
        remove = str(input("Would you like to remove a task from your list?"))
        if (remove == "yes"):
            removetask()
            run()
        elif (remove == "no"):
            view = str(input("Would you like to view your list?"))
            if (view == "yes"):
                viewlist()
                run()
            elif (view == "no"):
                complete = input("Would you like to cross off any of the items on your list?")
                if (complete == "yes"):
                    whichelement = input("Which list item would you like to change? Specify which string index.")
                    list[int(whichelement) - 1] = (str((list[int(whichelement) - 1]) + " X"))
                    print("Your new list is" + str(list))
                elif (complete == "no"):
                    ca = input("Would you like to clear your entire list?")
                    if (ca == "yes"):
                        removeall()
                        run()
                    elif (ca == "no"):
                        wantsort = input("Would you like to sort your list alphabetically?")
                        if (wantsort == "yes"):
                            alphasort()
                            run()
                        elif (wantsort == "no"):
                            wantlength = input("Would you like to know how many items are on your list?")
                            if (wantlength == "yes"):
                                countlist()
                                run()
                            elif (wantlength == "no"):
                                quit = input("Would you like to quit the program?")
                                if (quit == "yes"):
                                    quitprogram()
                                elif (quit == "no"):
                                    run()
                                    



                

def todos():
    print("Welcome to your list generator! Select an option to start.")
    run()
    
        
        
#Main
todos()