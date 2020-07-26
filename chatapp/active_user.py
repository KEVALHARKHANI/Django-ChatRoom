class Active_user:
    def set_name(self,username):

        self.users={}
        self.users[username]=username
    def get_name(self):
        return self.users
