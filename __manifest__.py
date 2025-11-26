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
        'security/ir.model.access.csv',
        
        'views/pc_component_views.xml',
        'views/pc_computer_views.xml',
        'views/menu.xml',
        'views/templates.xml',
        'views/tags_views.xml',
        'views/views.xml',

    ],

    'demo': [
        'demo/demo.xml',
    ],
}
