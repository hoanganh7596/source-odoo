# -*- coding: utf-8 -*-
from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class Course(models.Model):
    _name = "course"
    _description = "Course Model"

    name = fields.Char(
        string='Name',
        required='True',
    )
    instructor_id = fields.Many2one(
        'res.partner',
        string='Instructor',
    )
    room_id = fields.Many2one(
        'course.room',
        string='Room',
    )
    attendant_ids = fields.Many2many(
        'res.partner',
        string='Attendants',
    )
    # lesson_ids = fields.One2many(
    #     comodel_name='course.lesson',
    #     inverse_name='course_id',
    #     string='Lessons')

    @api.constrains('attendant_ids', 'room_id', 'room_id.capacity')
    def _check_room_capacity(self):
        for course in self:
            if course.room_id and course.room_id.capacity:
                if len(course.attendant_ids.ids) > course.room_id.capacity:
                    raise ValidationError(_('Numbers of attendants can not greater than room capacity'))
