

class User():
    def __init__(self, first_name, last_name, login_attempts, **user_info):
        """包含用户姓与名及其它几个属性"""
        self.name = {}  # 定义空字典
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = login_attempts
        for k, v in user_info.items():
            self.name[k] = v  # 将所有字典值赋值给字典name，其实姓名也可以赋值到这个字典里面

    def describe_user(self):
        '''打印用户信息摘要'''
        print('以下为用户的基本信息： ')
        self.fullname = self.first_name + self.last_name
        print('姓名：' + self.fullname)
        for key, value in self.name.items():  # 使用字典里面的信息
            print(key + ': ' + str(value))

    def greet_user(self):
        print(self.first_name.title() + self.last_name.title() + ' Welcome to join us')

    def increment_login_attempts(self):
        self.fullname = self.first_name + self.last_name
        self.login_attempts += 1
        print(self.fullname.title() + ' 尝试登录次数是' + str(self.login_attempts) + '次')

    def reset_login_attempts(self):
        self.fullname = self.first_name + self.last_name
        self.login_attempts = 0
        print('重置用户 ' + self.fullname.title() + '登录次数为' + str(self.login_attempts) + '次')


class Privileges():
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print('The administrator has the following permissions :')
        for self.privilege in self.privileges:
            print(self.privilege.title())


class Admin(User):
    def __init__(self, first_name, last_name, login_attempts, privileges, **user_info):
        super().__init__(first_name, last_name, login_attempts, **user_info)
        self.privileges = Privileges(privileges)  # 在Admin类中增加了一个Privileges类 实例用作其属性。


print('\n')


eric = Admin('Albert','Einstein','123456','111@qq.com',)
eric_privileges = [
    'can reset passwords',
    'can moderate discussions',
    'can suspend accounts',
    ]
eric.privileges.privileges = eric_privileges
eric.privileges.show_privileges()







