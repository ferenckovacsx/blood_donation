from donor_register import donor_register_get_user_data
from donation_event_register import donation_event_reg
from datetime import datetime
from time import sleep
from donor_class import Donor
from event_class import DonationEvent
import os

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
        print(donor_datas.__repr__())
        sleep(15)
        os.system('cls' if os.name == 'nt' else 'clear')



    elif Answer == "2":
        donation_event_actual = DonationEvent()
        donation_event_actual.date_of_event_string = donation_event_reg.get_date_of_event_string()
        donation_event_actual.donation_start_time = donation_event_reg.get_donation_start_time()
        donation_event_actual.donation_end_time = donation_event_reg.get_donation_end_time()
        donation_event_actual.address = donation_event_reg.get_address()
        donation_event_actual.zip_code = donation_event_reg.get_zip_code()
        donation_event_actual.city = donation_event_reg.get_city()
        donation_event_actual.bed_count = donation_event_reg.get_bed_count()
        donation_event_actual.donor_number = donation_event_reg.get_planned_donor_number()
        if donation_event_actual.check_min_period and donation_event_actual.not_weekend():
            donation_event_actual.actual_donor_number = input("How many succesful donation was?")
            print(donation_event_actual.get_donation_success_rate())
            sleep(5)
    elif Answer == "x":
        Switch = False
    else:
        print("Answer invalid.")