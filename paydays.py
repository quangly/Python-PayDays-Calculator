"""
Author: Quang Ly
"""
import decimal
import datetime
from datetime import timedelta

"""mock data"""
paycycles = [
    {'empid' : 1, 'paydate': '2015-01-01'},
    {'empid' : 1, 'paydate': '2015-01-15'},
    {'empid' : 2, 'paydate': '2015-02-17'}
]


def get_last_pay(empid):
    """get last pay
    :params: int
    :return: date
    """
    seq = [x['paydate'] for x in paycycles if x['empid'] == empid]
    return(datetime.datetime.strptime(max(seq), "%Y-%m-%d").date())
    

def move_days(input_date, days):
    """
    Moves date by given number of +/- days
    """
    assert(type(input_date) is datetime.date)
    assert(type(days) is int)
    newdate = input_date + timedelta(days = days)
    message = "Input date {inputdate}: \t Days {days} \t New date {newdate}".format(inputdate=input_date, days=days, newdate=newdate)
    print(message)
    return newdate