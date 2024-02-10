from customer import Customer
from admin import Admin
from abc import abstractmethod, ABC


class Factoryuser(ABC):
    def __init__(self,username,password):
        self.username = username
        self.password = password
    @abstractmethod
    def users_creator(self):
        raise NotImplementedError("you must implement this method")


class Factoryadmin(Factoryuser):
    def users_creator(self):
        return Admin(self.username,self.password)


class Factorycustomer(Factoryuser):
    def users_creator(self):
        return Customer(self.username,self.password)


class Authenticate_users:
    def __init__(self,factory,username,password,table_name):
        self.factory = factory
        self.user = self.factory.users_creator()
        self.username = username
        self.password = password
        self.table_name = table_name

    def register_user(self):
        self.user.register(self.table_name)

    def login_user(self):
        self.user.login(self.table_name)
