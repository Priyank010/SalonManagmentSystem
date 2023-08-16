import datetime
import os
import random
import string

ID_TYPES = (
    ('PAN CARD', 'PAN CARD'),
    ('AADHAR', 'AADHAR'),
    ('VOTER ID', 'VOTER ID'),
    ('DRIVING LICENCE', 'DRIVING LICENCE'),
    ('OTHERS', 'OTHERS')
)

Attendance_STATUS = (
    ('Present', 'Present'),
    ('Absent', 'Absent'),
    ('Leave', 'Leave')
)

marital_status = (
    ('Single', 'Single'),
    ('Married', 'Married')
)

discount_type = (
    ('Flat', 'Flat'),
    ('Percentage', 'Percentage')
)

transaction_type = (
    ('Debit','Debit'),
    ('Credit','Credit')
)

appointment_status = (
    ('Booked','Booked'),
    ('Cancelled','Cancelled'),
    ('Completed','Completed')
)

targer_type = (
    ('Sales','Sales'),
    ('Service','Service')
)

user_STATUS = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected')
)