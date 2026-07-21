from odoo import models, fields

class OSLHrPatient(models.Model):
    _name = 'odoo_school_library.patient'
    _description = 'Patient'

    name = fields.Char()
    description = fields.Char()