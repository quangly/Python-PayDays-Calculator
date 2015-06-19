#Python PayDays Calculator

Challenge:
Write a python module that helps calculate paydays for a given user. Assume that a user's pay cycle data is stored as JSON within the user model. In order to minimize the scope of this project, only write the library to work for bi-weekly pay cycles. The module should work the same for all pay cycles, but you only need to implement the bi-weekly logic. The module requires the following features:


Given a user's pay cycle data provide functions to return the following:
- whether a given day is a payday for that user. 
- If a date is not specified, default to today's date. Return a boolean value
- get the user's next payday. Return a python date object.
- get the user's next X number of paydays starting at a given date. If a date is not supplied, default to today. Return python date objects.

#Unit Testing
- sniffer -x tests.test_paydays -x--nocapture -x--verbose
