from datetime import datetime

CITIES = ("miskolc", "kazincbarcika", "szerencs", "sarospatak")


def get_date_of_event_string():
    date_of_event_string = ""
    while date_of_event_string == "":
        date_of_event_string = input("Enter date of event (YYYY.MM.DD): ")
        try:
            datetime.strptime(date_of_event_string, '%Y.%m.%d')
            return date_of_event_string
        except:
            print("Incorrect date. Please try again.")
            date_of_event_string = ""


def get_donation_start_time():
    donation_start_time = ""
    while donation_start_time == "":
        donation_start_time = input("Enter the start time of the donation (H:M) : ")
        try:
            datetime.strptime(donation_start_time, '%H:%M')
            return donation_start_time
        except:
            print("Incorrect time format. Please try again.")
            donation_start_time = ""


def get_donation_end_time():
    donation_end_time = ""
    while donation_end_time == "":
        donation_end_time = input("Enter the end time of the donation (H:M): ")
        try:
            datetime.strptime(donation_end_time, '%H:%M')
            return donation_end_time
        except:
            print("Incorrect time format. Please try again.")
            donation_end_time = ""


def get_zip_code():
    zip_code = ""
    while zip_code == "":
        zip_code = input("Enter zip code (XXXX): ")
        if zip_code.isdigit() and len(zip_code) == 4 and str(zip_code)[0] != "0":
            return zip_code
        else:
            print("Zip code should contain 4 positive integers and can't start with 0. Please try again.")
            zip_code = ""


def get_city():
    city = ""
    while city == "":
        city = input("Enter city name (one of the following: Miskolc, Kazincbarcika, Szerencs, Sarospatak): ")
        if city.lower() in CITIES:
            return city
        else:
            print("The chosen city should be one of the following cities: Miskolc, Kazincbarcika, Szerencs, Sarospatak. Please try again.")
            city = ""


def get_address():
    address = ""
    while address == "":
        address = input("Enter address: ")
        if len(address) <= 25:
            return address
        else:
            print("Street name too long")
            address = ""


def get_bed_count():
    bed_count = ""
    while bed_count == "":
        bed_count = input("Enter the number of available beds: ")
        if bed_count.isdigit() and int(bed_count) > 0:
            return bed_count
        else:
            print("Invalid bed count. Please try again.")
            bed_count = ""


def get_planned_donor_number():
    donor_number = ""
    while donor_number == "":
        donor_number = input("Enter the planned number of donations: ")
        if donor_number.isdigit() and int(donor_number) > 0:
            return donor_number
        else:
            print("Invalid input. Please enter a positive integer.")