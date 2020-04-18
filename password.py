class Credentials:
    '''
    Class that creates accounts and authenticates the users
    '''
    users_list = []

    def __init__(self, recognise, username, password):
        '''
        Initalizing the variables
        '''
        self.recognise = recognise
        self.username = username
        self.password = password

    def create_account(self):
        '''
        creating and saving log in credentials for the various users
        '''
        Credentials.users_list.append(self)

    @classmethod
    def authenticate_account(cls, name, key):
        '''
        Method that checks if the username and password are correct
        '''
        for user in cls.users_list:
            if user.username == name and user.password == key:

                return user
        return 0


class UsersInfo:
    '''
    Class that holds website and password info for the users
    '''
    data_list = []

    def __init__(self, ident, id, website, web_pass):
        self.ident = ident
        self.id = id
        self.website = website
        self.web_pass = web_pass

    # def add_password(self):
    #     '''
    #     creating a method that creates the username and password
    #     '''
    #     UsersInfo.data_list.append(self)

    @classmethod
    def display_data(cls, number, count):
        '''
        display all passwords generated by the user
        '''
        for password in cls.data_list:
            if password.ident == number:
                if password.id == count:
                    return password

    @classmethod
    def existing_data(cls, number):
        '''
        Checks if info exists in the profile
        '''
        for data in cls.data_list:
            if data.ident == number:
                return True
        return False

    @classmethod
    def copy_password(cls, number, count):
        found_password = UsersInfo.display_data(number, count)
        # pyperclip.copy(found_password.web_pass)
