from user import User
from orm.orm import Context_manager_for_orm,Orm



class Admin(User):
    def __init__(self,username,password):
        super().__init__(username,password)
        self.database = Orm()
        self.is_logged = None

    def register(self):
        print("implemented!")

    def login(self,table_name):
        if self.database.if_exists(table_name,"name",self.username):
            for i in self.database.show_table(table_name,"name",self.username):
                if i[3] == self.password:
                    self.is_logged = True
                else:
                    return "incorrect password"
        else:
            return "user not found"

    def create_table(self,table_name,value):
        if isinstance(value,list):
            self.database.create_table(table_name,value)
        else:
            return "the value attribute must be list!"

    def drop_table(self,table_name):
        if isinstance(table_name,str):
            self.database.drop_table(table_name)
        else:
            return "table name must be string"

    def show_table(self, table_name, filter_column=None, filter_column_value=None, mode=None):
        self.database.show_table(table_name,filter_column,filter_column_value,mode)

    def add_to_table(self, table_name, values):
        if isinstance(values,list):
            self.database.insert_to_table(table_name,values)
        else:
            return "the values attribute must be list!"

    def delete_data(self,table_name, filter_column=None, filter_column_value=None):
        self.database.delete_row(table_name,filter_column,filter_column_value)
        return "data was deleted successfully"

    def update_data(self,table_name, column_to_change, new_value, column_to_defind=None, value_to_defind=None):
        self.database.update(table_name,column_to_change,new_value,column_to_defind,value_to_defind)





