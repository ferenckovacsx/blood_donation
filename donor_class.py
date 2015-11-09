from datetime import datetime
import random

MINIMUM_AGE_IN_YEAR = 18
MINIMUM_WEIGHT_IN_KG = 50
MIN_NUMBER_OF_DAYS_FROM_LAST_DONATION = 90
MINIMUM_HEMOGLOBIN_LEVEL = 110
TODAY = datetime.now()


class Donor(object):
    name = ""
    weight = 0
    gender = ""
    birth_date = datetime(1, 1, 1)
    last_donation = datetime(1, 1, 1)
    was_sick_last_month = ""
    identifier = ""
    id_expire = datetime(1, 1, 1)
    blood_type = ""
    e_mail = ""
    mobile_number = ""
    hemoglobin_level = 0
    how_old = ((TODAY - birth_date).days // 365)

    def check_age(self):
        if ((TODAY - self.birth_date).days // 365) > MINIMUM_AGE_IN_YEAR:
            return True
        else:
            print("The minimum age is not reached.")
            return False

    def check_weight(self):
        if self.weight > MINIMUM_WEIGHT_IN_KG:
            return True
        else:
            print("The minimum weight is not reached.")
            return False

    def check_last_donation(self):
        if (TODAY - self.last_donation).days > MIN_NUMBER_OF_DAYS_FROM_LAST_DONATION:
            return True
        else:
            print("The minimum age is not reached.")
            return False

    def check_id_expiration(self):
        if self.id_expire > TODAY:
            return True
        else:
            print("Your ID is expired.")
            return False

    def check_hemoglobin(self):
        self.hemoglobin_level = random.randrange(80, 220)
        if self.hemoglobin_level > 110:
            print("\nYour hemoglobin level is OK.")
            return True
        else:
            print("\nYour hemoglobin level is low.")

    def is_suitable(self):
        if self.check_age() and self.check_weight() and self.check_id_expiration() \
            and self.check_last_donation() and self.check_hemoglobin():
            return "OK"
        else:
            return "Sorry"

    def __repr__(self):
        return "\nName: %s - %s\nWeight: %d kg\nAge: %s - %d years old\nE-Mail: %s\n" \
               "Mobile Number: %s\nBlood Type: %s\nID number: %s\nID expires: %s\nHemoglobin level: %s\n\n" \
               "Donor suitable for donation: %s"  \
               % (self.name, self.gender, self.weight, self.birth_date.date(), self.how_old, self.e_mail,
                  self.mobile_number, self.blood_type, self.identifier, self.id_expire, self.hemoglobin_level,
                  self.is_suitable())