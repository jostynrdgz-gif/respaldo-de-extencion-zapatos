from odoo import models, fields 

class zapatoextension(models.model):
    _inherit = 'zapato'
    _description = 'este modulo es una extencion del modulo base zapato'

    proveedor = fields.Char(string="Proveedor")
    descuento = fields.Float(string="Descuento (%)")
    material = fields.Selection([
        ('cuero', 'Cuero'),
        ('sintetico', 'Sintético'),
        ('textil', 'Textil')
    ], string="Material")