from user import User
from amin import Amin, Privileges
my_admin = Amin('lin', 'kun', 28)
my_admin.describe_user()
my_admin.privileges.show_privileges()
