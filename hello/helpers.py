import pandas as pd
import datetime
import random
from .models import Citations
from datetime import date

def change_datetime_header(dataframe):
    newColumns = []
    for key in dataframe.keys():
        if isinstance(key, datetime.datetime):
            key = key.strftime('%d-%b')
        newColumns.append(key)
    dataframe.columns = newColumns
    # return dataframe

def get_sheet(filename, sheet, userEmail):
    data = pd.read_excel(filename, index_col=0, sheet_name=sheet,header=1, parse_dates=True,)
    subjects = data[data['Mail'] == 'Temat zajęć']
    userAttendance = data[data['Mail'] == userEmail]
    change_datetime_header(subjects)
    change_datetime_header(userAttendance)
    result = subjects.append(userAttendance)
    htmlResult = result.to_html(bold_rows=True, na_rep='', justify='center')
    return htmlResult

def get_faculty_login(user):
    if user.is_authenticated and not is_admin(user):
        mail = user.username.split("@")[1]
        if (mail.__contains__("ug.edu.pl")):
            return 'ug'
        elif (mail.__contains__("pjwstk.edu.pl")):
            return 'pjatk'
        else:
            return None
    else:
        return None

def is_admin(user):
    if user.username == "admin":
        return True
    else:
        return False

def is_vacation():
    today = date.today()
    if (today.month >= 7 and today.month <= 10):
        vacation = True
    else:
        vacation = False
    return vacation

def get_random_citation():
    citations = Citations.objects.all()
    randomIndex = random.randint(0, len(citations)-1)
    randomCitation = citations[randomIndex]
    return randomCitation

# def get_attendance_sheet():
#     data = pd.read_excel('https://inf.ug.edu.pl/~mmiotk/TestoweZajecia.xlsx', index_col=0, sheet_name='Obecnosci',header=1, parse_dates=True)
#     subjects = data[data['Mail'] == 'Temat zajęć']
#     userAttendance = data[data['Mail'] == 'mateusz.miotk@ug.edu.pl']
#     change_datetime_header(subjects)
#     change_datetime_header(userAttendance)
#     result = subjects.append(userAttendance)
#     htmlResult = result.to_html(bold_rows=True, na_rep='', justify='center')
#     return htmlResult
#
# def get_grades_sheet():
#     data = pd.read_excel('https://inf.ug.edu.pl/~mmiotk/TestoweZajecia.xlsx', index_col=0, sheet_name='Punkty',header=1, parse_dates=True)
#     subjects = data[data['Mail'] == 'Temat zajęć']
#     userAttendance = data[data['Mail'] == 'mateusz.miotk@ug.edu.pl']
#     change_datetime_header(subjects)
#     change_datetime_header(userAttendance)
#     result = subjects.append(userAttendance)
#     htmlResult = result.to_html(bold_rows=True, na_rep='', justify='center')
#     return htmlResult