from datetime import datetime
GENDERS = ("male","female")
BLOOD_TYPES = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', '0+', '0-']


def get_name_string():
    name_string = ""
    while name_string == "":
        name_string = input("Enter donor's name: ")
        splitted_name = name_string.split(" ")
        if len(splitted_name) == len([x for x in splitted_name if x.isalpha()]):
            return name_string
        else:
            print("Format is invalid. ('firstname lastname')")
            name_string = ""


def get_weight_string():
    weight_string = ""
    while weight_string == "":
        weight_string = input("Please enter donor's weight: ")
        if weight_string.isdigit():
            return weight_string
        else:
            print("Invalid value.")
            weight_string = ""


def get_gender_string():
    gender_string = ""
    while gender_string == "":
        gender_string = input("Pleas enter donor gender (male, female): ").lower()
        if gender_string in GENDERS:
            return gender_string
        else:
            print("Not a valid answer.")
            gender_string = ""


def get_birth_string():
    birth_string = ""
    while birth_string == "":
        birth_string = input("Pleas enter donor's date of birth (YYYY.MM.DD): ")
        try:
            birth_date = datetime.strptime(birth_string,"%Y.%m.%d")
            return birth_date
        except:
            print("Invalid date.")
            print("Format is invalid.(YYYY.MM.DD)")
            birth_string = ""


def get_last_donation_string():
    last_donation_string = ""
    while last_donation_string == "":
        last_donation_string = input("Pleas enter donor's last donation date (YYYY.MM.DD): ")
        try:
            donation_date = datetime.strptime(last_donation_string,"%Y.%m.%d")
            return donation_date
        except:
            print("Format is invalid. (YYYY.MM.DD)")
            last_donation_string = ""


def get_sick_response_string():
    sick_response_string = ""
    while sick_response_string == "":
        sick_response_string = input("Was the donor sick in the last month? (Y,N): ")
        if sick_response_string.lower() not in ["y", "n"]:
            print("Please enter Y or N")
            sick_response_string = ""

    return sick_response_string


def check_identifier(doc_id):
    if len(doc_id) == 8:
        if (doc_id[:6].isdigit() and doc_id[6:].isalpha()) or \
            (doc_id[:6].isalpha() and doc_id[6:].isdigit()):
            return True
    else:
        return False


def get_unique_indentifier_string():
    unique_indentifier_string = ""
    while unique_indentifier_string == "":
        unique_indentifier_string = input("Please enter a unique indentifier for the donor: ")
        if not check_identifier(unique_indentifier_string):
            print("Please enter a valid identifier.")
            unique_indentifier_string = ""

    return unique_indentifier_string


def get_donor_blood_type_string():
    blood_type_string = ""
    while blood_type_string == "":
        blood_type_string = input("Please enter the donor's blood type ({0}): ".format(", ".join(BLOOD_TYPES)))
        if blood_type_string.upper() not in BLOOD_TYPES:
            print("Please enter a correct blood type.")
            blood_type_string = ""
    return blood_type_string


def get_id_expiration_date_string():
    id_expiration_date_string = ""
    while id_expiration_date_string == "":
        id_expiration_date_string = input("Please enter the expiration date of the ID (YYYY.MM.DD): ")

    return id_expiration_date_string


def email_is_valid(email_string):
    return "@" in email_string and \
           email_string.index("@") > 0 and \
           (email_string.endswith(".hu") or email_string.endswith(".com"))


def get_email_string():
    email_string = ""
    while email_string == "":
        email_string = input("Please enter donor's e-mail address (example@something.com/.hu): ")
        if not email_is_valid(email_string):
            print("Please input a valid e-mail address.")
            print("The e-mail address should contain a @ and must end with .hu or .com")
            email_string = ""

    return email_string


def is_it_valid_mobile_number(number_to_validate: str):
    providers = ["20", "30", "70"]
    start_is_valid = False
    provider_index = 2

    if number_to_validate.startswith("06"):
        start_is_valid = True
    elif number_to_validate.startswith("+36"):
        start_is_valid = True
        provider_index = 3

    provider_is_valid = number_to_validate[provider_index:provider_index + 2] in providers
    ending_is_digit = number_to_validate[provider_index + 2:].isdigit()

    return start_is_valid and \
           provider_is_valid and \
           len(number_to_validate) in [11, 12] and \
           ending_is_digit


def get_mobile_string():
    mobile_string = ""
    while mobile_string == "":
        mobile_string = input("Please enter donor's mobile number: ")
        if not is_it_valid_mobile_number(mobile_string):
            print("Please enter a valid mobile number\nn(examples: +36301234567, 06201112223)")
            mobile_string = ""
    return mobile_string
