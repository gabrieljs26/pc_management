from odoo import models, fields

class Tags(models.Model):
    _name = "pc.tags"
    _description = "Tags de Sistema Operativo"

    name = fields.Char(string="Etiqueta")
