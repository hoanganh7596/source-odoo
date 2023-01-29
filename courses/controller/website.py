# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class CourseController(http.Controller):
    @http.route('/course', type='http', auth='user', website=True)
    def show_custom_webpage(self, **kw):
        return http.request.render('courses.new_web_page', {})
