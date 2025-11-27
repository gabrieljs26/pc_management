from odoo import models, fields

class Componente(models.Model):
    _name = "pc.component"
    _description = "Componentes de ordenador"

    nombre = fields.Char(string="Nombre técnico", required=True)
    especificaciones = fields.Text(string="Especificaciones")
    precio = fields.Monetary(string="Precio")
    currency_id = fields.Many2one("res.currency", default=lambda self: self.env.company.currency_id)
