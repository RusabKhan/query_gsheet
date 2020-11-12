"""

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import sqlite3


def initialize():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    Creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(Creds)
    return client.open("Lyftron")

gs =initialize()



def createDBfromWorksheets(dbName,filename):
    for s in gs.worksheets():
        df = pd.DataFrame(gs.worksheet(s.title).get_all_records())
        df.columns = df.columns.str.replace(' ', '_')
        conn = sqlite3.connect(filename)  # You can create a new database by changing the name within the quotes
        c = conn.cursor()  # The database will be saved in the location where your 'py' file is saved
        df.to_sql(s.title, conn)
        df.query()


createDBfromWorksheets('demoDB.db','demo')
"""