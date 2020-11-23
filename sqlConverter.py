from sheets import filterData, deleteData, updateData
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dateutil.parser import parse
import pandas as pd

slct = 'select'
updt = 'update'
dlte = 'delete'


def queryMaker(query):
    commands = query.split()
    col = []
    values = []

    if (commands[0].lower() == slct.lower()):
        if (re.search('where', query, re.IGNORECASE)):
            columnsPart = query.split('where ')[1]
            columns = columnsPart.rsplit(' or ')
            for c in columns:
                col.append(c.split('=')[0])
                values.append(c.split('=')[1])
        displayValues = query.split(',')
        table = query.split('from ', maxsplit=1)[1]
        table = table.split()

        displayValues[0] = re.sub('select ', '', displayValues[0], flags=re.IGNORECASE)
        displayValues[len(displayValues) - 1] = displayValues[len(displayValues) - 1].split(' from')[0]


        if ("*" in commands[1]):
            # print()
            displayValues = '*'
            filterData(table[0], col, values, displayValues)
        else:
            print()
            filterData(table[0], col, values, displayValues)

    elif (commands[0].lower() == updt.lower()):
        table = query.split(' SET', maxsplit=1)[0]
        table = re.sub('update ', '', table, flags=re.IGNORECASE)
        columnsPart = query.split('WHERE ')[1]
        columns = columnsPart.rsplit(' or ')
        updValues = query.split(',')
        updValues[0] = (re.sub('Update ' + table + ' set ', '', updValues[0], flags=re.IGNORECASE)).split('=')[1]
        updValues[len(updValues) - 1] = (updValues[len(updValues) - 1].split(' WHERE')[0]).split('=')[1]

        for c in columns:
            col.append(c.split('=')[0])
            values.append(c.split('=')[1])
        updateData(table, col, values, updValues)

    elif (commands[0].lower() == dlte.lower()):
        columnsPart = query.split('where ')[1]
        columns = columnsPart.rsplit(' or ')
        table = query.split('from ', maxsplit=1)[1]
        table = table.split()
        for c in columns:
            col.append(c.split('=')[0])
            values.append(c.split('=')[1])
        deleteData(table[0], col, values)


queryMaker('select * from S1')
