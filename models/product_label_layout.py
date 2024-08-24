from odoo import models, fields, api, _
import logging
import json

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

            # Intentar generar la acción del reporte
            try:
                _logger.debug('Attempting to call report_action on the report with context: %s', json.dumps(self.env.context))

                # Registrar el contexto actual, para verificar que se pasan correctamente los datos
                context_copy = self.env.context.copy()
                _logger.debug('Current context: %s', json.dumps(context_copy))

                # Registrar el ID del usuario actual y la compañía
                _logger.debug('Current user ID: %s, Company ID: %s', self.env.user.id, self.env.user.company_id.id)

                action = report.report_action(self)

                # Registrar el contenido de la acción generada
                _logger.debug('Report action result: %s', action)

                # Verificar los datos devueltos por report_action
                if action:
                    _logger.info('Report action generated successfully for record ID: %s', self.id)
                else:
                    _logger.warning('Report action returned None for record ID: %s', self.id)

                return action
            except Exception as e:
                _logger.error('Error generating the report action for record ID: %s. Exception: %s', self.id, str(e))

                # Registrar información de depuración adicional del entorno y contexto
                _logger.debug('Exception context: %s', json.dumps(self.env.context))
                _logger.debug('Exception user ID: %s, Company ID: %s', self.env.user.id, self.env.user.company_id.id)

                return {'type': 'ir.actions.act_window_close'}
        else:
            _logger.warning('Report not found for XML ID: %s, Process aborted for record ID: %s', report_xml_id, self.id)
            return {'type': 'ir.actions.act_window_close'}
