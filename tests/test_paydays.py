
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

    def test_get_last_pay(self):
        """For given empid, get latest pay"""
        empid = 1
        last_pay_date = paydays.get_last_pay(1)
        check_date = date(2015, 1, 1)
        assert(check_date == last_pay_date)

    def test_dayrange(self):
        "test get number of days bewteen date"
        start_date = date(2015, 1, 1)
        end_date = date(2015, 1, 31)
        # print(30 % 15)
        print(paydays.dayrange(start_date, end_date))


    def test_is_payday_true(self):
        """Whether a given day IS a payday for that user. If a date is not specified, default to today's date. """
        d = date(2015, 1, 31)
        empid = 1
        is_paydate = paydays.is_payday(empid, d)
        assert(is_paydate == True)

    def test_is_payday_true_false(self):
        """Whether a given day is NOT payday for that user. If a date is not specified, default to today's date. """
        d = date(2015, 1, 15)
        empid = 1
        is_paydate = paydays.is_payday(empid, d)
        assert(is_paydate == False)

    def test_is_payday_current_day(self):
        "If no payday given, use current day"
        empid = 1
        is_paydate = paydays.is_payday(empid, None)
        assert(is_paydate == False)

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
