from odoo import api, fields, models
from datetime import date

class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _description = "Hospital Appointment"
    _inherit = ['mail.thread','mail.activity.mixin']
    # _rec_name = 'patient_id'

    parent_id = fields.Many2one('hospital.patient', string='Patient')
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", related='parent_id.gender')
    appointment_time = fields.Date(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string='Booking Date', default=fields.Date.context_today)
    ref = fields.Char(string="Reference")
    days_to_booking_date = fields.Integer(string='No of Days ', compute='_compute_days')

    @api.depends('booking_date', 'appointment_time')
    def _compute_days(self):
        for rec in self:
            today = date.today()
            if rec.booking_date:
                rec.days_to_booking_date = rec.booking_date.day - today.day
            else:
                rec.days_to_booking_date = 0

    @api.onchange('patient_id')
    def onchange_patient_id(self):
        self.ref=self.patient_id.ref