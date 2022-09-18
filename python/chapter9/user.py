class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("My name is "+self.first_name.title()+" " +
              self.last_name.title()+"\tI'm "+str(self.age)+' years old '+' lgoin '+str(self.login_attempts)+'times')

    def greet_user(self):
        print(self.first_name.title()+' Welcome!')

    def increment_login_attemps(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


'''
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
'''

'''       self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        for privilege in self.privileges:
            print('everyone has this privileges:'+privilege+'.')



Linkun = User('shen', 'linkun', 29)
Linkun.describe_user()
Linkun.greet_user()
Jaychou = User('jay', 'chou', 39)
Jaychou.describe_user()
Jaychou.greet_user()
Jaychou.increment_login_attemps()
Jaychou.increment_login_attemps()
Jaychou.describe_user()
Jaychou.reset_login_attempts()
Jaychou.describe_user()
# admin = Amin('ge', 'ge', 31)
admin.privileges.show_privileges()
'''
