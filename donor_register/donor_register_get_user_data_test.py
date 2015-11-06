import unittest
from donor_register import donor_register_get_user_data


class ValidationTestCase(unittest.TestCase):
    def test_identifier_number(self):
        self.assertTrue(donor_register_get_user_data.check_identifier("123456CD"), "This should be a personal ID card.")
        self.assertTrue(donor_register_get_user_data.check_identifier("DFBCGH56"), "This should be a passport.")
        self.assertFalse(donor_register_get_user_data.check_identifier("A1B2C3"), "This should be a wrong value.")

    def test_email_address(self):
        self.assertFalse(donor_register_get_user_data.email_is_valid("@abc.de"), "This should be wrong.")
        self.assertTrue(donor_register_get_user_data.email_is_valid("gmail@chucknorris.com"), "This is Chuck Norris' e-mail.")
        self.assertTrue(donor_register_get_user_data.email_is_valid("manyika@freemail.hu"), "This should be good.")

    def test_mobile_number(self):
        self.assertTrue(donor_register_get_user_data.is_it_valid_mobile_number("+36301237895"), "This should be a valid number-")
        self.assertFalse(donor_register_get_user_data.is_it_valid_mobile_number("36201122334"))
        self.assertTrue(donor_register_get_user_data.is_it_valid_mobile_number("06709873214"))

if __name__ == '__main__':
    unittest.main()
