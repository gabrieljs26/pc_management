# -*- coding: utf-8 -*-
{
    'name': "PC Management",

    'summary': "Gestión de ordenadores en Odoo",

    'description': """
Módulo para gestionar PCs, componentes o inventario de equipos.
    """,

    'author': "Gabi",
    'website': "https://github.com/tuusuario/pc_management",

    'category': 'Inventory',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'views/views.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
    ],

    'demo': [
        'demo/demo.xml',
    ],
}
