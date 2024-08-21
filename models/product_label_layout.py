from odoo import models, fields

class ProductLabelLayout(models.TransientModel):
    _inherit = 'product.label.layout.form'

    print_format = fields.Selection(selection_add=[('new_label', 'Nuevo Reporte de Etiquetas')])

    def process(self):
        if self.print_format == 'new_label':
            return self.env.ref('stock_move_label_extension.action_report_product_label_new').report_action(self)
        return super(ProductLabelLayout, self).process()
