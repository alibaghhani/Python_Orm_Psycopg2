from user import User
from orm.orm import Orm, Context_manager_for_orm


class Customer(User):
    def __init__(self, username, password):
        super().__init__(username, password)
        self.database = Orm()
        self.is_logged = None

    def login(self,table_name):
        if self.database.if_exists("customer", "name", self.username):
            for data in self.database.show_table("customer", "name", self.username):
                if data[3] == self.password:
                    self.is_logged = True
                else:
                    return "incorrect password"

    def register(self,table_name):
        if isinstance(self.username, str) and len(self.username) > 8:
            self.database.insert_to_table(table_name", [self.username,self.password])
        else:
            return "length of username must be more than 8 characters"

    def show_table(self,table_name:str, column_name, mode:str):
        self.database.show_table(table_name=table_name,filter_column=column_name,mode=mode)



    def logout(self, table_name, filter_column=None, filter_column_value=None):
        self.database.delete_row("customer","name",self.username)
        return "user was deleted successfully"
