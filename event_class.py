
from donation_event_register import donation_event_reg
from datetime import datetime
MIN_PERIOD = 10
PREPARATION_TIME = 30
DONATION_TIME = 30

class DonationEvent:
    date_of_event_string = datetime(1, 1, 1)
    donation_start_time = datetime(1, 1, 1)
    donation_end_time = datetime(1, 1, 1)
    city = ""
    address = ""
    zip_code = 0
    bed_count = 0
    donor_number = 0
    actual_donor_number = 0
    duration = 0


    def check_min_period(self):
        if not datetime.strptime(self.date_of_event_string, "%Y.%m.%d") - datetime.today() >= MIN_PERIOD:
            print("The registration should be at least 10 days before event.")
            return False
        else:
            return True

    def not_weekend(self):
        if not datetime.isoweekday(self.date_of_event_string):
            print("Event should be on weekdays only.")
            return False
        else:
            return True

    def donation_duration(self):
        duration = datetime.strptime(self.donation_end_time,"%Y.%m.%d") - datetime.strptime(self.donation_start_time,"%Y.%m.%d")
        return duration

    def donation_number(self):
        max_donation_number = ((self.duration - PREPARATION_TIME) / DONATION_TIME) * self.bed_count

    def get_donation_success_rate(self, donor_number, actual_donor_number):
        rate = actual_donor_number / donor_number

        if rate < 0.2:
            return "Unsuccessful, not worth to organise there again."
        elif rate <= 0.75:
            return "Normal event."
        elif rate <= 1.1:
            return "Successful."
        else:
            return "Outstanding."
