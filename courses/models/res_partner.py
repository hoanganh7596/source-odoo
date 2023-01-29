# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class ResPartner(models.Model):
    _inherit = "res.partner"

    instructor = fields.Boolean(
        string='Is Instructor',
        default=False
    )
    course_ids = fields.Many2many(
        'course',
        string='Courses'
    )
