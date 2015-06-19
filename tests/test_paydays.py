
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
        check_date = date(2015, 1, 15)
        assert(check_date == last_pay_date)

    def test_is_payday_date(self):
        """whether a given day is a payday for that user. 
        If a date is not specified, default to today's date. 
        Return a boolean value"""
        d = date(2015, 1, 30)
        empid = 1

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
