from odoo import models, fields

class CustomProductLabelLayout(models.TransientModel):
    _name = 'custom.product.label.layout'
    _description = 'Custom Product Label Layout'

    print_format = fields.Selection([
        ('letter_label', 'Etiqueta en Formato Letter'),
    ], string="Formato de Impresión", required=True, default='letter_label')

    def process(self):
        if self.print_format == 'letter_label':
            action = self.env.ref('stock_move_label_extension.action_report_product_label_letter').report_action(self)
            action['target'] = 'new'  # Abrir el reporte en una nueva pestaña
            return action
        else:
            return super(CustomProductLabelLayout, self).process()
