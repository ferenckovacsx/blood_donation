from datetime import datetime
GENDERS = ("male","female")


def get_name_string():
    name_string = ""
    while name_string == "":
        name_string = input("Enter donor name: ")
        splitted_name = name_string.split(" ")
        if len(splitted_name) == 2 and splitted_name[0].isalpha() and splitted_name[1].isalpha():
            return name_string
        else:
            print("Format is invalid.(Firstname Lastname)")
            name_string = ""


def get_weight_string():
    weight_string = ""
    while weight_string == "":
        weight_string = input("Please enter donor weight: ")
        if weight_string.isdigit():
            return weight_string
        else:
            print("Format is invalid.")
            weight_string = ""


def get_gender_string():
    gender_string = ""
    while gender_string == "":
        gender_string = input("Pleas enter donor gender(Male,Female): ").lower()
        if gender_string in GENDERS:
            return gender_string
        else:
            print("Not a valid answer.(Male or Female)")
            gender_string = ""


def get_birth_string():
    birth_string = ""
    while birth_string == "":
        birth_string = input("Pleas enter donor birth(YYYY.MM.DD): ")
        try:
            birth_date = datetime.strptime(birth_string,"%Y.%m.%d")
            return birth_date
        except:
            print("Format is invalid.(YYYY.MM.DD)")
            birth_string = ""


def get_last_donation_string():
    last_donation_string = ""
    while last_donation_string == "":
        last_donation_string = input("Pleas enter donor last donation date(YYYY:MM:DD): ")
        try:
            donation_date = datetime.strptime(last_donation_string,"%Y.%m.%d")
            return donation_date
        except:
            print("Format is invalid.(YYYY.MM.DD)")
            last_donation_string = ""


def get_sick_response_string():
    sick_response_string = ""
    while sick_response_string == "":
        sick_response_string = input("Was the donor sick in the last month?(Yes,No): ")
    return sick_response_string


def get_unique_indentifier_string():
    unique_indentifier_string = ""
    while unique_indentifier_string == "":
        unique_indentifier_string = input("Please enter the donor unique indentifier: ")
    return unique_indentifier_string


def get_donor_blood_type_string():
    blood_type_string = ""
    while blood_type_string == "":
        blood_type_string = input("Please enter the donor blood type: ")
    return blood_type_string


def get_id_experation_date_string():
    id_experation_date_string = ""
    while id_experation_date_string == "":
        id_experation_date_string = input("Please enter the experation time of the ID(YYYY:MM:DD): ")
    return id_experation_date_string


def get_email_string():
    email_string = ""
    while email_string == "":
        email_string = input("Please enter donor email(example@something.com): ")
    return email_string


def get_mobile_string():
    mobile_string = ""
    while mobile_string == "":
        mobile_string = input("Please enter donor mobile number: ")
    return mobile_string


get_name_string()
get_weight_string()
get_gender_string()
get_birth_string()
get_last_donation_string()