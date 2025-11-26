from odoo import models, fields

class PcTag(models.Model):
    _name = "pc.tag"
    _description = "Etiqueta de PC"

    name = fields.Char(string="Nombre de la etiqueta")
