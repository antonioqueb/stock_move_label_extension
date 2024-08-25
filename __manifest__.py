{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',  # Permisos de seguridad
        'report/report_product_label_template_letter.xml',  # Plantilla y reporte QWeb
        'views/custom_product_label_action.xml',  # Vistas y acciones
        'views/view_picking_form_inherit_print_label.xml'  # Vista personalizada del picking con el botón para imprimir etiquetas
    ],
    'installable': True,
    'application': False,
}
