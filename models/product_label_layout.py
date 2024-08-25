from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)

class CustomProductLabelLayout(models.TransientModel):
    _name = 'custom.product.label.layout'
    _description = 'Custom Product Label Layout'

    print_format = fields.Selection([
        ('letter_label', 'Etiqueta en Formato Letter'),
    ], string="Formato de Impresión", required=True, default='letter_label')

    def process(self):
        _logger.info('Process method called in CustomProductLabelLayout for record ID: %s', self.id)

        # Definir el ID del informe
        report_xml_id = 'stock_move_label_extension.action_report_product_label_letter'

        try:
            # Intentar obtener la referencia del informe
            report = self.env.ref(report_xml_id, raise_if_not_found=False)
        except Exception as e:
            _logger.error('Error finding report with XML ID: %s. Exception: %s', report_xml_id, str(e))
            return {'type': 'ir.actions.act_window_close'}

        if report:
            # Obtener el ID de stock.picking desde el contexto
            stock_picking_id = self.env.context.get('active_id')
            if not stock_picking_id:
                _logger.error('No stock picking ID found in context.')
                return {'type': 'ir.actions.act_window_close'}

            # Buscar el registro de stock.picking
            stock_picking = self.env['stock.picking'].browse(stock_picking_id)
            if not stock_picking.exists():
                _logger.error('No valid stock picking record found for ID: %s', stock_picking_id)
                return {'type': 'ir.actions.act_window_close'}

            # Verificar si se está en modo de previsualización
            if self.env.context.get('preview_mode'):
                # Generar el informe en formato adecuado para previsualización (sin descargar)
                action = report.report_action(stock_picking, config=False)
            else:
                # Generar el informe en formato PDF
                action = report.report_action(stock_picking)

            # Verificar si se ha generado la acción
            if action:
                return action
            else:
                _logger.error('Failed to generate report action for Stock Picking ID: %s', stock_picking_id)
                return {'type': 'ir.actions.act_window_close'}
        else:
            _logger.error('Report not found.')
            return {'type': 'ir.actions.act_window_close'}
