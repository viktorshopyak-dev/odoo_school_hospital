from odoo import models, fields

class OSLHrVisit(models.Model):
    _name = 'odoo_school_library.visit'
    _description = 'Visit'

    name = fields.Char()
    description = fields.Char()
    res_disease_id = fields.Many2one(
        'odoo_school_library.disease',
        'Disease',
        ondelete='restrict',
        index=True,
    )
    res_doctor_id = fields.Many2one(
        'odoo_school_library.doctor',
        'Doctor',
        ondelete='restrict',
        index=True,
    )
    res_patient_id = fields.Many2one(
        'odoo_school_library.patient',
        'Patient',
        ondelete='restrict',
        index=True,
    )
