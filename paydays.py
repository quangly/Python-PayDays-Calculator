"""
Author: Quang Ly
"""
import decimal
import datetime
from datetime import timedelta, date

"""
mock data
use a service to get employee pay records
"""
PAYCYCLES = [
    {'empid' : 1, 'paydate': '2014-01-17'},
    {'empid' : 1, 'paydate': '2015-01-01'},
    {'empid' : 2, 'paydate': '2015-02-17'},
    {'empid' : 3, 'paydate': '2015-02-17'}
]

FREQUENCY = 15 #biweekly frequency of days
YEARS  = 5 #default years of assumed employment
DAYS = 364 #
TOTAL_DAYS_CHECK = YEARS * DAYS


def get_last_pay(empid):
    """get last pay
    :params: int
    :return: date
    """
    paydays = [x['paydate'] for x in PAYCYCLES if x['empid'] == empid]
    return(datetime.datetime.strptime(max(paydays), "%Y-%m-%d").date())

def get_first_pay(empid):
    """get last pay
    :params: int
    :return: date
    """
    paydays = [x['paydate'] for x in PAYCYCLES if x['empid'] == empid]
    return(datetime.datetime.strptime(min(paydays), "%Y-%m-%d").date())

def get_next_pay(empid):
    """for given empid, get next pay date
    :params: int
    :return date
    """
    last_paydate = get_last_pay(empid)
    next_paydate = move_days(last_paydate, FREQUENCY)
    return next_paydate

def daterange(start_date, end_date):
    """get list of ranges
    return list or generator"""
    dates = []
    for n in range(int ((end_date - start_date).days)):
        # yield start_date + timedelta(n)
        dates.append(start_date + timedelta(n))
    return dates

def dayrange(start_date, end_date):
    return (end_date - start_date).days

def get_x_paydays(empid, end_date):
    """
    Get X number of pay days for a given end date and last date of empid
    """
    start_date = get_last_pay(empid)
    next_paydate = move_days(start_date, FREQUENCY)

    '''days between start and end date'''
    days_range = daterange(start_date, move_days(end_date, 1)) #add 1 day to make it inclusive
    i = 1 # iterator

    found_paydates = []
    while True:
        '''check when to exit loop'''
        if i <= TOTAL_DAYS_CHECK:
            if next_paydate in days_range:
                found_paydates.append(next_paydate)
            next_paydate = move_days(next_paydate, FREQUENCY)    
        else:
            break
        i+=1

    return len(found_paydates), found_paydates

def is_payday(empid, date = None):
    """
    for given empid and date, return bool on valid paydate
    :params: int, date
    :return bool
    """

    count, found_paydates = get_x_paydays(empid, date)
    found = False
    for x in found_paydates:
        if date == x:
            found = True
            #found break out of loop
            break

    return found

def is_payday2(empid, date = None):
    """
    THIS IS AN ALTERNATE IMPLEMENTATION OF is payday using modulus
    for given empid and date, return bool on valid paydate
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