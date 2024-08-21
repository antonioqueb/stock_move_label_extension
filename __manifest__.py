{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',  # Permisos de seguridad
        'report/report_product_label_template_letter.xml',  # Plantilla del reporte
        'report/report_action.xml',  # Acción del reporte
        'views/custom_product_label_layout_view.xml',
        'views/custom_product_label_action.xml',
        'views/stock_picking_action_print_label.xml',
        'views/stock_picking_view_inherit.xml',
    ],
    'installable': True,
    'application': False,
}
