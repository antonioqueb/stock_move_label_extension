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
        report_xml_id = 'stock_move_label_extension.action_report_product_label_letter'
        
        # Verifica si el reporte existe
        _logger.info('Attempting to generate report with ID: %s', report_xml_id)
        report = self.env.ref(report_xml_id, raise_if_not_found=False)
        
        if report:
            _logger.info('Report found: %s', report_xml_id)
            try:
                return report.report_action(self)
            except Exception as e:
                _logger.error('Error generating the report: %s', str(e))
                return {'type': 'ir.actions.act_window_close'}
        else:
            _logger.warning('Report not found for XML ID: %s', report_xml_id)
            return {'type': 'ir.actions.act_window_close'}
