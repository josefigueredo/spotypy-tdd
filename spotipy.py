from not_available_email import NotAvailableEmail

class Spotipy():
    
    def __init__(self):
        self.__user = []

    def register_user(self, new_user):
        if self.__is_available_email(new_user):
            self.__user.append(new_user)
        else:
            raise NotAvailableEmail(new_user.email)

    def __is_available_email(self, new_user):

        repeated = list(filter( lambda u: u.email == new_user.email, self.__user ))

        return len(repeated) == 0

    def is_registered(self, email):

        return email in list(map( lambda u: u.email, self.__user))