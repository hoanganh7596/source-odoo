# -*- coding: utf-8 -*-
from odoo import fields, models


class CourseRoom(models.Model):
    _name = "course.room"
    _description = "Student model"

    name = fields.Char(
        string='Name',
        required='True',
    )
    capacity = fields.Integer(
        string='Capacity')
