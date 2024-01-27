import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
# ----- My Modules -----
from get_file import Get_information
from update import Credentials_database

def start_process():
# Get Dates from CSV
    csv = Get_information()
    list_file = csv.convert_csv_file(int(inicio.get()), int(fin.get()))

    # Important: Connection in the database
    my_connection = Credentials_database("root","root","test_raloy","10.150.41.114","5432")

    for i in list_file:
        print(F"Num. Dato: {i['Contador']}")
        my_connection.connnect(my_connection.update_dates(i['city'] , i['state_id'], i['street'], i['street2'], i['zip'], i['id']))


ventana = tk.Tk()
ventana.title("Actualizacion de determinates")
ventana.config(width=400, height=300)

style = ThemedStyle(ventana)
style.set_theme("adapta")

canvas = tk.Canvas(ventana, highlightthickness=0, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)


etiqueta_inicio = ttk.Label(text="INICIO:")
etiqueta_inicio.place(x=20, y=20)

etiqueta_fin = ttk.Label(text="FIN:")
etiqueta_fin.place(x=20, y=50)

inicio = ttk.Entry()
inicio.place(x=120, y=20, width=160)

fin = ttk.Entry()
fin.place(x=120, y=50, width=160)

boton_execute = ttk.Button(text="INICIAR", command=start_process)
boton_execute.place(x=195, y=120)

ventana.mainloop()
