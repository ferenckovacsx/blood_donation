from datetime import datetime


def get_date_of_event_string():
    date_of_event_string = ""
    while date_of_event_string == "":
        date_of_event_string = input("Enter date of event (YYYY.MM.DD): ")
        try:
            datetime.strptime(date_of_event_string, '%Y.%m.%d')
        except:
            print("Incorrect date. Please try again")
    return date_of_event_string


def get_donation_start_time():
    donation_start_time = ""
    while donation_start_time == "":
        donation_start_time = input("Enter the start time of the donation: ")
    return donation_start_time


def get_donation_end_time():
    donation_end_time = ""
    while donation_end_time == "":
        donation_end_time = input("Enter the end time of the donation: ")
    return donation_end_time


def get_zip_code():
    zip_code = ""
    while zip_code == "":
        zip_code = input("Enter zip code: ")
    return zip_code


def get_city():
    city = ""
    while city == "":
        city = input("Enter city name: ")
    return city


def get_address():
    address = ""
    while address == "":
        address = input("Enter address: ")
    return address


def get_bed_count():
    bed_count = ""
    while bed_count == "":
        bed_count = input("Enter the number of available beds: ")
    return bed_count


def get_planned_donor_number():
    donor_number = ""
    while donor_number == "":
        donor_number = input("Enter the planned number of donations: ")
    return donor_number


get_date_of_event_string()
"""
get_donation_start_time()
get_donation_end_time()
get_zip_code()
get_city()
get_address()
get_bed_count()
get_planned_donor_number()
get_planned_donor_number()
"""