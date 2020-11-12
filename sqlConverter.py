import sheets

slct = 'select'
updt = 'update'
dlte = 'delete'


def queryMaker(query):
    commands = query.split()
    table = query.split('from ', maxsplit=1)[1]
    table = table.split()
    columnsPart = query.split('where ')[1]
    columns = columnsPart.rsplit('and')
    col = []
    values = []
    for c in columns:
        col = c.split('=')[0]
        values = c.split('=')[1]

    if ("*" not in commands[1]):
        # print()
        sheets.filterData(table[0], col, values)
    # print(columns)

    if (commands[0].lower() == slct.lower()):
        print()
    # print(sheets.filterData(table, colClause[1], columns))

    elif (commands[0].lower() == updt.lower()):
        updValues = commands[3].rsplit('=')
        colClause = commands[len(commands) - 1].rsplit('=')
    # print( sheets.updateData(colClause[0], colClause[1], updValues[0], updValues[1]))

    elif (commands[0].lower() == dlte.lower()):
        colClause = commands[len(commands) - 1].rsplit('=')


# print( sheets.deleteData(colClause[1]))


queryMaker('select keyword from S1 where Keyword=bookkeeping')

# lst = [("select keyword"),("bb8"),("ccc8"),("dddddd8")]

# print("rusab from spreadsheet where keyword=bookkeeping".split(' from', 1)[0])
# print([s.strip('select ') for s in lst]) # remove the 8 from the string borders
# print([s.replace('8', '') for s in lst]) # remove all the 8s
