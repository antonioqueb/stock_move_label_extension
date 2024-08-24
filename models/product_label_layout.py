from odoo import models, fields, api

class CustomProductLabelLayout(models.TransientModel):
    _name = 'custom.product.label.layout'
    _description = 'Custom Product Label Layout'

    print_format = fields.Selection([
        ('letter_label', 'Etiqueta en Formato Letter'),
    ], string="Formato de Impresión", required=True, default='letter_label')

    def process(self):
        report_xml_id = 'stock_move_label_extension.action_report_product_label_letter'
        # Verifica si el reporte existe
        if self.env['ir.model.data'].sudo().search([('model', '=', 'ir.actions.report'), ('module', '=', 'stock_move_label_extension'), ('name', '=', report_xml_id)]):
            action = self.env.ref(report_xml_id).report_action(self)
            action['target'] = 'current'  # Cargar el reporte en la ventana/pestaña actual
            return action
        else:
            return {'type': 'ir.actions.act_window_close'}
