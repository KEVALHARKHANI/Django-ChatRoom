class Active_user:
    def __init__(self):
        self.active_user={
            "connected":"true"
        }

    def set_name(self,user):
        self.active_user[user]=user
    def get_name(self):
        return self.active_user