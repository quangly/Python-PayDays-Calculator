
import sys
import unittest
sys.path.append("..")
import datetime
from datetime import date
from pprint import pprint as pp
import json
import paydays
from nose.tools import eq_
from datetime import timedelta
class TestHelper(unittest.TestCase):
    def setUp(self):
        "Setup test fixtures"
        pass
    def tearDown(self):
        "Tear down test fixtures"
        pass

    def test_is_payday_true(self):
        """CASE (1a) Whether a given day IS a payday for that user.
        return bool
        """
        d = date(2015, 1, 31)
        empid = 1
        is_paydate = paydays.is_payday(empid, d)
        assert(is_paydate == True)


    def test_is_payday_date(self):
        """CASE (1b) Whether a given day is NOT payday for that user.  """
        mydate = date(2015, 1, 15)
        empid = 1
        assert(paydays.is_payday(empid, mydate) == False)

    def test_is_payday_current_date(self):
        """CASE (1c) For given empid, if no payday given, use current day"""
        mydate = datetime.datetime.now().date()
        empid = 1
        is_paydate = paydays.is_payday(empid, mydate)
        assert(is_paydate == False)

    def test_get_next_paydate(self):
        """CASE (2) For given empid, get NEXT pay date
        return date
        """
        empid = 1
        last_pay_date = paydays.get_next_pay(1)
        check_date = date(2015, 1, 16)
        assert(check_date == last_pay_date)

    def test_get_x_paydays_paydate(self):
        """CASE (3a) For given date, get the user's next X number of paydays. 
        Return python date objects."""
        end_date = date(2015, 2, 15)
        empid = 1
        count, found_paydates = paydays.get_x_paydays(empid, end_date)
        check_found_paydates = [datetime.date(2015, 1, 16), 
                                datetime.date(2015, 1, 31), 
                                datetime.date(2015, 2, 15)]
        assert(count == 3)
        assert(found_paydates == check_found_paydates)

    def skip_get_x_paydays_nodate(self):
        """CASE (3b) For NO given date, use current date, get the user's next X number of paydays. 
        Return python date objects."""
        end_date = datetime.datetime.now().date()
        empid = 1
        count, found_paydates = paydays.get_x_paydays(empid, end_date)
        print('\n')
        for date in found_paydates:
            print(date)

    def test_get_last_paydate(self):
        """For given empid, get PREVIOUS pay date"""
        empid = 1
        last_pay_date = paydays.get_last_pay(1)
        assert(date(2015, 1, 1) == last_pay_date)

    def test_get_first_paydate(self):
        """For given empid, get FIRST pay date"""
        empid = 1
        first_pay_date = paydays.get_first_pay(1)
        assert(date(2014, 1, 17) == first_pay_date)

    def test_dayrange(self):
        "Test get number of days between date"
        start_date = date(2015, 1, 1)
        end_date = date(2015, 1, 31)
        assert(paydays.dayrange(start_date, end_date) == 30)


    def test_move_days_plus(self):
        "Test add 10 move_days"
        mydate = datetime.datetime.now().date()
        days = 10
        newdate = paydays.move_days(mydate, days)

        assert(newdate == mydate + timedelta(days = days))

    def test_move_days_minus(self):
        "Test minus 10 move_days"
        mydate = datetime.datetime.now().date()
        days = -10
        newdate = paydays.move_days(mydate, days)

        assert(newdate == mydate + timedelta(days = days))
