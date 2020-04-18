from password import Credentials, UsersInfo
import unittest


class TestCredentials(unittest.TestCase):
    '''
    Test class that defines the test cases for creating and authenticating credentials
    '''

    # def setUp(self):
    #     '''
    #     Setting up the structure before each test
    #     '''
    #     self.new_user = Credentials(1, "martin", "mwikia")


    def tearDown(self):
        '''
        Cleans up after each test has run
        '''
        Credentials.users_list = []

    def test_init(self):
        '''
        Test case to test if the case has been initialized properly
        '''
        self.assertEqual(self.new_user.recognise, 1)
        self.assertEqual(self.new_user.username, "martin")
        self.assertEqual(self.new_user.password, "mwikia")

    def test_create(self):
        '''
        Testing if the new credential is saved into the list
        '''
        self.new_user.create_account()
        self.assertEqual(len(Credentials.users_list), 1)

    def test_authenticate(self):
        '''
        Testing to check if the authenticate function can sign in a user properly
        '''
        self.new_user.create_account()
        test_account = Credentials(1, "Test", "Password")
        test_account.create_account()

        found_user = Credentials.authenticate_account("Test", "Password")
        self.assertEqual(found_user.recognise, test_account.recognise)


class TestUserData(unittest.TestCase):
    '''
    Test class that defines the test cases for creating websites log in credentials
    '''

    def setUp(self):
        '''
        Setting up the structure before each test
        '''
        self.new_data = UsersInfo(1, 1, "gmail.com", "madashmartin")


    def tearDown(self):
        '''
        Cleans up the test after test is complete
        '''
        UsersInfo.data_list = []

    def test_init(self):
        '''
        Test case to evaluate if the case has been initialized properly
        '''
        self.assertEqual(self.new_data.ident, 1)
        self.assertEqual(self.new_data.id, 1)
        self.assertEqual(self.new_data.website, "gmail.com")
        self.assertEqual(self.new_data.web_pass, "madashmartin")

    def test_add_password(self):
        '''
        Testing if the new website and password can be saved
        '''
        self.new_data.add_password()
        self.assertEqual(len(UsersInfo.data_list), 1)

    def test_display_data(self):
        '''
        Testing if the data can be displayed.
        '''
        self.new_data.add_password()
        test_data = UsersInfo(1, 1, "gmail.com", "madashmartin")
        test_data.add_password()

        data_found = UsersInfo.display_data(1, 1)
        self.assertEqual(data_found.website, test_data.website)

    def test_data_exists(self):
        '''
        Testing to check if the function for checking data works well
        '''
        self.new_data.add_password()
        test_data = UsersInfo(1, 1, "gmail.com", "madashmartin")
        test_data.add_password()

        data_exists = UsersInfo.existing_data(1)
        self.assertTrue(data_exists)

    def test_copy_password(self):
        '''
        Testing if the copy password function works
        '''
        self.new_data.add_password()
        UsersInfo.copy_password(1, 1)

        # self.assertEqual(self.new_data.web_pass, pyperclip.paste())


if __name__ == "__main__":
    unittest.main()



