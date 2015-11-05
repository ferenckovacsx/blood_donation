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

    def check_age(self, birth_date):
        if ((TODAY - birth_date).days // 365) > MINIMUM_AGE_IN_YEAR:
            return True
        else:
            print("The minimum age is not reached.")
            return False

    def check_weight(self, weight):
        if weight > MINIMUM_WEIGHT_IN_KG:
            return True
        else:
            print("The minimum weight is not reached.")
            return False

    def check_last_donation(self, last_doantion):
        if (TODAY - last_doantion).days > MIN_NUMBER_OF_DAYS_FROM_LAST_DONATION:
            return True
        else:
            print("The minimum age is not reached.")
            return False

    def check_id_expiration(self, id_expire):
        if id_expire > TODAY:
            return True
        else:
            print("Your ID is expired.")
            return False

    def check_hemoglobin(self):
        self.hemoglobin_level = random.randrange(80, 220)
        if self.hemoglobin_level > 110:
            print("Your hemoglobin level is OK.")
            return True
        else:
            print("Your hemoglobin level is low.")

    def __repr__(self):
        how_old = ((TODAY - self.birth_date).days // 365)
        return "%s\n%d kg\n%s - %d years old\n%s\n%s\n%s"  \
               % (self.name, self.weight, self.birth_date.date(), how_old, self.e_mail, self.mobile_number, self.blood_type)