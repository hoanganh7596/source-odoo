# -*- coding: utf-8 -*-
from odoo import fields, models


class Class(models.Model):
    _name = "project.class"
    _description = "Class model"

    name = fields.Char(
        string='Name',
        required='True',
    )
    student_ids = fields.One2many(
        comodel_name='student',
        inverse_name='class_id',
        string='Students')
