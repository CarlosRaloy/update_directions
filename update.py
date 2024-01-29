import psycopg2
class Credentials_database:
    def __init__(self, user, password, database, host, port):
        self.__user = user
        self.__password = password
        self.__database = database
        self.__host = host
        self.__port = int(port)

    def connnect(self, query):
        db_params = {
            'host': self.__host,
            'database': self.__database,
            'user': self.__user,
            'password': self.__password,
            'port': self.__port,
        }

        try:
            conn = psycopg2.connect(**db_params)
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()

        except psycopg2.Error as e:
            print(f"Error al ejecutar la consulta: {e}")

        finally:
            if conn:
                cursor.close()
                conn.close()

    def update_dates(self, city, state_id, street, street2, zip_code, id_partner):
        sql_query = f"""
            UPDATE public.res_partner
            SET
              city = '{city}',
              state_id = {state_id},
              street = '{street}',
              street2 = '{street2}',
              zip = '{zip_code}'
            WHERE
              id = {id_partner};
            """
        print("Query Exitoso")
        return sql_query


#Notes: Productive database
"""my_connection = Credentials_database("root", "root",
                                     "localhost", "localhost", "5432")"""

""" Example from call to update_dates
my_connection.connnect(my_connection.update_dates('Ciudad K',1, 'Call1 One',
                                    'CENTRO','8000',1))
"""
