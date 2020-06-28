# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###
from __future__ import absolute_import

from .api.timeslots import Timeslots
from .api.timeslots_dentist_name import TimeslotsDentistName
from .api.timeslots_dentist_name_available import TimeslotsDentistNameAvailable
from .api.appointments_book import AppointmentsBook
from .api.appointments_cancel import AppointmentsCancel
from .api.appointments_appointment_id_cancel import AppointmentsAppointmentIdCancel
from .api.appointments_appointment_id import AppointmentsAppointmentId


routes = [
    dict(resource=Timeslots, urls=['/timeslots'], endpoint='timeslots'),
    dict(resource=TimeslotsDentistName, urls=['/timeslots/<dentist_name>'], endpoint='timeslots_dentist_name'),
    dict(resource=TimeslotsDentistNameAvailable, urls=['/timeslots/<dentist_name>/available'], endpoint='timeslots_dentist_name_available'),
    dict(resource=AppointmentsBook, urls=['/appointments/book'], endpoint='appointments_book'),
    dict(resource=AppointmentsCancel, urls=['/appointments/cancel'], endpoint='appointments_cancel'),
    dict(resource=AppointmentsAppointmentIdCancel, urls=['/appointments/<appointment_id>/cancel'], endpoint='appointments_appointment_id_cancel'),
    dict(resource=AppointmentsAppointmentId, urls=['/appointments/<appointment_id>'], endpoint='appointments_appointment_id'),
]