import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class OSLHrDiseases(models.Model):
    _name = 'odoo_school_library.disease'
    _description = 'Disease'
    _parent_name = 'parent_id'
    _parent_store = True
    _order = 'parent_path'
    _rec_name = 'complete_name'


    name = fields.Char(required=True)
    description = fields.Char()

    parent_id = fields.Many2one(
        'odoo_school_library.disease',
        string='Parent Disease',
        ondelete='restrict',
        index=True,
    )
    child_ids = fields.One2many(
        'odoo_school_library.disease',
        'parent_id',
        string='Child Diseases',
    )
    parent_path = fields.Char(index=True, unaccent=False)

    complete_name = fields.Char(
        string='Complete Name',
        compute='_compute_complete_name',
        recursive=True,
        store=True,
    )

    display_name_intended = fields.Char(
        string='Name',
        compute='_compute_display_name_intended',
        recursive=True,
        store=True,
    )

    @api.depends('name', 'parent_id.complete_name')
    def _compute_complete_name(self):
        for disease in self:
            if disease.parent_id:
                disease.complete_name = f'{disease.parent_id.complete_name} / {disease.name}'
            else:
                disease.complete_name = disease.name

    @api.depends('name', 'parent_path')
    def _compute_display_name_intended(self):
        for disease in self:
            level = (disease.parent_path.count('/')-1) if disease.parent_path else 0
            if level:
                disease.display_name_intended = ('-'*level) + str(disease.name or ' ')
            else:
                disease.display_name_intended = disease.name

    @api.constrains('parent_id')
    def _check_hierarchy(self):
        if not self._check_recursion():
            raise models.ValidationError('Помилка! Ви не можете створити рекурсивну ієрархію хвороб.')
