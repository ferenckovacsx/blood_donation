
from donation_event_register import donation_event_reg
from datetime import datetime
MIN_PERIOD = 10
PREPARATION_TIME = 30
DONATION_TIME = 30


class DonationEvent:
    date_of_event_string = ""
    donation_start_time = ""
    donation_end_time = ""
    address = ""
    bed_count = 0
    donor_number = 0

    def __init__(self, date_of_event_string, donation_start_time, donation_end_time, address, bed_count, donor_number):
        self.date_of_event_string = date_of_event_string
        self.donation_start_time = donation_start_time
        self.donation_end_time = donation_end_time
        self.address = address
        self.bed_count = bed_count
        self.donor_number = donor_number


    def check_min_period(self):
        if not datetime.strptime(self.date_of_event_string, "%Y.%m.%d") - datetime.today() >= MIN_PERIOD:
            print("The registration should be at least 10 days before event.")
        else:
            return True

    def not_weekend(self):
        if not datetime.isoweekday(self.date_of_event_string):
            print("Event should be on weekdays only.")
        else:
            return True

    def donation_duration(self):
        duration = datetime.strptime(self.donation_end_time) - datetime.strptime(self.donation_start_time)
        return duration

    def donor_number(self):
        max_donor_number = ((self.duration - PREPARATION_TIME) / DONATION_TIME) * self.bed_count

