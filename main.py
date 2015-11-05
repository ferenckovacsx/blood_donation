from donor_register import donor_register_get_user_data
from donation_event_register import donation_event_reg
from datetime import datetime
from time import sleep
from donor_class import Donor
import os

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
        donor_datas = Donor()
        donor_datas.name = donor_register_get_user_data.get_name_string()
        donor_datas.weight = donor_register_get_user_data.get_weight_string()
        donor_datas.gender = donor_register_get_user_data.get_gender_string()
        donor_datas.birth_date = donor_register_get_user_data.get_birth_date()
        donor_datas.last_donation = donor_register_get_user_data.get_last_donation_date()
        donor_datas.was_sick_last_month = donor_register_get_user_data.get_sick_response_string()
        donor_datas.identifier = donor_register_get_user_data.get_unique_indentifier_string()
        donor_datas.id_expire = donor_register_get_user_data.get_id_expiration_date()
        donor_datas.blood_type = donor_register_get_user_data.get_donor_blood_type_string()
        donor_datas.e_mail = donor_register_get_user_data.get_email_string()
        donor_datas.mobile_number = donor_register_get_user_data.get_mobile_string()
        if donor_datas.check_age() and donor_datas.check_weight() and donor_datas.check_id_expiration() \
            and donor_datas.check_last_donation() and donor_datas.check_hemoglobin():
            print(donor_datas.__repr__())
            sleep(10)
            os.system('cls' if os.name == 'nt' else 'clear')



    elif Answer == "2":
        pass
    elif Answer == "x":
        Switch = False
    else:
        print("Answer invalid.")