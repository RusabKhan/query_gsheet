In the sheets.py class there is a variable "gs" in it put the api credential location for you gsheet api as frist argument and the spreadsheet name as 2nd argument.

gs = initialize("Your_credential.json","Your spreadsheet name")



after that call the queryMaker method for sqlConverter.py and write a basic select/update/delete query in it.

queryMaker('select * from sheet1 where columnValue=yourValue')
queryMaker('UPDATE sheet1 SET columnValue=yourValue WHERE columnValue=NotyourValue')
queryMaker('delete from sheet1 WHERE columnValue=yourValue')


