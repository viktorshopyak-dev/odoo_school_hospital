from odoo import models, fields

class OSLHrHospital(models.Model):
    _name = 'odoo_school_library.doctor'
    _description = 'Doctor'

    name = fields.Char()
    description = fields.Char()

