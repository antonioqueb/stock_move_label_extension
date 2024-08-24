from odoo.tests import common

class TestStockMoveLabelExtension(common.TransactionCase):
    def setUp(self):
        super(TestStockMoveLabelExtension, self).setUp()
        # Setup para las pruebas
        # Crear un registro de stock picking para usar en las pruebas
        self.picking = self.env['stock.picking'].create({
            'name': 'Test Picking',
            'partner_id': self.env.ref('base.res_partner_1').id,
            'picking_type_id': self.env.ref('stock.picking_type_out').id,
        })
        
    def test_action_open_label_layout(self):
        # Verifica si la acción "Imprimir Etiquetas Personalizadas" está disponible
        action = self.env.ref('stock_move_label_extension.action_open_label_layout')
        self.assertTrue(action, "La acción 'Imprimir Etiquetas Personalizadas' no está disponible.")
        
    def test_report_generation(self):
        # Simula el proceso de generación del informe de etiquetas
        wizard = self.env['custom.product.label.layout'].create({
            'print_format': 'letter_label'
        })
        report_action = wizard.process()
        self.assertEqual(report_action['type'], 'ir.actions.report', "El reporte no fue generado correctamente.")
        self.assertEqual(report_action['report_name'], 'stock_move_label_extension.report_product_label_letter',
                         "El nombre del reporte generado no es correcto.")
        
    def test_view_inherited(self):
        # Verifica si la vista heredada está presente y correctamente configurada
        view = self.env.ref('stock_move_label_extension.view_picking_form_inherit_print_label')
        self.assertTrue(view, "La vista personalizada no está disponible.")
