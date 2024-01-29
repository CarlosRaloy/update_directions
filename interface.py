import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
# ----- My Modules -----
from get_file import Get_information
from update import Credentials_database


def start_process():
    # Get Dates from CSV
    csv = Get_information()
    list_file = csv.convert_csv_file(int(start.get()), int(finish.get()))

    # Important: Connection in the database
    my_connection = Credentials_database("root", "root", "test_raloy", "10.150.41.114", "5432")

    for i in list_file:
        print(F"Num. Dato: {i['Contador']}")
        my_connection.connnect(my_connection.update_dates(i['city'], i['state_id'], i['street'],
                                                          i['street2'], i['zip'], i['id']))


if __name__ == "__main__":
    window = tk.Tk()
    window.title("Actualizacion de determinantes")
    window.geometry("300x200")
    window.configure(bg="white")

    style = ThemedStyle(window)
    style.set_theme("arc")
    frame = ttk.Frame(window, style="TFrame")
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Configure the widgets
    style.configure("TFrame", background="white")
    style.configure("TLabel", font=('Helvetica', 12), padding=6, background="white")
    style.configure("TEntry", fieldbackground="white", font=('Helvetica', 12), padding=6)
    style.configure("TButton", font=('Helvetica', 12, 'bold'), padding=6)

    label_start = ttk.Label(frame, text="INICIO:")
    label_start.grid(row=0, column=0, pady=(0, 10), sticky=tk.W)

    label_finish = ttk.Label(frame, text="FIN:")
    label_finish.grid(row=1, column=0, pady=(0, 10), sticky=tk.W)

    start = ttk.Entry(frame)
    start.grid(row=0, column=1, pady=(0, 10), sticky=tk.W + tk.E)

    finish = ttk.Entry(frame)
    finish.grid(row=1, column=1, pady=(0, 10), sticky=tk.W + tk.E)

    button_execute = ttk.Button(frame, text="INICIAR", command=start_process)
    button_execute.grid(row=2, column=1, pady=(10, 0), sticky=tk.E)

    # Center aligned
    for child in frame.winfo_children():
        child.grid_configure(padx=10)

    window.mainloop()
