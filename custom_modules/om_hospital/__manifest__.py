# -*- coding: utf-8 -*-



{
    'name': 'Hospital Management ',
    'version': '1.0.0',
    'category': 'Hospital',
    'author': 'Joshua Mumo',
    'sequence': -200,
    'summary': 'Hospital management system',
    'description': """ Hospital management system """,
    'depends': [],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_views.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}