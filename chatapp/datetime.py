from datetime import datetime

def get_datetime():
    d=datetime.now()
    if int(d.hour)>12:
        hour=int(d.hour)-12
        date=month_f(d.month)+" "+str(d.day)+", "+str(d.year)+", "+str(hour)+":"+str(d.minute)+" p.m."
    else:
        date=month_f(d.month)+" "+str(d.day)+", "+str(d.year)+", "+str(d.hour)+":"+str(d.minute)+" p.m."
    return date

def month_f(month):
    all={1:'January',
         2:'February',
         3:'March',
         4:'April',
         5:'May',
         6:'June',
         7:'July',
         8:'August',
         9:'September',
         10:'October',
         11:'November',
         12:'December'
         }
    return all[month]