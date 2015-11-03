def get_name_string():
    name_string = ""
    while name_string == "":
        name_string = input("Enter donor name: ")
    return name_string


def get_weight_string():
    weight_string = ""
    while weight_string == "":
        weight_string = input("Please enter donor weight: ")
    return weight_string


def get_gender_string():
    gender_string = ""
    while gender_string == "":
        gender_string = input("Pleas enter donor gender(Male,Female): ")
    return gender_string


def get_birth_string():
    birth_string = ""
    while birth_string == "":
        birth_string = input("Pleas enter donor birth: ")
    return birth_string


def get_last_donation_string():
    last_donation_string = ""
    while last_donation_string == "":
        last_donation_string = input("Pleas enter donor birth: ")
    return last_donation_string


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
        id_experation_date_string = input("Please enter the experation time of the ID: ")
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
