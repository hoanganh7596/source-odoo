# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class Student(models.Model):
    _name = "student"
    _description = "Student model"

    name = fields.Char(
        string='Name',
        required='True',
    )
    student_identify = fields.Char(
        string='ID',
        required='True',
        copy='False',
        default=lambda self: _('New'),
    )
    class_id = fields.Many2one(
        comodel_name='project.class',
        string='Class'
    )

    #=== CRUD METHODS ===#
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('student_identify', _("New")) == _("New"):
                vals['student_identify'] = self.env[
                    'ir.sequence'].next_by_code(
                    'student.identify') or _("New")
        return super().create(vals_list)
