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

        # Verificar el formato de impresión seleccionado
        _logger.debug('Selected print format: %s', self.print_format)

        report_xml_id = 'stock_move_label_extension.action_report_product_label_letter'
        _logger.info('Attempting to generate report with ID: %s', report_xml_id)

        # Verificar si existe el reporte en el sistema
        try:
            report = self.env.ref(report_xml_id, raise_if_not_found=False)
            _logger.debug('Report reference fetched: %s', report)
        except Exception as e:
            _logger.error('Error finding report with XML ID: %s. Exception: %s', report_xml_id, str(e))
            return {'type': 'ir.actions.act_window_close'}

        if report:
            _logger.info('Report found: %s', report_xml_id)

            # Intentar generar la acción del reporte con los datos correctos
            try:
                # Asegúrate de que pasas el registro correcto para el reporte
                stock_picking_id = self.env.context.get('active_id')
                if not stock_picking_id:
                    _logger.error('No stock picking ID found in context.')
                    return {'type': 'ir.actions.act_window_close'}

                stock_picking = self.env['stock.picking'].browse(stock_picking_id)
                if not stock_picking.exists():
                    _logger.error('No valid stock picking record found for ID: %s', stock_picking_id)
                    return {'type': 'ir.actions.act_window_close'}

                _logger.info('Generating report for Stock Picking ID: %s', stock_picking_id)

                # Llamar a report_action con los datos correctos
                action = report.report_action(stock_picking)

                # Verificar el contenido de la acción generada
                _logger.debug('Report action result: %s', action)

                # Verificar si la acción del reporte fue generada exitosamente
                if action:
                    _logger.info('Report action generated successfully for Stock Picking ID: %s', stock_picking_id)
                    return action
                else:
                    _logger.warning('Report action returned None for Stock Picking ID: %s', stock_picking_id)
                    return {'type': 'ir.actions.act_window_close'}
            except Exception as e:
                _logger.error('Error generating the report action for Stock Picking ID: %s. Exception: %s', stock_picking_id, str(e))
                return {'type': 'ir.actions.act_window_close'}
        else:
            _logger.warning('Report not found for XML ID: %s, Process aborted for record ID: %s', report_xml_id, self.id)
            return {'type': 'ir.actions.act_window_close'}
