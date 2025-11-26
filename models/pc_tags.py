from odoo import models, fields

class PcTags(models.Model):
    _name = "pc.tags"
    _description = "Etiqueta de PC"

    name = fields.Char(string="Nombre de la etiqueta")
