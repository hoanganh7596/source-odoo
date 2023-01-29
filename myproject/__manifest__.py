# -*- coding: utf-8 -*-

{
    'name': 'My Project',
    'version': '1.0.0',
    'category': 'Hidden',
    'depends': ['base'],
    'description': """
Module for School management
===============================================
    """,
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'report/report.xml',
        'views/class_views.xml',
        'views/student_views.xml',
        'views/student_menus.xml',
    ],
    'demo': [
    ],
    'assets': {
    },
    'installable': True,
    'license': 'LGPL-3',
}
