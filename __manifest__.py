{
    'name': 'Gestión de PCs de Empresa',
    'version': '1.0',
    'author': 'Alejandro Ibáñez',
    'category': 'Tools',
    'summary': 'Gestión de ordenadores, componentes y mantenimiento.',
    'description': """
Módulo para gestionar ordenadores, componentes, precios, incidencias y usuarios
asociados. Incluye relaciones Many2one, Many2many, restricciones y tags.
""",
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/componente_views.xml',
        'views/ordenador_views.xml',
        'views/menus.xml',
        'views/templates.xml',
        'views/tags_views.xml',
        'views/views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
