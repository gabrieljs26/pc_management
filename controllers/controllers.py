# -*- coding: utf-8 -*-
# from odoo import http


# class /var/lib/odoo/addons/18.0/pcManagement(http.Controller):
#     @http.route('//var/lib/odoo/addons/18.0/pc_management//var/lib/odoo/addons/18.0/pc_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//var/lib/odoo/addons/18.0/pc_management//var/lib/odoo/addons/18.0/pc_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/var/lib/odoo/addons/18.0/pc_management.listing', {
#             'root': '//var/lib/odoo/addons/18.0/pc_management//var/lib/odoo/addons/18.0/pc_management',
#             'objects': http.request.env['/var/lib/odoo/addons/18.0/pc_management./var/lib/odoo/addons/18.0/pc_management'].search([]),
#         })

#     @http.route('//var/lib/odoo/addons/18.0/pc_management//var/lib/odoo/addons/18.0/pc_management/objects/<model("/var/lib/odoo/addons/18.0/pc_management./var/lib/odoo/addons/18.0/pc_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/var/lib/odoo/addons/18.0/pc_management.object', {
#             'object': obj
#         })

