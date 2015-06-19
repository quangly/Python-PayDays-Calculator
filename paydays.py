"""
Author: Quang Ly
"""
import decimal
import datetime
from datetime import timedelta, date

""" {'empid' : 1, 'paydate': '2015-01-15'},
    {'empid' : 1, 'paydate': '2015-01-30'},
"""   

"""mock data"""
PAYCYCLES = [
    {'empid' : 1, 'paydate': '2015-01-01'},
    {'empid' : 2, 'paydate': '2015-02-17'}
]

FREQUENCY = 15

def get_last_pay(empid):
    """get last pay
    :params: int
    :return: date
    """
    seq = [x['paydate'] for x in PAYCYCLES if x['empid'] == empid]
    return(datetime.datetime.strptime(max(seq), "%Y-%m-%d").date())
    

def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

def dayrange(start_date, end_date):
    return (end_date - start_date).days

def is_payday(empid, date = None):
    """for given empid and date, return bool on valid paydate
    :params: int, date
    :return bool
    """
    'get last paydate'
    if date is None:
        date = datetime.datetime.now().date()
    last_paydate = get_last_pay(empid)

    'return bool whether range is divisible by FREQUENCY paycycle'
    'TOOO: add exception to holidays, etc'
    return dayrange(last_paydate, date) % FREQUENCY == 0


def move_days(input_date, days):
    """
    Moves date by given number of +/- days
    """
    assert(type(input_date) is datetime.date)
    assert(type(days) is int)
    newdate = input_date + timedelta(days = days)
    # message = "Input date {inputdate}: \t Days {days} \t New date {newdate}".format(inputdate=input_date, days=days, newdate=newdate)
    # print(message)
    return newdate