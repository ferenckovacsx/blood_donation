# blood_donation 

This is a project of the Python Hussars team @ Codecool, written in Python.
The objective is to organize a blood donation event. 

The first part is to register a donor for the event.
The following data are needed for this:
* name, date of birth, weight, gender, last donation date, blood type, was sick in the last month
* ID number, expiration of ID, e-mail address, mobile number.

The following criteria are required:
* the weight must greater than 50 kilograms
* the donor has to be at least 18 years old
* the donor's ID did not expire
* the last donation date was more than 3 months ago

Data input is checked for correct format. 
* The name must contain characters, space between the first name(s) and the last name(s).
* The weight must be an integer number. The format of birth date is like this: YYYY.MM.DD (birth date, last donation date, ID expiration).
* The ID number must be one of the following formats: 6 digits and 2 letters, or 6 letters and 2 digits. 
* The blood tyoe is checked if it is in a given list. 
* The e-mail address must contain a @ character, and has to end with ".hu" or ".com". 
* The mobile number has to be in one of thee following format: +36201234567 or 06309876543. The mobile number should begin
with +36 or 06 prefix, after that there is the region code of the provider. The last 7 digits is the actual phone number.

At the end of the registration procedure, the program displays the donor's data in a nice format.

The second part is the donation event registration. 
The following data are needed:
* date of event
* start time of event
* end time of event
* an address, where would the event take place
  - zip code
  - city
  - address
* available beds for the donation
* planned donor number

These are the criteria for the data above:
* the registration of the event should occur before 10 days of the event
* the event can only be on weekdays
* address validation
  - the address should be 25 characters long
  - the zip code is valid: 4 digit number, cannot begin with zero
  - the city is in a given list

The program calculates the duration time of the event in minutes, then using the given preparation and donation
time plus the number of available beds, the program calculates the maximum donor number who can attend the event.

After the registration, the program asks the user, to input the number of successful donations.
(Let's assume that the event has happened.)
The program prints out that how successful the evenet was, based on  the planned donor number and the number of
successful donations.