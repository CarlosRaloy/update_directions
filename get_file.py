import os
import pandas as pd
def read_csv():
    try:
        folder_contend = os.listdir(os.path.dirname(os.path.abspath(__file__)))

        for file_name in folder_contend:
            if file_name.endswith(".csv"):
                print(f"Se encontró un archivo CSV: 📗 {file_name}")
                return os.path.join(file_name)

    except OSError:
        print("❌ No se encontro un archivo csv")

def convert_csv_file():
    df = pd.read_csv(read_csv())
    data_dict = df.to_dict(orient='records')
    print("⚙️ Contenido del archivo CSV convertido a diccionario")
    print(data_dict)
    return data_dict


if __name__ == "__main__":
    read_csv()
    convert_csv_file()