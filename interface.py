import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
# ----- My Modules -----
from get_file import Get_information
from update import Credentials_database

# Get Dates from CSV
csv = Get_information()
list_file = csv.convert_csv_file(1,11)

print(list_file)

# Important: Connection in the database
my_connection = Credentials_database("root","root","test_raloy","10.150.41.114","5432")
my_connection.connnect(my_connection.update_dates('Ciudad K',1, 'Call1 One',
                                    'CENTRO','8000',1))


