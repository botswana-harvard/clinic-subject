from dateutil.relativedelta import relativedelta

from edc_visit_schedule import Schedule, Visit

from .requisitions import requisitions

from ..visit_schedule import crfs


schedule1 = Schedule(
    name='schedule1',
    title='Bcpp Clinic',
    enrollment_model='bcpp_clinic_subject.enrollment',
    disenrollment_model='bcpp_clinic_subject.disenrollment',)

visit0 = Visit(
    code='C1',
    title='Clinic Subject Survey',
    timepoint=0,
    rbase=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crfs)

schedule1.add_visit(visit=visit0)
