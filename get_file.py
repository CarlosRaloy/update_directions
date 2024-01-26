import os
import pandas as pd
def read_csv():
    try:
        folder_contend = os.listdir(os.path.dirname(os.path.abspath(__file__)))

        for file_name in folder_contend:
            if file_name.endswith(".csv"):
                return os.path.join(file_name)
    except OSError:
        print("❌ No se encontro un archivo csv")

def convert_csv_file():
    try:
        csv_path = read_csv()
        if csv_path is None:
            raise ValueError("❌ La función read_csv() devolvió None. Asegúrate de proporcionar una ruta de archivo válida.")

        df = pd.read_csv(csv_path)
        data_dict = df.to_dict(orient='records')
        print("⚙️ Contenido del archivo CSV convertido a diccionario")
        #print(data_dict)
        return data_dict
    except OSError as e:
        print(f"No se pudo crear el diccionario. Error: {e}")


if __name__ == "__main__":
    convert_csv_file()