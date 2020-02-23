import time
import random



print("This is a dice simulator. ",
"This is a 6 sided dice")

roll = input("If you want to roll, type roll")

if roll == "roll":
    time.sleep(1)

    number = random.randint(1, 6)
    time.sleep(1)

    if number == 1:

        die1_display = ["",
                        "   _______________________    " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |                     |  " ,
                        "   |          O          | " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |_____________________|  " ,
            ]      
        print("\n".join(die1_display[0 : len(die1_display)]))
        print("\n")

    if number == 2:

        die2_display = ["",
                        "   _______________________    " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |              O      | " ,
                        "   |                     |  " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |      O              | " ,
                        "   |                     | " ,
                        "   |_____________________|  " ,
            ]      
        print("\n".join(die2_display[0 : len(die2_display)]))
        print("\n")

    if number == 3:

        die3_display = ["",
                        "   _______________________    " ,
                        "   |                     | " ,
                        "   |                 O   | " ,
                        "   |                     | " ,
                        "   |                     |  " ,
                        "   |          O          | " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |   O                 | " ,
                        "   |_____________________|  " ,
            ]      
        print("\n".join(die3_display[0 : len(die3_display)]))
        print("\n")
        
    if number == 4:

        die4_display = ["",
                        "   _______________________    " ,
                        "   |                     | " ,
                        "   |    O            O   | " ,
                        "   |                     | " ,
                        "   |                     |  " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |    O            O   | " ,
                        "   |_____________________|  " ,
            ]      
        print("\n".join(die4_display[0 : len(die4_display)]))
        print("\n")

    if number == 5:

        die5_display = ["",
                        "   _______________________    " ,
                        "   |                     | " ,
                        "   |   O             O   | " ,
                        "   |                     | " ,
                        "   |                     |  " ,
                        "   |          O          | " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |   O             O   | " ,
                        "   |_____________________|  " ,
            ]      
        print("\n".join(die5_display[0 : len(die5_display)]))
        print("\n")

    if number ==6:

        die6_display = ["",
                        "   _______________________    " ,
                        "   |                     | " ,
                        "   |   O              O  | " ,
                        "   |                     | " ,
                        "   |                     |  " ,
                        "   |   O              O  | " ,
                        "   |                     | " ,
                        "   |                     | " ,
                        "   |   O              O  | " ,
                        "   |_____________________|  " ,
            ]      
        print("\n".join(die6_display[0 : len(die6_display)]))
        print("\n")
        

    

        

        

        
