from odoo import models, fields, api
from odoo.exceptions import UserError

class CustomProductLabelLayout(models.TransientModel):
    _name = 'custom.product.label.layout'
    _description = 'Custom Product Label Layout'

    print_format = fields.Selection([
        ('letter_label', 'Etiqueta en Formato Letter'),
    ], string="Formato de Impresión", required=True, default='letter_label')

    def process(self):
        try:
            # ID del reporte
            report_xml_id = 'stock_move_label_extension.action_report_product_label_letter'

            # Verificar si el reporte existe
            report_action = self.env['ir.model.data'].sudo().search([
                ('model', '=', 'ir.actions.report'),
                ('module', '=', 'stock_move_label_extension'),
                ('name', '=', report_xml_id)
            ])

            if not report_action:
                raise UserError("No se pudo encontrar el reporte con el ID especificado.")

            # Intentar generar la acción del reporte
            try:
                action = self.env.ref(report_xml_id).report_action(self)
                action['target'] = 'current'  # Cargar el reporte en la ventana/pestaña actual
                return action
            except Exception as e:
                raise UserError(f"Error al generar el reporte: {str(e)}")

        except UserError as ue:
            # Manejo de errores específicos de usuario
            raise ue

        except Exception as e:
            # Manejo de cualquier otra excepción no específica
            raise UserError(f"Ocurrió un error inesperado: {str(e)}")
