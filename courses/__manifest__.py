# -*- coding: utf-8 -*-

{
    'name': 'Courses',
    'version': '1.0.0',
    'category': 'Hidden',
    'depends': ['base', 'contacts'],
    'description': """
Module for Courses
===============================================
    """,
    'data': [
        'security/ir.model.access.csv',
        'views/course_views.xml',
        'views/course_room_views.xml',
        'views/course_menus.xml',
        'views/res_partner_views.xml',
    ],
    'demo': [
    ],
    'assets': {
    },
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
