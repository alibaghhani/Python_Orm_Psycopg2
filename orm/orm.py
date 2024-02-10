import psycopg2


class Context_manager_for_orm:
    def __enter__(self):
        self.conn = psycopg2.connect("dbname='postgres' user='postgres' host='localhost' password='1234' post='5432'")
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.conn.commit()
        self.conn.close()


class Orm(psycopg2):

    def create_table(self, table_name, values: list):
        if isinstance(table_name, str) and isinstance(values, list):
            with Context_manager_for_orm() as cursor:
                column_definitions = ', '.join([f"{col.replace(' ', '_')} VARCHAR(255)" for col in values])
                query = f"""CREATE TABLE IF NOT EXISTS {table_name}
                     (id SERIAL PRIMARY KEY, {column_definitions})"""
                cursor.execute(query)

    def drop_table(self, table_name):
        if isinstance(table_name, str):
            with Context_manager_for_orm() as cursor:
                query = f"""DROP TABLE IF EXISTS {table_name} """
                cursor.execute(query)

    def show_table(self, table_name, filter_column=None, filter_column_value=None, mode=None):
        if isinstance(table_name, str):
            with Context_manager_for_orm() as cursor:
                if filter_column_value:
                    query = f"SELECT * FROM {table_name} WHERE {filter_column} = %s ORDER BY name;"
                    cursor.execute(query, (filter_column_value,))
                    result = cursor.fetchall()
                    print(result)
                else:
                    query = f"""SELECT * FROM {table_name} 
                    ORDER BY {filter_column} {mode};"""
                    cursor.execute(query)
                    results = cursor.fetchall()
                    for result in results:
                        print(result)

    def insert_to_table(self, table_name, values):
        if isinstance(table_name, str) and isinstance(values, list):
            with Context_manager_for_orm() as cursor:
                value_getter = ', '.join(['%s'] * len(values))
                cursor.execute(f"""INSERT INTO {table_name}
                 VALUES (default, {value_getter})""", values)

    def delete_row(self, table_name, filter_column=None, filter_column_value=None):
        if isinstance(table_name, str):
            with Context_manager_for_orm() as cursor:
                if filter_column is None:
                    query = f"DELETE FROM {table_name};"
                    cursor.execute(query)
                else:
                    query = f"DELETE FROM {table_name} WHERE {filter_column} = %s;"
                    cursor.execute(query, (filter_column_value,))
                print("row(s) deleted!")

    def update(self, table_name, column_to_change, new_value, column_to_defind=None, value_to_defind=None):
        if isinstance(table_name, str):
            if column_to_defind:
                with Context_manager_for_orm() as cursor:
                    query = f"""
                    UPDATE {table_name}
                    SET {column_to_change} = '{new_value}'
                    WHERE {column_to_defind} = '{value_to_defind}'; 
                    """
                    cursor.execute(query)
                    print("Updated successfully!")
            else:
                with Context_manager_for_orm() as cursor:
                    query = f"""
                    UPDATE {table_name}
                    SET {column_to_change} = '{new_value}';
                    """
                    cursor.execute(query)
    def if_exists(self,table_name,column,value):
        with Context_manager_for_orm() as cursor:
            query = f"""
            SELECT * FROM {table_name} WHERE {column} = %s
            """
            cursor.execute(query, (value,))
            return cursor.fetchone() is not None

