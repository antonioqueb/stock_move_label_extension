from odoo import models, fields

class CustomProductLabelLayout(models.TransientModel):
    _name = 'custom.product.label.layout'
    _description = 'Custom Product Label Layout'

    print_format = fields.Selection([
        ('letter_label', 'Etiqueta en Formato Letter'),
    ], string="Formato de Impresión", required=True, default='letter_label')

    def process(self):
        # Asegúrate de que el 'id' del reporte aquí coincida exactamente con el 'id' definido en el XML
        if self.print_format == 'letter_label':
            return self.env.ref('stock_move_label_extension.action_report_product_label_letter').report_action(self)
        else:
            return super(CustomProductLabelLayout, self).process()
