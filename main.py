from donor_register import donor_register_get_user_data
from donation_event_register import donation_event_reg
from datetime import datetime
from time import sleep

TODAY = datetime.today()
Switch = True

while Switch:
    print("""
    1 = donor registration
    2 = donor event registration
    x = exit
    """)
    Answer = input("Answer: ")
    if Answer == "1":
        pass
    elif Answer == "2":
        pass
    elif Answer == "x":
        Switch = False
    else:
        print("Answer invalid.")