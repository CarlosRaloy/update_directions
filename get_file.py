import os
import pandas as pd
class Get_information:
    def read_csv(self):
        try:
            folder_contend = os.listdir(os.path.dirname(os.path.abspath(__file__)))

            for file_name in folder_contend:
                if file_name.endswith(".csv"):
                    return os.path.join(file_name)
        except OSError:
            print("❌ No se encontro un archivo csv")

    def convert_csv_file(self,start_counter, end_counter):
        try:
            csv_path = self.read_csv()
            if csv_path is None:
                raise ValueError("❌ La función read_csv() devolvió None. Asegúrate de proporcionar una ruta de archivo válida.")

            df = pd.read_csv(csv_path)
            if start_counter is not None and end_counter is not None:
                df = df[(df['Contador'] >= start_counter) & (df['Contador'] <= end_counter)]

            data_dict = df.to_dict(orient='records')
            print("⚙️ Contenido del archivo CSV convertido a diccionario")
            #print(data_dict)
            return data_dict
        except OSError as e:
            print(f"No se pudo crear el diccionario. Error: {e}")


""" Exaple for get information
csv = Get_information()
csv.convert_csv_file(2,3)
"""
