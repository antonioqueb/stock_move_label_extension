{
    'name': 'Stock Move Label Extension',
    'version': '1.0',
    'depends': ['stock', 'product'],
    'data': [
        'security/ir.model.access.csv',  # Permisos de seguridad
        'views/report_product_label_template_letter.xml',  # Plantilla del reporte
        'views/report_action.xml',  # Mueve la acción del reporte a 'views/'
        'views/custom_product_label_layout_view.xml',
        'views/custom_product_label_action.xml',
        'views/stock_picking_action_print_label.xml',
        'views/stock_picking_view_inherit.xml',
    ],
    'installable': True,
    'application': False,
}
