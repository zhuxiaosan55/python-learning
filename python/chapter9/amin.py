from user import User


class Privileges():
    def __init__(self, privileges=['can add post', 'can delet post', 'can ban user']):
        """初始化特权属性"""
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print('everyone has this privileges:'+privilege+'.')


class Amin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()
