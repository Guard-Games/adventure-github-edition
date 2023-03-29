answer = input("do you want to play (yes/no) ?")

if answer.lower().strip() == "yes":

    answer = input("you reach a crossroads, do you want to go left or right? ").lower().strip()
    if answer == "left":
        answer = input("you encounter a monster, do you want to fight or run? ").lower().strip()

        if answer == "fight":
            print("the monster fights back and kills you (bad ending 1) ")

        elif answer == "run":
            answer = input("do you want to go into the forest?(yes/no) ")

            if answer == "yes":
                print("you got lost and drowned in the river (bad ending 2) ")
            elif answer == "no":
                answer = input("you see a town nearby, do you want to go there (yes/no) ")

                if answer == "yes":
                    print("you decided to live here(good ending 1) ")
                elif answer == "no":
                    answer = input("you decided to go on the opposite path, but suddenly you see a bear, do you want do fight or run" )
                    

    elif answer == "right":
        print("you fall off a cliff and die (bad ending 3) ")

    else:
        print("you lost" )

else:
    print("bye!" )