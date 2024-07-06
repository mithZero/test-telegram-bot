import gspread

gc = gspread.service_account(filename="./credentials.json")

sheet = gc.open("гугл_табличка")