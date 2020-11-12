import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dateutil.parser import parse
import pandas as pd

data = []
gs = None


def initialize():
    scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    Creds = ServiceAccountCredentials.from_json_keyfile_name(
        "creds.json", scope)
    client = gspread.authorize(Creds)
    return client.open("Lyftron")

    # data = sheet.get_all_records()
    # 1st row of all sheets stored in this e.g column names stored in this


gs = initialize()  # activate all sheet methods from here
filtered_dict = []


def makeSchema():
    sheets = gs.worksheets()
    schema = []
    for s in sheets:
        headers = (s.row_values(1))
        # read first 100 values to determine datatypes
        res = (gs.values_get(s.title + "!A2:AZ100"))
        table = pd.DataFrame(res['values'])
        schema.append(checkDtype(table, headers))
    return schema


def makeLookup():
    lookUp = dt
    sheets = []
    for d in lookUp:
        for s in d:
            d[d.index(s)] = s.split(":", maxsplit=1)[0]
    for s in gs.worksheets():
        sheets.append(s.title)
    lookUp.append(sheets)
    return lookUp


# print(gs.worksheet('S1').col_values(1).__contains__('bookkeeping'))
# print(gs.worksheet('S1').col_values(2).__contains__('bookkeeping'))
# print(gs.worksheet('S1').col_values(5).__contains__('31'))

def checkDtype(table, headers):
    digit = 0
    date = 0
    inc = 0
    for c in table:
        for v in table[c]:
            if v.isdigit() | v.replace('.', '').replace(',', '').isdigit():
                digit = digit + 1
            elif is_date(v):
                date = date + 1
        if digit == len(table[c]):
            if table[c].str.len().max() > 5:
                headers[inc] = headers[inc] + ":nvarchar"
                inc = inc + 1
                digit = 0
            else:
                headers[inc] = headers[inc] + ":int"
                inc = inc + 1
                digit = 0
        elif date == len(table[c]):
            headers[inc] = headers[inc] + ":date"
            inc = inc + 1
            date = 0
        else:
            if table[c].str.len().max() > 5:
                headers[inc] = headers[inc] + ":nvarchar"
                inc = inc + 1
            else:
                headers[inc] = headers[inc] + ":varchar"
                inc = inc + 1
    return headers


def is_date(string, fuzzy=False):
    """
    Return whether the string can be interpreted as a date.
    :param string: str, string to check for date
    :param fuzzy: bool, ignore unknown tokens in string if True
    """
    try:
        parse(string, fuzzy=fuzzy)
        return True

    except ValueError:
        return False


def makeTable():
    sheets = gs.worksheets()
    table = None
    for s in sheets:
        # read first 100 values to determine datatypes
        res = (gs.values_get(s.title + "!A1:AZ100"))
        t1 = pd.DataFrame(res['values'])
        table = pd.concat([table, t1], axis=1)
    print(table)


# makeTable()

dt = makeSchema()

lookUp = makeLookup()


def filterData(table, columns, value):
    if isinstance(columns, list) & isinstance(value, list):
        for col in columns:
            arrIndex = (lookUp[len(lookUp) - 1].index(table))
            colIndex = lookUp[arrIndex].index(col) + 1
            c = gs.worksheet(table).findall(
                value[columns.index(col)], None, colIndex)
            for s in c:
                print(gs.worksheet(table).row_values(s.row))
    elif isinstance(value, list):
        arrIndex = (lookUp[len(lookUp) - 1].index(table))
        colIndex = lookUp[arrIndex].index(columns) + 1
        c = gs.worksheet(table).findall(
            value[columns.index(columns)], None, colIndex)
        for s in c:
            print(gs.worksheet(table).row_values(s.row))
    elif isinstance(columns, list):
        for col in columns:
            arrIndex = (lookUp[len(lookUp) - 1].index(table))
            colIndex = lookUp[arrIndex].index(col) + 1
            c = gs.worksheet(table).findall(
                value, None, colIndex)
            for s in c:
                print(gs.worksheet(table).row_values(s.row))
    else:
        arrIndex = (lookUp[len(lookUp) - 1].index(table))
        colIndex = lookUp[arrIndex].index(columns) + 1
        c = gs.worksheet(table).findall(
            value, None, colIndex)
        for s in c:
            print(gs.worksheet(table).row_values(s.row))
    # print(lookUp)
    """
    dict = [d for d in data if d[col] == value]

    if len(columns) < 1:
        return dict
    for c in columns:
        for d in dict:
            filtered_dict.append(d[c])

    return filtered_dict
    # filtered_dict = [d[c] for d in dict]

    #    df = pd.DataFrame(filtered_dict)
    #    dfg = df.groupby(
    #        ['Keyword', 'Min search volume', 'Max search volume', 'Competition', 'Competition (indexed value)']).sum()
    #    dfg.to_html('result.html');

    # df = pd.DataFrame(filtered_dict)
    # dfg = df.groupby(['Keyword']).sum()
    #    Table = []
    #    for key, value in df.iteritems():  # or .items() in Python 3
    #        temp = []
    #        temp.extend([key, value])  # Note that this will change depending on the structure of your dictionary
    #        Table.append(temp)
    #     return filtered_dict
"""


# filterData('S1', ['Keyword', 'Competition (indexed value)'],
#          ['bookkeeping', '31'])


def updateData(updateCol, updateValue, col, value):
    colIndex = (
            (next((d for d, i in enumerate(data) if updateCol in i), None)) + 1)
    valueIndex = (next((d for d, i in enumerate(data)
                        if updateValue in i.values()), None)) + 2


def deleteData(updateValue):
    delIndex = (next((d for d, i in enumerate(data)
                      if updateValue in i.values()), None)) + 2

    # return gs.delete_row(delIndex)

# pprint (d for d in data if d['Min search volume'] > 10)
# pprint(filtered_dict)
