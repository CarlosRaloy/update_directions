# Actualizacion Masiva de direcciones 🚛

## Resumen
EL sig. proyecto se conecta a la base de datos de odoo y crea un update basandose en un archivo csv

## Requerimientos y librerias 📚

### Instalar librerias para postgres

```bash
sudo apt install libpq-dev python3-dev
```
### Instalar entorno virtual

**Importante:** : En caso de no tener la libreria de virtualenv ejecutar el sig. comando

```bash
sudo apt-get -y install python3-virtualenv
```
si se tiene la libreria , ejecutar el virlual env

```bash
virtualenv venv --python=python3
```

Activamos el entorno virtual

```bash
source venv/bin/activate
```

### Instalar Tkinter (LINUX)

```bash
sudo apt-get install python3-tk
```

### Instalar los requeriments.txt

Contiene las librerias de python que hay en el proyecto

```bash
pip3 install -r requeriments.txt
```
### Crear un archivo .env con la configuracion de la base de datos

Variables de entorno
```dotenv
USER_DB=root
PASSWORD_DB=root
HOST_DB=localhost
DATABASE_DB=test_raloy
PORT_DB=5432
```
## Ejecutando el programa ▶️

Cuando ya teminamos toda la configuracion ejecutamos el entorno grafico

```bash
python3 interface.py
```

Listo , el programa ya estara corriendo 🚀
























